from __future__ import annotations

import argparse
import csv
import time
from collections import defaultdict
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluate_transfer import get_patch_features
from scripts.generate_benchmark_grid import VISA_CLASSES
from src.calibration.platt import VectorPlattScaler, entropy_binary
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support, split_calibration
from src.evaluation.metrics import summarize_binary
from src.models.baselines import build_model
from src.run_experiment import run_once


REP_CLASSES = ["candle", "cashew", "pcb1"]
REP_K = [1, 4, 8]
REP_SEEDS = [0, 1, 2]


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def read_existing(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def summarize(rows: list[dict], group_keys: list[str], metrics: list[str]) -> list[dict]:
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for row in rows:
        key_parts = []
        for k in group_keys:
            value = row[k]
            if k in {"k_shot", "pca_components", "seed"}:
                value = int(value)
            key_parts.append(value)
        groups[tuple(key_parts)].append(row)
    out = []
    for key, group in sorted(groups.items(), key=lambda item: tuple(str(v) for v in item[0])):
        item = {k: v for k, v in zip(group_keys, key)}
        item["n"] = len(group)
        for metric in metrics:
            vals = [float(r[metric]) for r in group if metric in r and np.isfinite(float(r[metric]))]
            item[f"{metric}_mean"] = float(np.mean(vals)) if vals else float("nan")
            item[f"{metric}_std"] = float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.0
        out.append(item)
    return out


def visa_pca128(base_config: dict, out_dir: Path, resume: bool, classes: list[str], k_shots: list[int], seeds: list[int], run_tag: str = "representative") -> None:
    detail = out_dir / f"visa_pca128_{run_tag}_detailed.csv"
    rows = read_existing(detail) if resume else []
    done = {(r["class"], int(r["k_shot"]), int(r["seed"])) for r in rows}
    total = len(classes) * len(k_shots) * len(seeds)
    for cls in classes:
        for k in k_shots:
            for seed in seeds:
                if (cls, k, seed) in done:
                    continue
                cfg = dict(base_config)
                cfg["experiment"] = {**base_config.get("experiment", {}), "name": f"p2_visa_pca128_{cls}_k{k}_seed{seed}", "output_dir": "outputs/p2_visa_pca128"}
                cfg["dataset"] = {**base_config.get("dataset", {}), "name": "visa", "root": "data/visa", "classes": [cls], "k_shots": [k], "seeds": [seed]}
                cfg["model"] = {**base_config.get("model", {}), "variant": "calib_subspace_head", "pca_components": 128}
                result = run_once(cfg, k=k, seed=seed, calibration_mode="normal_synthetic")
                rows.append({"dataset": "visa", "class": cls, "k_shot": k, "seed": seed, "pca_components": 128, **result})
                write_csv(detail, rows)
                write_csv(out_dir / f"visa_pca128_{run_tag}_summary.csv", summarize(rows, ["dataset", "pca_components", "k_shot"], ["auroc", "ap", "ece", "brier", "nll", "model_storage_mb", "latency_sec_per_image"]))
                print(f"visa_pca128_progress={len(rows)}/{total} class={cls} k={k} seed={seed}", flush=True)


def no_cache_runtime(base_config: dict, out_dir: Path, resume: bool) -> None:
    detail = out_dir / "runtime_no_cache_representative_detailed.csv"
    rows = read_existing(detail) if resume else []
    done = {(r["dataset"], r["class"], int(r["k_shot"]), int(r["seed"])) for r in rows}
    cases = [("mvtec", "bottle"), ("mvtec", "cable"), ("visa", "candle")]
    for dataset, cls in cases:
        for k in [1, 8]:
            for seed in [0]:
                if (dataset, cls, k, seed) in done:
                    continue
                cfg = dict(base_config)
                cfg["experiment"] = {**base_config.get("experiment", {}), "name": f"p2_no_cache_{dataset}_{cls}_k{k}_seed{seed}", "output_dir": "outputs/p2_runtime_no_cache"}
                cfg["dataset"] = {**base_config.get("dataset", {}), "name": dataset, "root": f"data/{dataset}", "classes": [cls], "k_shots": [k], "seeds": [seed]}
                cfg["backbone"] = {**base_config.get("backbone", {}), "cache_dir": f"outputs/p2_runtime_no_cache/feature_cache_{dataset}_{cls}_k{k}_seed{seed}_{int(time.time())}"}
                cfg["model"] = {**base_config.get("model", {}), "variant": "calib_subspace_head"}
                start = time.perf_counter()
                result = run_once(cfg, k=k, seed=seed, calibration_mode="normal_synthetic")
                wall = time.perf_counter() - start
                rows.append({
                    "dataset": dataset,
                    "class": cls,
                    "k_shot": k,
                    "seed": seed,
                    "wall_time_sec": wall,
                    "wall_time_sec_per_eval_image": wall / max(float(result.get("eval_image_count", 1) or 1), 1.0),
                    **result,
                })
                write_csv(detail, rows)
                write_csv(out_dir / "runtime_no_cache_representative_summary.csv", summarize(rows, ["dataset", "k_shot"], ["wall_time_sec", "latency_sec_per_image", "model_storage_mb", "auroc", "ece"]))
                print(f"runtime_no_cache_progress={len(rows)}/{len(cases)*2} dataset={dataset} class={cls} k={k}", flush=True)


def shift_features(model, features: np.ndarray, support_features: np.ndarray) -> np.ndarray:
    base = model.calibration_features(features)
    support_flat = support_features.reshape(-1, support_features.shape[-1])
    center = support_flat.mean(axis=0, keepdims=True)
    support_norm = np.linalg.norm(support_flat - center, axis=1)
    norm_scale = float(np.percentile(support_norm, 95) + 1e-6)
    centered = features - center.reshape(1, 1, -1)
    norms = np.linalg.norm(centered, axis=2)
    norm_max = (norms.max(axis=1) / norm_scale)[:, None]
    norm_mean = (norms.mean(axis=1) / norm_scale)[:, None]
    pca_patch = model.pca.residual_scores(features)
    pca_mean = pca_patch.mean(axis=1, keepdims=True)
    pca_std = pca_patch.std(axis=1, keepdims=True)
    pca_max = pca_patch.max(axis=1, keepdims=True)
    pca_concentration = pca_max / (pca_mean + 1e-6)
    return np.concatenate([base, norm_max, norm_mean, pca_mean, pca_std, pca_concentration], axis=1).astype(np.float32)


def shift_synthetic_features(model, support_features: np.ndarray, seed: int, ratio: float) -> np.ndarray:
    synth = model._make_synthetic_feature_batch(support_features, seed=seed, ratio=ratio)
    return shift_features(model, synth, support_features)


def shift_aware_calibration(base_config: dict, out_dir: Path, resume: bool, visa_classes: list[str], mvtec_classes: list[str], k_shots: list[int], seeds: list[int], run_tag: str = "representative") -> None:
    detail = out_dir / f"shift_aware_calibration_{run_tag}_detailed.csv"
    rows = read_existing(detail) if resume else []
    done = {(r["dataset"], r["class"], int(r["k_shot"]), int(r["seed"]), r["method"]) for r in rows}
    cases = [("visa", cls) for cls in visa_classes] + [("mvtec", cls) for cls in mvtec_classes]
    for dataset, cls in cases:
        for k in k_shots:
            for seed in seeds:
                if all((dataset, cls, k, seed, method) in done for method in ["vector_platt", "shift_aware_vector_platt"]):
                    continue
                cfg = dict(base_config)
                cfg["dataset"] = {**base_config.get("dataset", {}), "name": dataset, "root": f"data/{dataset}", "classes": [cls]}
                cfg["model"] = {**base_config.get("model", {}), "variant": "calib_subspace_head"}
                model_cfg = {**cfg.get("model", {}), "device": cfg.get("experiment", {}).get("device", "cuda")}
                records = load_records(dataset, f"data/{dataset}", [cls])
                support = few_shot_support(records, k=k, seed=seed)
                eval_recs = evaluation_records(records)
                backbone_name = cfg.get("backbone", {}).get("name", "dinov2_vits14")
                support_features = get_patch_features(cfg, support, f"p2_shift_support_{dataset}_{cls}_{backbone_name}_k{k}_seed{seed}", seed)
                eval_features = get_patch_features(cfg, eval_recs, f"p2_shift_eval_{dataset}_{cls}_{backbone_name}", seed, cache_seed=0)
                model = build_model("calib_subspace_head", support_features, model_cfg, seed=seed)
                raw_scores, _ = model.score_images(eval_features)
                labels = np.asarray([r.label for r in eval_recs], dtype=np.int64)
                for method in ["vector_platt", "shift_aware_vector_platt"]:
                    if (dataset, cls, k, seed, method) in done:
                        continue
                    if method == "vector_platt":
                        support_x = model.calibration_features(support_features)
                        synth_x = model.synthetic_calibration_features(support_features, seed=seed, ratio=float(model_cfg.get("synthetic_anomaly_ratio", 1.0)))
                        eval_x = model.calibration_features(eval_features)
                    else:
                        support_x = shift_features(model, support_features, support_features)
                        synth_x = shift_synthetic_features(model, support_features, seed=seed, ratio=float(model_cfg.get("synthetic_anomaly_ratio", 1.0)))
                        eval_x = shift_features(model, eval_features, support_features)
                    train_x = np.concatenate([support_x, synth_x], axis=0)
                    train_y = np.concatenate([np.zeros(len(support_x), dtype=np.float32), np.ones(len(synth_x), dtype=np.float32)])
                    calibrator = VectorPlattScaler().fit(train_x, train_y, positive_indices=(0,))
                    probs = calibrator.predict_proba(eval_x)
                    metrics = summarize_binary(labels, raw_scores, probs, bins=int(cfg.get("calibration", {}).get("bins", 15)))
                    rows.append({
                        "dataset": dataset,
                        "class": cls,
                        "k_shot": k,
                        "seed": seed,
                        "method": method,
                        "entropy_mean": float(entropy_binary(probs).mean()),
                        "feature_dim": eval_x.shape[1],
                        **metrics,
                    })
                    done.add((dataset, cls, k, seed, method))
                write_csv(detail, rows)
                write_csv(out_dir / f"shift_aware_calibration_{run_tag}_summary.csv", summarize(rows, ["dataset", "method", "k_shot"], ["auroc", "ap", "ece", "brier", "nll", "entropy_mean"]))
                print(f"shift_aware_progress={len(rows)} dataset={dataset} class={cls} k={k} seed={seed}", flush=True)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k1_seed0.yaml")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--tasks", nargs="*", default=["visa_pca128", "runtime_no_cache", "shift_aware"])
    parser.add_argument("--visa-classes", nargs="*", default=REP_CLASSES)
    parser.add_argument("--mvtec-classes", nargs="*", default=["bottle", "cable"])
    parser.add_argument("--k-shots", nargs="*", type=int, default=REP_K)
    parser.add_argument("--seeds", nargs="*", type=int, default=REP_SEEDS)
    parser.add_argument("--run-tag", default="representative")
    args = parser.parse_args()
    base = load_config(args.base_config)
    out_dir = Path(args.out_dir)
    if "visa_pca128" in args.tasks:
        visa_pca128(base, out_dir, args.resume, args.visa_classes, args.k_shots, args.seeds, args.run_tag)
    if "runtime_no_cache" in args.tasks:
        no_cache_runtime(base, out_dir, args.resume)
    if "shift_aware" in args.tasks:
        shift_aware_calibration(base, out_dir, args.resume, args.visa_classes, args.mvtec_classes, args.k_shots, args.seeds, args.run_tag)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
