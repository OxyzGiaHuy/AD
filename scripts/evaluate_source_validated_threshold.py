from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.evaluate_source_conditioned_routing import conformalize


def conservative_threshold(normal_p_values: np.ndarray, alpha: float) -> float:
    values = np.sort(np.asarray(normal_p_values, dtype=np.float64))
    if len(values) == 0:
        return 0.0
    unique = np.unique(values)
    valid = [threshold for threshold in unique if np.mean(values <= threshold) <= alpha]
    return float(max(valid)) if valid else 0.0


def source_validated_threshold(source: pd.DataFrame, score_col: str, alpha: float) -> tuple[float, float, int]:
    p_values = []
    for held_out, target in source.groupby("class"):
        reference = source[source["class"] != held_out]
        if reference.empty:
            continue
        p_values.extend(conformalize(reference[score_col].to_numpy(), target[score_col].to_numpy()).tolist())
    values = np.asarray(p_values, dtype=np.float64)
    threshold = conservative_threshold(values, alpha)
    validation_far = float(np.mean(values <= threshold)) if len(values) else float("nan")
    return threshold, validation_far, len(values)


def evaluate_target_only(frame: pd.DataFrame, residuals: pd.DataFrame, alphas: list[float]) -> pd.DataFrame:
    rows = []
    keys = ["dataset", "class", "k_shot", "seed", "corruption"]
    residual_keys = ["dataset", "class", "k_shot", "seed"]
    residual_groups = {key: group.loio_residual.to_numpy(dtype=np.float64) for key, group in residuals.groupby(residual_keys)}
    for key, target in frame.groupby(keys):
        dataset, target_class, k_shot, seed, corruption = key
        support_scores = residual_groups.get((dataset, target_class, k_shot, seed))
        if support_scores is None or target.label.nunique() < 2:
            continue
        target_p = conformalize(support_scores, target.raw_score.to_numpy(dtype=np.float64))
        labels = target.label.to_numpy(dtype=np.int64)
        anomaly_score = 1.0 - target_p
        for alpha in alphas:
            alarms = target_p <= alpha
            normal = labels == 0
            anomaly = labels == 1
            rows.append({
                "dataset": dataset,
                "class": target_class,
                "k_shot": k_shot,
                "seed": seed,
                "corruption": corruption,
                "method": "target_only",
                "alpha": alpha,
                "selected_p_threshold": alpha,
                "source_validation_far": float("nan"),
                "source_validation_count": len(support_scores),
                "false_alarm_rate": float(alarms[normal].mean()),
                "power": float(alarms[anomaly].mean()),
                "alarm_precision": float(labels[alarms].mean()) if alarms.any() else float("nan"),
                "coverage_gap": float(alarms[normal].mean() - alpha),
                "auroc": float(roc_auc_score(labels, anomaly_score)),
                "ap": float(average_precision_score(labels, anomaly_score)),
            })
    return pd.DataFrame(rows)


def evaluate(frame: pd.DataFrame, score_col: str, source_mode: str, alphas: list[float]) -> pd.DataFrame:
    rows = []
    keys = ["dataset", "class", "k_shot", "seed", "corruption"]
    for key, target in frame.groupby(keys):
        dataset, target_class, k_shot, seed, corruption = key
        source_corruption = corruption if source_mode == "matched_condition" else "clean"
        source = frame[
            (frame.dataset == dataset)
            & (frame["class"] != target_class)
            & (frame.k_shot == k_shot)
            & (frame.seed == seed)
            & (frame.corruption == source_corruption)
            & (frame.label == 0)
        ].copy()
        if source["class"].nunique() < 2 or target.label.nunique() < 2:
            continue
        target_scores = target[score_col].to_numpy(dtype=np.float64)
        target_p = conformalize(source[score_col].to_numpy(dtype=np.float64), target_scores)
        labels = target.label.to_numpy(dtype=np.int64)
        anomaly_score = 1.0 - target_p
        for alpha in alphas:
            threshold, validation_far, validation_count = source_validated_threshold(source, score_col, alpha)
            alarms = target_p <= threshold
            normal = labels == 0
            anomaly = labels == 1
            rows.append({
                "dataset": dataset,
                "class": target_class,
                "k_shot": k_shot,
                "seed": seed,
                "corruption": corruption,
                "source_mode": source_mode,
                "method": "source_validated_pool",
                "alpha": alpha,
                "selected_p_threshold": threshold,
                "source_validation_far": validation_far,
                "source_validation_count": validation_count,
                "false_alarm_rate": float(alarms[normal].mean()),
                "power": float(alarms[anomaly].mean()),
                "alarm_precision": float(labels[alarms].mean()) if alarms.any() else float("nan"),
                "coverage_gap": float(alarms[normal].mean() - alpha),
                "auroc": float(roc_auc_score(labels, anomaly_score)),
                "ap": float(average_precision_score(labels, anomaly_score)),
            })
    return pd.DataFrame(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--support-stats", required=True)
    parser.add_argument("--support-residuals", default=None, help="Long CSV of per-support LOIO residuals; enables the target_only anchor method.")
    parser.add_argument("--source-modes", nargs="+", default=["matched_condition", "clean_source"])
    parser.add_argument("--alphas", nargs="+", type=float, default=[0.05, 0.10, 0.20])
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="representative")
    args = parser.parse_args()

    frame = pd.concat([pd.read_csv(path) for path in args.inputs], ignore_index=True)
    stats = pd.read_csv(args.support_stats)
    frame = frame.merge(stats, on=["dataset", "class", "k_shot", "seed"], how="left")
    scale = np.maximum(frame.support_cal_mad.to_numpy(dtype=np.float64), 1e-6)
    frame["support_normalized_score"] = (frame.raw_score - frame.support_cal_median) / scale
    parts = [evaluate(frame, "support_normalized_score", mode, args.alphas) for mode in args.source_modes]
    if args.support_residuals:
        residuals = pd.read_csv(args.support_residuals)
        target_only = evaluate_target_only(frame, residuals, args.alphas)
        for mode in args.source_modes:
            replicated = target_only.copy()
            replicated["source_mode"] = mode
            parts.append(replicated)
    detailed = pd.concat(parts, ignore_index=True)
    metrics = ["selected_p_threshold", "source_validation_far", "false_alarm_rate", "power", "alarm_precision", "coverage_gap", "auroc", "ap"]
    summary = detailed.groupby(["dataset", "source_mode", "method", "k_shot", "corruption", "alpha"])[metrics].agg(["mean", "std"]).reset_index()
    summary.columns = ["_".join(str(part) for part in column if part) if isinstance(column, tuple) else str(column) for column in summary.columns]
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    detailed.to_csv(out / f"source_validated_threshold_{args.run_tag}_detailed.csv", index=False)
    summary.to_csv(out / f"source_validated_threshold_{args.run_tag}_summary.csv", index=False)
    print(f"wrote {len(detailed)} detailed rows and {len(summary)} summary rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
