from __future__ import annotations

import argparse
import hashlib
import sys
import time
from pathlib import Path

import numpy as np

from .backbones.dinov2 import FeatureBatch, build_backbone
from .calibration.platt import PlattScaler, VectorPlattScaler, entropy_binary, reliability_bins
from .config import load_config
from .data.datasets import load_records
from .data.sampling import evaluation_records, few_shot_support, split_calibration
from .evaluation.metrics import summarize_binary
from .models.baselines import build_model
from .utils.docs import append_markdown, write_run_note
from .utils.io import ensure_dir, write_json, write_table


def _records_hash(records: list, seed: int, backbone_name: str, image_size: int) -> str:
    h = hashlib.sha256()
    h.update(f"seed={seed}|backbone={backbone_name}|image_size={image_size}".encode("utf-8"))
    for rec in records:
        h.update(f"{rec.path}|{rec.label}|{rec.split}|{rec.category}|{rec.mask_path}\n".encode("utf-8"))
    return h.hexdigest()[:16]


def encode_with_cache(
    backbone,
    records: list,
    cache_dir: str | Path,
    cache_name: str,
    seed: int,
    backbone_name: str,
    image_size: int,
    cache_seed: int | None = None,
) -> FeatureBatch:
    cache_dir = ensure_dir(cache_dir)
    key_seed = seed if cache_seed is None else cache_seed
    key = _records_hash(records, seed=key_seed, backbone_name=backbone_name, image_size=image_size)
    path = cache_dir / f"{cache_name}_{key}.npz"
    if path.exists():
        try:
            data = np.load(path)
            grid = tuple(int(x) for x in data["grid_size"].tolist())
            return FeatureBatch(patch_features=data["patch_features"].astype(np.float32), grid_size=grid)
        except Exception:
            path.unlink(missing_ok=True)
    batch = backbone.encode_records(records, seed=seed)
    np.savez_compressed(path, patch_features=batch.patch_features.astype(np.float32), grid_size=np.asarray(batch.grid_size))
    return batch


