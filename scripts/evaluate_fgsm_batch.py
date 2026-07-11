from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np

from scripts.evaluate_fgsm import _fgsm_features, _select_records
from src.backbones.dinov2 import build_backbone
from src.calibration.platt import entropy_binary, reliability_bins
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import summarize_binary
from src.models.baselines import build_model
from src.robustness.attacks import parse_epsilon
from src.run_experiment import _fit_calibrator, _fit_vector_calibrator, encode_with_cache, load_feature_cache_if_present
from src.utils.io import ensure_dir, write_json, write_table


def run_config(config_path: Path, backbone, epsilon_text: str, max_images: int | None, force: bool = False) -> bool:
    config = load_config(config_path)
    dataset_cfg = config.get("dataset", {})
    experiment_cfg = config.get("experiment", {})
    backbone_cfg = config.get("backbone", {})
    model_cfg = dict(config.get("model", {}))
    model_cfg.setdefault("device", experiment_cfg.get("device", "cuda"))
    k = int(dataset_cfg.get("k_shots", [1])[0])
    seed = int(dataset_cfg.get("seeds", [0])[0])
    calibration_mode = config.get("calibration", {}).get("modes", ["normal_synthetic"])[0]
    epsilon = parse_epsilon(epsilon_text)
    eps_tag = epsilon_text.replace("/", "_").replace(".", "p")
    run_name = f"{experiment_cfg.get('name', 'experiment')}_{model_cfg.get('variant', 'model')}_k{k}_seed{seed}_fgsm_eps{eps_tag}"
    out_dir = Path(experiment_cfg.get("output_dir", "outputs")) / "robustness" / run_name
    metrics_path = out_dir / "metrics.json"
    if metrics_path.exists() and not force:
        try:
            metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
            if int(metrics.get("num_images", 0)) > 20:
                return False
        except Exception:
            pass

    records = load_records(dataset_cfg.get("name", "mvtec"), dataset_cfg.get("root"), dataset_cfg.get("classes", "all"))
    support = few_shot_support(records, k=k, seed=seed)
    eval_clean = _select_records(evaluation_records(records), max_images)
    labels = np.asarray([r.label for r in eval_clean], dtype=np.int64)
    backbone_name = backbone_cfg.get("name", "dinov2_vits14")
    image_size = int(dataset_cfg.get("image_size", backbone_cfg.get("image_size", 518)))
    cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")
    dataset_name = dataset_cfg.get("name", "dataset")
    support_cache_name = f"{dataset_name}_support_{backbone_name}_k{k}_seed{seed}"
    support_batch = load_feature_cache_if_present(support, cache_dir, support_cache_name, seed, backbone_name, image_size)
    if support_batch is None:
        support_batch = encode_with_cache(backbone, support, cache_dir, support_cache_name, seed, backbone_name, image_size)
    support_features = support_batch.patch_features
    model = build_model(model_cfg.get("variant", "calib_subspace_head"), support_features, model_cfg, seed=seed)
    support_scores, _ = model.score_images(support_features)
    adv_batch = _fgsm_features(
        backbone,
        eval_clean,
        model,
        epsilon=epsilon,
        image_size=image_size,
        batch_size=int(backbone_cfg.get("batch_size", 4)),
    )
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
    metrics.update({"k_shot": k, "seed": seed, "attack": "fgsm_image_pca_surrogate", "epsilon": epsilon_text, "epsilon_float": epsilon, "num_images": len(eval_clean)})

    ensure_dir(out_dir / "anomaly_maps")
    write_json(metrics_path, metrics)
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
                "epsilon": epsilon_text,
            }
        )
    write_table(out_dir / "predictions", rows)
    np.save(out_dir / "anomaly_maps" / "patch_scores.npy", patch_scores.astype(np.float32))
    print(out_dir, flush=True)
    return True


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--run-list", required=True)
    parser.add_argument("--variant", default="calib_subspace_head")
    parser.add_argument("--epsilon", default="8/255")
    parser.add_argument("--max-images", type=int, default=None)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    config_paths = [Path(line.strip()) for line in Path(args.run_list).read_text(encoding="utf-8").splitlines() if line.strip() and Path(line.strip()).name.startswith(f"{args.variant}_")]
    if not config_paths:
        print("No configs selected")
        return 1
    first = load_config(config_paths[0])
    first_dataset = first.get("dataset", {})
    first_backbone = first.get("backbone", {})
    first_experiment = first.get("experiment", {})
    backbone = build_backbone(
        first_backbone.get("name", "dinov2_vits14"),
        device=first_experiment.get("device", "cuda"),
        image_size=int(first_dataset.get("image_size", first_backbone.get("image_size", 518))),
        batch_size=int(first_backbone.get("batch_size", 4)),
    )
    completed = 0
    skipped = 0
    for config_path in config_paths:
        ran = run_config(config_path, backbone, args.epsilon, args.max_images, force=args.force)
        if ran:
            completed += 1
        else:
            skipped += 1
        if completed and completed % 10 == 0:
            print(f"fgsm_batch_completed={completed} skipped={skipped}", flush=True)
    print(f"fgsm_batch_done completed={completed} skipped={skipped}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
