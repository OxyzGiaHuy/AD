from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
from PIL import Image

from src.backbones.dinov2 import FeatureBatch, build_backbone
from src.calibration.platt import entropy_binary, reliability_bins
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import summarize_binary
from src.models.baselines import build_model
from src.robustness.attacks import parse_epsilon
from src.run_experiment import _fit_calibrator, _fit_vector_calibrator, encode_with_cache, load_feature_cache_if_present
from src.utils.io import ensure_dir, write_json, write_table


def _select_records(records, max_images: int | None):
    if not max_images:
        return records
    normals = [rec for rec in records if rec.label == 0]
    anomalies = [rec for rec in records if rec.label == 1]
    half = max(1, max_images // 2)
    return normals[:half] + anomalies[: max_images - half]


def _fgsm_features(backbone, records, model, epsilon: float, image_size: int, batch_size: int) -> FeatureBatch:
    import torch
    import torchvision.transforms.functional as TF

    if not hasattr(model, "pca"):
        raise NotImplementedError("FGSM image-space path currently requires a PCA-based model.")
    device = backbone.device
    mean = torch.tensor([0.485, 0.456, 0.406], device=device).view(1, 3, 1, 1)
    std = torch.tensor([0.229, 0.224, 0.225], device=device).view(1, 3, 1, 1)
    pca_mean = torch.from_numpy(model.pca.mean.astype(np.float32)).to(device)
    components = torch.from_numpy(model.pca.components.astype(np.float32)).to(device)

    patches = []
    for start in range(0, len(records), batch_size):
        batch_records = records[start : start + batch_size]
        images = []
        labels = []
        for rec in batch_records:
            image = Image.open(rec.path).convert("RGB")
            tensor = TF.to_tensor(TF.resize(image, [image_size, image_size], antialias=True))
            images.append(tensor)
            labels.append(float(rec.label))
        x = torch.stack(images, dim=0).to(device).requires_grad_(True)
        y = torch.tensor(labels, dtype=torch.float32, device=device)
        normed = (x - mean) / std
        out = backbone.model.forward_features(normed)
        feats = out["x_norm_patchtokens"]
        centered = feats - pca_mean
        coeff = centered @ components.t()
        recon = coeff @ components
        residual = ((centered - recon) ** 2).sum(dim=-1)
        score = residual.max(dim=1).values
        score_center = score.detach().mean()
        score_scale = score.detach().std().clamp_min(1e-6)
        logits = (score - score_center) / score_scale
        loss = torch.nn.functional.binary_cross_entropy_with_logits(logits, y)
        backbone.model.zero_grad(set_to_none=True)
        if x.grad is not None:
            x.grad.zero_()
        loss.backward()
        adv = torch.clamp(x + epsilon * x.grad.sign(), 0.0, 1.0).detach()
        with torch.no_grad():
            adv_out = backbone.model.forward_features((adv - mean) / std)
            patches.extend(adv_out["x_norm_patchtokens"].detach().cpu().numpy().astype(np.float32))
    n_patches = patches[0].shape[0] if patches else 0
    grid = int(n_patches**0.5)
    return FeatureBatch(np.stack(patches, axis=0), (grid, grid))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--epsilon", default="8/255")
    parser.add_argument("--max-images", type=int, default=None)
    args = parser.parse_args()

    config = load_config(args.config)
    dataset_cfg = config.get("dataset", {})
    experiment_cfg = config.get("experiment", {})
    backbone_cfg = config.get("backbone", {})
    model_cfg = dict(config.get("model", {}))
    model_cfg.setdefault("device", experiment_cfg.get("device", "cuda"))
    k = int(dataset_cfg.get("k_shots", [1])[0])
    seed = int(dataset_cfg.get("seeds", [0])[0])
    calibration_mode = config.get("calibration", {}).get("modes", ["normal_synthetic"])[0]
    epsilon = parse_epsilon(args.epsilon)

    records = load_records(dataset_cfg.get("name", "mvtec"), dataset_cfg.get("root"), dataset_cfg.get("classes", "all"))
    support = few_shot_support(records, k=k, seed=seed)
    eval_clean = _select_records(evaluation_records(records), args.max_images)
    labels = np.asarray([r.label for r in eval_clean], dtype=np.int64)

    backbone_name = backbone_cfg.get("name", "dinov2_vits14")
    image_size = int(dataset_cfg.get("image_size", backbone_cfg.get("image_size", 518)))
    batch_size = int(backbone_cfg.get("batch_size", 4))
    cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")
    dataset_name = dataset_cfg.get("name", "dataset")
    support_cache_name = f"{dataset_name}_support_{backbone_name}_k{k}_seed{seed}"
    support_batch = load_feature_cache_if_present(support, cache_dir, support_cache_name, seed, backbone_name, image_size)
    if support_batch is None:
        backbone_for_cache = build_backbone(backbone_name, device=experiment_cfg.get("device", "cuda"), image_size=image_size, batch_size=batch_size)
        support_batch = encode_with_cache(backbone_for_cache, support, cache_dir, support_cache_name, seed, backbone_name, image_size)

    support_features = support_batch.patch_features
    model = build_model(model_cfg.get("variant", "calib_subspace_head"), support_features, model_cfg, seed=seed)
    support_scores, _ = model.score_images(support_features)

    backbone = build_backbone(backbone_name, device=experiment_cfg.get("device", "cuda"), image_size=image_size, batch_size=batch_size)
    adv_batch = _fgsm_features(backbone, eval_clean, model, epsilon=epsilon, image_size=image_size, batch_size=batch_size)
    adv_features = adv_batch.patch_features
    raw_scores, patch_scores = model.score_images(adv_features)
    if hasattr(model, "calibration_features"):
        calibrator, _, adv_vec = _fit_vector_calibrator(
            calibration_mode,
            model,
            support_features,
            adv_features,
            labels,
            seed=seed,
            synthetic_ratio=float(model_cfg.get("synthetic_anomaly_ratio", 1.0)),
        )
        probs = calibrator.predict_proba(adv_vec)
    else:
        calibrator = _fit_calibrator(calibration_mode, support_scores, raw_scores, labels)
        probs = calibrator.predict_proba(raw_scores)
    entropy = entropy_binary(probs)
    metrics = summarize_binary(labels, raw_scores, probs, bins=int(config.get("calibration", {}).get("bins", 15)))
    metrics.update({"k_shot": k, "seed": seed, "attack": "fgsm_image_pca_surrogate", "epsilon": args.epsilon, "epsilon_float": epsilon, "num_images": len(eval_clean)})

    eps_tag = args.epsilon.replace("/", "_").replace(".", "p")
    run_name = f"{experiment_cfg.get('name', 'experiment')}_{model_cfg.get('variant', 'model')}_k{k}_seed{seed}_fgsm_eps{eps_tag}"
    out_dir = Path(experiment_cfg.get("output_dir", "outputs")) / "robustness" / run_name
    ensure_dir(out_dir / "anomaly_maps")
    write_json(out_dir / "metrics.json", metrics)
    write_json(out_dir / "calibration_bins.json", {"bins": reliability_bins(labels, probs, bins=int(config.get("calibration", {}).get("bins", 15)))})
    rows = []
    for rec, score, prob, ent in zip(eval_clean, raw_scores, probs, entropy):
        rows.append(
            {
                "image_path": rec.path,
                "label": rec.label,
                "raw_score": float(score),
                "calibrated_probability": float(prob),
                "entropy": float(ent),
                "class": rec.category,
                "seed": seed,
                "corruption": "none",
                "attack": "fgsm_image_pca_surrogate",
                "epsilon": args.epsilon,
            }
        )
    write_table(out_dir / "predictions", rows)
    np.save(out_dir / "anomaly_maps" / "patch_scores.npy", patch_scores.astype(np.float32))
    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
