from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import sys

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.backbones.dinov2 import FeatureBatch, build_backbone
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import summarize_binary
from src.models.baselines import build_model
from src.robustness.attacks import parse_epsilon
from src.run_experiment import encode_with_cache, load_feature_cache_if_present


def select_records(records, max_images: int) -> list:
    normals = [rec for rec in records if rec.label == 0]
    anomalies = [rec for rec in records if rec.label == 1]
    half = max(1, max_images // 2)
    return normals[:half] + anomalies[: max_images - half]


def fgsm_features(backbone, records, model, epsilon: float, image_size: int, batch_size: int, direction: str) -> FeatureBatch:
    import torch
    import torchvision.transforms.functional as TF

    device = backbone.device
    mean = torch.tensor([0.485, 0.456, 0.406], device=device).view(1, 3, 1, 1)
    std = torch.tensor([0.229, 0.224, 0.225], device=device).view(1, 3, 1, 1)
    pca_mean = torch.from_numpy(model.pca.mean.astype(np.float32)).to(device)
    components = torch.from_numpy(model.pca.components.astype(np.float32)).to(device)
    sign = 1.0 if direction == "ascent" else -1.0

    patches = []
    for start in range(0, len(records), batch_size):
        batch_records = records[start : start + batch_size]
        images = []
        labels = []
        for rec in batch_records:
            image = Image.open(rec.path).convert("RGB")
            images.append(TF.to_tensor(TF.resize(image, [image_size, image_size], antialias=True)))
            labels.append(float(rec.label))
        x = torch.stack(images, dim=0).to(device).requires_grad_(True)
        y = torch.tensor(labels, dtype=torch.float32, device=device)
        out = backbone.model.forward_features((x - mean) / std)
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
        adv = torch.clamp(x + sign * epsilon * x.grad.sign(), 0.0, 1.0).detach()
        with torch.no_grad():
            adv_out = backbone.model.forward_features((adv - mean) / std)
            patches.extend(adv_out["x_norm_patchtokens"].detach().cpu().numpy().astype(np.float32))
    n_patches = patches[0].shape[0] if patches else 0
    grid = int(n_patches**0.5)
    return FeatureBatch(np.stack(patches, axis=0), (grid, grid))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k1_seed0.yaml")
    parser.add_argument("--epsilons", nargs="+", default=["2/255", "4/255", "8/255"])
    parser.add_argument("--max-images", type=int, default=20)
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    args = parser.parse_args()

    config = load_config(args.config)
    dataset_cfg = config.get("dataset", {})
    experiment_cfg = config.get("experiment", {})
    backbone_cfg = config.get("backbone", {})
    model_cfg = dict(config.get("model", {}))
    model_cfg.setdefault("device", experiment_cfg.get("device", "cuda"))
    k = int(dataset_cfg.get("k_shots", [1])[0])
    seed = int(dataset_cfg.get("seeds", [0])[0])
    backbone_name = backbone_cfg.get("name", "dinov2_vits14")
    image_size = int(dataset_cfg.get("image_size", backbone_cfg.get("image_size", 518)))
    batch_size = int(backbone_cfg.get("batch_size", 4))
    cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")

    records = load_records(dataset_cfg.get("name", "mvtec"), dataset_cfg.get("root"), dataset_cfg.get("classes", "all"))
    support = few_shot_support(records, k=k, seed=seed)
    eval_recs = select_records(evaluation_records(records), args.max_images)
    labels = np.asarray([rec.label for rec in eval_recs], dtype=np.int64)

    backbone = build_backbone(backbone_name, device=experiment_cfg.get("device", "cuda"), image_size=image_size, batch_size=batch_size)
    support_cache_name = f"{dataset_cfg.get('name', 'dataset')}_support_{backbone_name}_k{k}_seed{seed}"
    support_batch = load_feature_cache_if_present(support, cache_dir, support_cache_name, seed, backbone_name, image_size)
    if support_batch is None:
        support_batch = encode_with_cache(backbone, support, cache_dir, support_cache_name, seed, backbone_name, image_size)
    clean_batch = backbone.encode_records(eval_recs, seed=seed)
    model = build_model(model_cfg.get("variant", "calib_subspace_head"), support_batch.patch_features, model_cfg, seed=seed)

    rows = []
    clean_scores, _ = model.score_images(clean_batch.patch_features)
    clean_metrics = summarize_binary(labels, clean_scores, clean_scores, bins=15)
    for label, name in [(0, "normal"), (1, "anomaly")]:
        mask = labels == label
        rows.append(
            {
                "config": args.config,
                "epsilon": "0",
                "direction": "clean",
                "label_group": name,
                "n": int(mask.sum()),
                "score_mean": float(clean_scores[mask].mean()),
                "score_delta_vs_clean": 0.0,
                "auroc": clean_metrics["auroc"],
                "ap": clean_metrics["ap"],
            }
        )

    for epsilon_text in args.epsilons:
        epsilon = parse_epsilon(epsilon_text)
        for direction in ["ascent", "descent"]:
            adv_batch = fgsm_features(backbone, eval_recs, model, epsilon, image_size, batch_size, direction)
            scores, _ = model.score_images(adv_batch.patch_features)
            metrics = summarize_binary(labels, scores, scores, bins=15)
            for label, name in [(0, "normal"), (1, "anomaly")]:
                mask = labels == label
                rows.append(
                    {
                        "config": args.config,
                        "epsilon": epsilon_text,
                        "direction": direction,
                        "label_group": name,
                        "n": int(mask.sum()),
                        "score_mean": float(scores[mask].mean()),
                        "score_delta_vs_clean": float(scores[mask].mean() - clean_scores[mask].mean()),
                        "auroc": metrics["auroc"],
                        "ap": metrics["ap"],
                    }
                )

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = Path(args.config).stem
    csv_path = out_dir / f"fgsm_objective_audit_{stem}.csv"
    with csv_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    (out_dir / f"fgsm_objective_audit_{stem}.json").write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(csv_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
