from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluate_transfer import fit_source_calibrator, get_patch_features
from scripts.generate_benchmark_grid import VISA_CLASSES
from src.calibration.platt import VectorPlattScaler, entropy_binary
from src.config import load_config
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support, split_calibration
from src.evaluation.metrics import summarize_binary
from src.models.baselines import build_model


def fit_target_calibrator(model, support_features: np.ndarray, mode: str, seed: int, synthetic_ratio: float, calib_features: np.ndarray | None, calib_labels: np.ndarray | None) -> VectorPlattScaler:
    support_vec = model.calibration_features(support_features)
    if mode == "visa_normal_synthetic":
        synth_vec = model.synthetic_calibration_features(support_features, seed=seed, ratio=synthetic_ratio)
        x = np.concatenate([support_vec, synth_vec], axis=0)
        y = np.concatenate([np.zeros(len(support_vec), dtype=np.float32), np.ones(len(synth_vec), dtype=np.float32)])
    elif mode == "visa_anomaly_val_upper_bound":
        if calib_features is None or calib_labels is None:
            raise ValueError("upper-bound mode requires calibration features and labels")
        calib_vec = model.calibration_features(calib_features)
        pos = calib_vec[calib_labels == 1]
        if len(pos) == 0:
            raise ValueError("upper-bound mode requires anomaly validation examples")
        x = np.concatenate([support_vec, pos], axis=0)
        y = np.concatenate([np.zeros(len(support_vec), dtype=np.float32), np.ones(len(pos), dtype=np.float32)])
    else:
        raise ValueError(mode)
    return VectorPlattScaler().fit(x, y, positive_indices=(0,))


def eval_one(base_config: dict, cls: str, k: int, seed: int, mode: str, source_calibrator: VectorPlattScaler | None) -> dict:
    cfg = dict(base_config)
    cfg["dataset"] = {**base_config.get("dataset", {}), "name": "visa", "root": "data/visa", "classes": [cls]}
    cfg["model"] = {**base_config.get("model", {}), "variant": "calib_subspace_head"}
    model_cfg = {**cfg.get("model", {}), "device": cfg.get("experiment", {}).get("device", "cuda")}
    records = load_records("visa", "data/visa", [cls])
    support = few_shot_support(records, k=k, seed=seed)
    if mode == "visa_anomaly_val_upper_bound":
        calib_recs, eval_recs = split_calibration(records, seed=seed)
    else:
        calib_recs, eval_recs = [], evaluation_records(records)

    backbone_name = cfg.get("backbone", {}).get("name", "dinov2_vits14")
    support_features = get_patch_features(cfg, support, f"visa_calib_ablation_support_{cls}_{backbone_name}_k{k}_seed{seed}", seed)
    eval_features = get_patch_features(cfg, eval_recs, f"visa_calib_ablation_eval_{cls}_{backbone_name}", seed, cache_seed=0)
    calib_features = None
    calib_labels = None
    if calib_recs:
        calib_features = get_patch_features(cfg, calib_recs, f"visa_calib_ablation_calib_{cls}_{backbone_name}_seed{seed}", seed)
        calib_labels = np.asarray([r.label for r in calib_recs], dtype=np.int64)

    model = build_model("calib_subspace_head", support_features, model_cfg, seed=seed)
    raw_scores, _ = model.score_images(eval_features)
    labels = np.asarray([r.label for r in eval_recs], dtype=np.int64)
    if mode == "mvtec_transfer_normal_synthetic":
        if source_calibrator is None:
            raise ValueError("source calibrator required")
        calibrator = source_calibrator
    else:
        calibrator = fit_target_calibrator(
            model,
            support_features,
            mode,
            seed=seed,
            synthetic_ratio=float(model_cfg.get("synthetic_anomaly_ratio", 1.0)),
            calib_features=calib_features,
            calib_labels=calib_labels,
        )
    probs = calibrator.predict_proba(model.calibration_features(eval_features))
    metrics = summarize_binary(labels, raw_scores, probs, bins=int(cfg.get("calibration", {}).get("bins", 15)))
    return {
        "dataset": "visa",
        "class": cls,
        "k_shot": k,
        "seed": seed,
        "calibration_mode": mode,
        "calibration_anomaly_val_count": int(np.sum(calib_labels == 1)) if calib_labels is not None else 0,
        "entropy_mean": float(entropy_binary(probs).mean()),
        **metrics,
    }


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


def summarize(rows: list[dict]) -> list[dict]:
    groups = defaultdict(list)
    for row in rows:
        groups[(row["dataset"], row["calibration_mode"], int(row["k_shot"]))].append(row)
    out = []
    for (dataset, mode, k), group in sorted(groups.items()):
        item = {"dataset": dataset, "calibration_mode": mode, "k_shot": k, "n": len(group)}
        for metric in ["auroc", "ap", "max_f1", "ece", "brier", "nll", "entropy_mean", "calibration_anomaly_val_count"]:
            vals = [float(r[metric]) for r in group if np.isfinite(float(r[metric]))]
            item[f"{metric}_mean"] = float(np.mean(vals)) if vals else float("nan")
            item[f"{metric}_std"] = float(np.std(vals, ddof=1)) if len(vals) > 1 else 0.0
        out.append(item)
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/mvtec_full/calib_subspace_head_mvtec_bottle_k1_seed0.yaml")
    parser.add_argument("--k-shots", nargs="*", type=int, default=[1, 2, 4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2, 3, 4])
    parser.add_argument("--classes", nargs="*", default=VISA_CLASSES)
    parser.add_argument("--modes", nargs="*", default=["mvtec_transfer_normal_synthetic", "visa_normal_synthetic", "visa_anomaly_val_upper_bound"])
    parser.add_argument("--source-max-classes", type=int, default=None)
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    base = load_config(args.base_config)
    out = Path(args.out_dir)
    detail_path = out / "transfer_calibration_ablation_detailed.csv"
    rows = read_existing(detail_path) if args.resume else []
    done = {(r["class"], int(r["k_shot"]), int(r["seed"]), r["calibration_mode"]) for r in rows}
    total = len(args.classes) * len(args.k_shots) * len(args.seeds) * len(args.modes)
    count = len(rows)
    for k in args.k_shots:
        for seed in args.seeds:
            source_calibrator = None
            if "mvtec_transfer_normal_synthetic" in args.modes:
                source_calibrator = fit_source_calibrator(base, k, seed, max_classes=args.source_max_classes)
            for cls in args.classes:
                for mode in args.modes:
                    key = (cls, k, seed, mode)
                    if key in done:
                        continue
                    rows.append(eval_one(base, cls, k, seed, mode, source_calibrator))
                    done.add(key)
                    count += 1
                    write_csv(detail_path, rows)
                    write_csv(out / "transfer_calibration_ablation_summary.csv", summarize(rows))
                    print(f"transfer_calib_ablation_progress={count}/{total} k={k} seed={seed} class={cls} mode={mode}", flush=True)
                    if args.limit and count >= args.limit:
                        return 0
    print(f"runs={len(rows)}")
    print(out / "transfer_calibration_ablation_summary.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
