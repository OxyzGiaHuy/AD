from __future__ import annotations

import argparse
from dataclasses import replace
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.backbones.dinov2 import FeatureBatch, build_backbone
from src.calibration.platt import entropy_binary, reliability_bins
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import summarize_binary
from src.models.baselines import build_model
from src.robustness import corruptions as C
from src.run_experiment import _fit_calibrator, _fit_vector_calibrator, _records_hash, encode_with_cache
from src.utils.io import ensure_dir, write_json, write_table

CORRUPTION_FUNCS = {
    "gaussian_noise": lambda image, seed: C.gaussian_noise(image, severity=0.05, seed=seed),
    "blur": lambda image, seed: C.blur(image, kernel=3),
    "brightness_contrast": lambda image, seed: C.brightness_contrast(image, brightness=0.05, contrast=1.15),
    "jpeg": lambda image, seed: C.jpeg(image, quality=60),
}


def load_feature_cache_if_present(
    records,
    cache_dir: str | Path,
    cache_name: str,
    seed: int,
    backbone_name: str,
    image_size: int,
    cache_seed: int | None = None,
) -> FeatureBatch | None:
    key_seed = seed if cache_seed is None else cache_seed
    path = Path(cache_dir) / f"{cache_name}_{_records_hash(records, key_seed, backbone_name, image_size)}.npz"
    if not path.exists():
        return None
    try:
        data = np.load(path)
        grid = tuple(int(x) for x in data["grid_size"].tolist())
        return FeatureBatch(patch_features=data["patch_features"].astype(np.float32), grid_size=grid)
    except Exception:
        path.unlink(missing_ok=True)
        return None