def load_feature_cache_if_present(
    records: list,
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


def _run_id(config: dict, k: int, seed: int, mode: str) -> str:
    name = config.get("experiment", {}).get("name", "experiment")
    variant = config.get("model", {}).get("variant", "model")
    return f"{name}_{variant}_k{k}_seed{seed}_{mode}"


def _fit_calibrator(
    mode: str,
    support_scores: np.ndarray,
    eval_scores: np.ndarray,
    eval_labels: np.ndarray,
    calib_scores: np.ndarray | None = None,
    calib_labels: np.ndarray | None = None,
) -> PlattScaler:
    if mode == "normal_synthetic":
        normal = support_scores
        synthetic = support_scores + max(float(np.std(support_scores)), 1e-3) + 1e-3
        scores = np.concatenate([normal, synthetic])
        labels = np.concatenate([np.zeros_like(normal), np.ones_like(synthetic)])
    elif mode == "normal_plus_anomaly_val":
        if calib_scores is None or calib_labels is None:
            raise ValueError("normal_plus_anomaly_val requires held-out calibration scores and labels.")
        pos = calib_scores[calib_labels == 1]
        if len(pos) == 0:
            raise ValueError("normal_plus_anomaly_val requires at least one anomaly calibration example.")
        scores = np.concatenate([support_scores, pos])
        labels = np.concatenate([np.zeros_like(support_scores), np.ones_like(pos)])
    else:
        raise ValueError(f"Unsupported calibration mode: {mode}")
    return PlattScaler().fit(scores, labels)


def _fit_vector_calibrator(
    mode: str,
    model,
    support_features: np.ndarray,
    eval_features: np.ndarray,
    eval_labels: np.ndarray,
    seed: int,
    synthetic_ratio: float,
    calib_features: np.ndarray | None = None,
    calib_labels: np.ndarray | None = None,
) -> tuple[VectorPlattScaler, np.ndarray, np.ndarray]:
    support_vec = model.calibration_features(support_features)
    eval_vec = model.calibration_features(eval_features)
    if mode == "normal_synthetic":
        synth_vec = model.synthetic_calibration_features(support_features, seed=seed, ratio=synthetic_ratio)
        train_x = np.concatenate([support_vec, synth_vec], axis=0)
        train_y = np.concatenate([np.zeros(len(support_vec), dtype=np.float32), np.ones(len(synth_vec), dtype=np.float32)])
    elif mode == "normal_plus_anomaly_val":
        if calib_features is None or calib_labels is None:
            raise ValueError("normal_plus_anomaly_val requires held-out calibration features and labels.")
        calib_vec = model.calibration_features(calib_features)
        pos = calib_vec[calib_labels == 1]
        if len(pos) == 0:
            raise ValueError("normal_plus_anomaly_val requires at least one anomaly calibration example.")
        train_x = np.concatenate([support_vec, pos], axis=0)
        train_y = np.concatenate([np.zeros(len(support_vec), dtype=np.float32), np.ones(len(pos), dtype=np.float32)])
    else:
        raise ValueError(f"Unsupported calibration mode: {mode}")
    return VectorPlattScaler().fit(train_x, train_y, positive_indices=(0,)), support_vec, eval_vec


def run_once(config: dict, k: int, seed: int, calibration_mode: str) -> dict:
    dataset_cfg = config.get("dataset", {})
    experiment_cfg = config.get("experiment", {})
    model_cfg = config.get("model", {})
    backbone_cfg = config.get("backbone", {})
    classes = dataset_cfg.get("classes", "all")
    records = load_records(
        dataset_cfg.get("name", "mvtec"),
        dataset_cfg.get("root"),
        classes,
        synthetic_count=int(dataset_cfg.get("synthetic_count", 12)),
    )
    support = few_shot_support(records, k=k, seed=seed)
    eval_records = evaluation_records(records)
    calib_records = []
    if calibration_mode == "normal_plus_anomaly_val":
        calib_records, eval_records = split_calibration(records, seed=seed)

    backbone_name = backbone_cfg.get("name", "identity_patch")
    image_size = int(dataset_cfg.get("image_size", backbone_cfg.get("image_size", 518)))
    cache_dir = backbone_cfg.get("cache_dir", "outputs/feature_cache")
    dataset_name = dataset_cfg.get("name", "dataset")
    support_cache_name = f"{dataset_name}_support_{backbone_name}_k{k}_seed{seed}"
    eval_cache_name = f"{dataset_name}_eval_{backbone_name}"
    eval_cache_seed = 0 if backbone_name.startswith("dinov2") else seed
    calib_cache_name = f"{dataset_name}_calib_{backbone_name}_seed{seed}"

    support_batch = load_feature_cache_if_present(support, cache_dir, support_cache_name, seed, backbone_name, image_size)
    eval_batch = load_feature_cache_if_present(eval_records, cache_dir, eval_cache_name, seed, backbone_name, image_size, cache_seed=eval_cache_seed)
    calib_batch = None
    if calib_records:
        calib_batch = load_feature_cache_if_present(calib_records, cache_dir, calib_cache_name, seed, backbone_name, image_size)

    if support_batch is None or eval_batch is None or (calib_records and calib_batch is None):
        backbone = build_backbone(
            backbone_name,
            device=experiment_cfg.get("device", "cuda"),
            image_size=image_size,
            batch_size=int(backbone_cfg.get("batch_size", 8)),
        )
        if support_batch is None:
            support_batch = encode_with_cache(backbone, support, cache_dir, support_cache_name, seed, backbone_name, image_size)
        if eval_batch is None:
            eval_batch = encode_with_cache(backbone, eval_records, cache_dir, eval_cache_name, seed, backbone_name, image_size, cache_seed=eval_cache_seed)
        if calib_records and calib_batch is None:
            calib_batch = encode_with_cache(backbone, calib_records, cache_dir, calib_cache_name, seed, backbone_name, image_size)
    support_features = support_batch.patch_features
    eval_features = eval_batch.patch_features
    calib_features = calib_batch.patch_features if calib_batch is not None else None

    model_cfg = dict(model_cfg)
    model_cfg.setdefault("device", experiment_cfg.get("device", "cuda"))
    model = build_model(model_cfg.get("variant", "head_pca"), support_features, model_cfg, seed=seed)
    support_scores, _ = model.score_images(support_features)
    start = time.perf_counter()
    raw_scores, patch_scores = model.score_images(eval_features)
    latency = (time.perf_counter() - start) / max(len(eval_records), 1)
    labels = np.asarray([r.label for r in eval_records], dtype=np.int64)
    calib_labels = np.asarray([r.label for r in calib_records], dtype=np.int64) if calib_records else None

    calibration_feature_names: list[str] = []
    eval_calibration_features = None
    if hasattr(model, "calibration_features"):
        calibrator, _, eval_calibration_features = _fit_vector_calibrator(
            calibration_mode,
            model,
            support_features,
            eval_features,
            labels,
            seed=seed,
            synthetic_ratio=float(model_cfg.get("synthetic_anomaly_ratio", 1.0)),
            calib_features=calib_features,
            calib_labels=calib_labels,
        )
        probs = calibrator.predict_proba(eval_calibration_features)
        calibration_feature_names = ["pca_score", "head_score", "z_disagreement"]
    else:
        calib_scores = None
        if calib_features is not None:
            calib_scores, _ = model.score_images(calib_features)
        calibrator = _fit_calibrator(calibration_mode, support_scores, raw_scores, labels, calib_scores=calib_scores, calib_labels=calib_labels)
        probs = calibrator.predict_proba(raw_scores)
    entropy = entropy_binary(probs)
    metrics = summarize_binary(labels, raw_scores, probs, bins=int(config.get("calibration", {}).get("bins", 15)))
    metrics.update(
        {
            "latency_sec_per_image": float(latency),
            "model_storage_mb": float(model.storage_bytes() / (1024 * 1024)) if hasattr(model, "storage_bytes") else float("nan"),
            "support_patch_count": int(np.prod(support_features.shape[:2])),
            "peak_memory_mb": float("nan"),
            "pixel_auroc": float("nan"),
            "pro": float("nan"),
            "k_shot": k,
            "seed": seed,
            "calibration_anomaly_val_count": int(np.sum(calib_labels == 1)) if calib_labels is not None else 0,
        }
    )

    run_id = _run_id(config, k, seed, calibration_mode)
    out_dir = Path(experiment_cfg.get("output_dir", "outputs")) / run_id
    ensure_dir(out_dir / "anomaly_maps")
    write_json(out_dir / "metrics.json", metrics)
    write_json(out_dir / "calibration_bins.json", {"bins": reliability_bins(labels, probs, bins=int(config.get("calibration", {}).get("bins", 15)))})
    rows = []
    for idx, (rec, score, prob, ent) in enumerate(zip(eval_records, raw_scores, probs, entropy)):
        row = {
            "image_path": rec.path,
            "label": rec.label,
            "raw_score": float(score),
            "calibrated_probability": float(prob),
            "entropy": float(ent),
            "calibration_mode": calibration_mode,
            "class": rec.category,
            "seed": seed,
            "corruption": "clean",
            "attack": "none",
        }
        if eval_calibration_features is not None:
            for feature_name, feature_value in zip(calibration_feature_names, eval_calibration_features[idx]):
                row[f"calibrator_{feature_name}"] = float(feature_value)
        rows.append(row)
    table_path = write_table(out_dir / "predictions", rows)
    np.save(out_dir / "anomaly_maps" / "patch_scores.npy", patch_scores.astype(np.float32))
    write_run_note(
        experiment_cfg.get("docs_dir", "docs"),
        run_id,
        config,
        metrics,
        command=" ".join(sys.argv),
        notes=[f"Predictions written to {table_path}", "Patch heatmap tensor saved as patch_scores.npy"],
    )
    append_markdown(
        Path(experiment_cfg.get("docs_dir", "docs")) / "experiment_findings.md",
        f"Completed {run_id}",
        [f"- AUROC: `{metrics['auroc']}`", f"- ECE: `{metrics['ece']}`", f"- Output dir: `{out_dir}`"],
    )
    return metrics


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True)
    args = parser.parse_args(argv)
    config = load_config(args.config)
    all_metrics = []
    for k in config.get("dataset", {}).get("k_shots", [1]):
        for seed in config.get("dataset", {}).get("seeds", [0]):
            for mode in config.get("calibration", {}).get("modes", ["normal_synthetic"]):
                all_metrics.append(run_once(config, int(k), int(seed), str(mode)))
    print(f"Completed {len(all_metrics)} runs")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