def corrupt_records(records, corruption: str, out_dir: Path, seed: int, max_images: int | None = None):
    ensure_dir(out_dir)
    func = CORRUPTION_FUNCS[corruption]
    if max_images:
        normals = [rec for rec in records if rec.label == 0]
        anomalies = [rec for rec in records if rec.label == 1]
        half = max(1, max_images // 2)
        selected = normals[:half] + anomalies[: max_images - half]
    else:
        selected = records
    corrupted = []
    for idx, rec in enumerate(selected):
        image = Image.open(rec.path).convert("RGB")
        arr = np.asarray(image).astype(np.float32) / 255.0
        path = out_dir / rec.category / rec.defect_type / f"{Path(rec.path).stem}_{corruption}.png"
        ensure_dir(path.parent)
        needs_write = True
        if path.exists():
            try:
                with Image.open(path) as cached:
                    cached.verify()
                needs_write = False
            except Exception:
                path.unlink(missing_ok=True)
        if needs_write:
            out = func(arr, seed + idx)
            Image.fromarray((np.clip(out, 0.0, 1.0) * 255).astype(np.uint8)).save(path)
        corrupted.append(replace(rec, path=str(path)))
    return corrupted


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    parser.add_argument("--corruption", choices=sorted(CORRUPTION_FUNCS), required=True)
    parser.add_argument("--max-images", type=int, default=None)
    parser.add_argument("--tmp-root", default="/tmp/AD-corruptions")
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

    records = load_records(dataset_cfg.get("name", "mvtec"), dataset_cfg.get("root"), dataset_cfg.get("classes", "all"))
    support = few_shot_support(records, k=k, seed=seed)
    eval_clean = evaluation_records(records)
    class_key = "-".join(dataset_cfg.get("classes", ["all"])) if isinstance(dataset_cfg.get("classes", ["all"]), list) else str(dataset_cfg.get("classes", "all"))
    tmp_dir = Path(args.tmp_root) / dataset_cfg.get("name", "dataset") / class_key / f"seed{seed}" / args.corruption
    eval_corrupt = corrupt_records(eval_clean, args.corruption, tmp_dir, seed=seed, max_images=args.max_images)

    backbone_name = backbone_cfg.get("name", "identity_patch")
    image_size = int(dataset_cfg.get("image_size", backbone_cfg.get("image_size", 518)))
    cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")
    dataset_name = dataset_cfg.get("name", "dataset")
    support_cache_name = f"{dataset_name}_support_{backbone_name}_k{k}_seed{seed}"
    corrupt_cache_name = f"{dataset_name}_corrupt_{class_key}_{args.corruption}_{backbone_name}_seed{seed}"
    corrupt_cache_seed = 0 if backbone_name.startswith("dinov2") else seed
    support_batch = load_feature_cache_if_present(support, cache_dir, support_cache_name, seed, backbone_name, image_size)
    corrupt_batch = load_feature_cache_if_present(
        eval_corrupt,
        cache_dir,
        corrupt_cache_name,
        seed,
        backbone_name,
        image_size,
        cache_seed=corrupt_cache_seed,
    )
    if support_batch is None or corrupt_batch is None:
        backbone = build_backbone(
            backbone_name,
            device=experiment_cfg.get("device", "cuda"),
            image_size=image_size,
            batch_size=int(backbone_cfg.get("batch_size", 8)),
        )
        if support_batch is None:
            support_batch = encode_with_cache(backbone, support, cache_dir, support_cache_name, seed, backbone_name, image_size)
        if corrupt_batch is None:
            corrupt_batch = encode_with_cache(
                backbone,
                eval_corrupt,
                cache_dir,
                corrupt_cache_name,
                seed,
                backbone_name,
                image_size,
                cache_seed=corrupt_cache_seed,
            )
    support_features = support_batch.patch_features
    corrupt_features = corrupt_batch.patch_features

    model = build_model(model_cfg.get("variant", "head_pca"), support_features, model_cfg, seed=seed)
    support_scores, _ = model.score_images(support_features)
    raw_scores, patch_scores = model.score_images(corrupt_features)
    labels = np.asarray([r.label for r in eval_corrupt], dtype=np.int64)
    if hasattr(model, "calibration_features"):
        calibrator, _, corrupt_vec = _fit_vector_calibrator(
            calibration_mode,
            model,
            support_features,
            corrupt_features,
            labels,
            seed=seed,
            synthetic_ratio=float(model_cfg.get("synthetic_anomaly_ratio", 1.0)),
        )
        probs = calibrator.predict_proba(corrupt_vec)
    else:
        calibrator = _fit_calibrator(calibration_mode, support_scores, raw_scores, labels)
        probs = calibrator.predict_proba(raw_scores)
    entropy = entropy_binary(probs)
    metrics = summarize_binary(labels, raw_scores, probs, bins=int(config.get("calibration", {}).get("bins", 15)))
    metrics.update({"k_shot": k, "seed": seed, "corruption": args.corruption, "num_images": len(eval_corrupt)})

    run_name = f"{experiment_cfg.get('name', 'experiment')}_{model_cfg.get('variant', 'model')}_k{k}_seed{seed}_{args.corruption}"
    out_dir = Path(experiment_cfg.get("output_dir", "outputs")) / "robustness" / run_name
    ensure_dir(out_dir / "anomaly_maps")
    write_json(out_dir / "metrics.json", metrics)
    write_json(out_dir / "calibration_bins.json", {"bins": reliability_bins(labels, probs, bins=int(config.get("calibration", {}).get("bins", 15)))})
    rows = []
    for rec, score, prob, ent in zip(eval_corrupt, raw_scores, probs, entropy):
        rows.append(
            {
                "image_path": rec.path,
                "label": rec.label,
                "raw_score": float(score),
                "calibrated_probability": float(prob),
                "entropy": float(ent),
                "class": rec.category,
                "seed": seed,
                "corruption": args.corruption,
                "attack": "none",
            }
        )
    write_table(out_dir / "predictions", rows)
    np.save(out_dir / "anomaly_maps" / "patch_scores.npy", patch_scores.astype(np.float32))
    print(out_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
