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

from scripts.evaluate_prevalence_stress import expected_calibration_error


def conformalize(source_normal_scores: np.ndarray, target_scores: np.ndarray) -> np.ndarray:
    source = np.asarray(source_normal_scores, dtype=np.float64).reshape(-1)
    target = np.asarray(target_scores, dtype=np.float64).reshape(-1)
    if len(source) == 0:
        raise ValueError("Source normal archive is empty")
    counts = (source[:, None] >= target[None, :]).sum(axis=0)
    return (1.0 + counts) / (len(source) + 1.0)


def operating_metrics(labels: np.ndarray, probs: np.ndarray, alpha: float) -> dict[str, float]:
    p_values = 1.0 - np.clip(probs, 0.0, 1.0)
    alarms = p_values <= alpha
    normal = labels == 0
    anomaly = labels == 1
    false_alarm = float(alarms[normal].mean()) if normal.any() else float("nan")
    power = float(alarms[anomaly].mean()) if anomaly.any() else float("nan")
    precision = float(labels[alarms].mean()) if alarms.any() else float("nan")
    return {
        "false_alarm_rate": false_alarm,
        "power": power,
        "alarm_precision": precision,
        "coverage_gap": false_alarm - alpha,
    }


def evaluate_group(
    target: pd.DataFrame,
    source: pd.DataFrame,
    prob_col: str,
    source_score_col: str | None,
    alphas: list[float],
    mix_weights: list[float],
) -> list[dict]:
    source_normal = source[source["label"] == 0]
    statistic_col = source_score_col or prob_col
    source_stat = pd.to_numeric(source_normal[statistic_col], errors="coerce").to_numpy(dtype=np.float64)
    source_stat = source_stat[np.isfinite(source_stat)]
    target_prob = pd.to_numeric(target[prob_col], errors="coerce").to_numpy(dtype=np.float64)
    target_stat = pd.to_numeric(target[statistic_col], errors="coerce").to_numpy(dtype=np.float64)
    labels = target["label"].to_numpy(dtype=np.int64)
    valid = np.isfinite(target_prob) & np.isfinite(target_stat)
    target_prob = target_prob[valid]
    target_stat = target_stat[valid]
    labels = labels[valid]
    source_p = conformalize(source_stat, target_stat)
    source_prob = 1.0 - source_p

    methods = {"target_only": target_prob, "source_pool": source_prob}
    for weight in mix_weights:
        methods[f"source_mix_{weight:.2f}"] = (1.0 - weight) * target_prob + weight * source_prob

    rows: list[dict] = []
    for method, probs in methods.items():
        base = {
            "method": method,
            "n_images": len(labels),
            "source_normal_count": len(source_stat),
            "auroc": float(roc_auc_score(labels, probs)),
            "ap": float(average_precision_score(labels, probs)),
            "ece": expected_calibration_error(labels, probs, 15),
            "brier": float(np.mean((probs - labels) ** 2)),
        }
        for alpha in alphas:
            row = {**base, "alpha": alpha}
            row.update(operating_metrics(labels, probs, alpha))
            rows.append(row)
    return rows


def evaluate(
    frame: pd.DataFrame,
    prob_col: str,
    source_score_col: str | None,
    source_mode: str,
    alphas: list[float],
    mix_weights: list[float],
) -> pd.DataFrame:
    required = {"dataset", "class", "k_shot", "seed", "corruption", "label", prob_col}
    if source_score_col:
        required.add(source_score_col)
    missing = required - set(frame.columns)
    if missing:
        raise KeyError(f"Missing columns: {sorted(missing)}")
    rows: list[dict] = []
    keys = ["dataset", "class", "k_shot", "seed", "corruption"]
    for key, target in frame.groupby(keys):
        dataset, target_class, k_shot, seed, corruption = key
        source_corruption = corruption if source_mode == "matched_condition" else "clean"
        source = frame[
            (frame["dataset"] == dataset)
            & (frame["class"] != target_class)
            & (frame["k_shot"] == k_shot)
            & (frame["seed"] == seed)
            & (frame["corruption"] == source_corruption)
        ]
        if source[source["label"] == 0].empty or target["label"].nunique() < 2:
            continue
        for result in evaluate_group(target, source, prob_col, source_score_col, alphas, mix_weights):
            rows.append(
                {
                    "dataset": dataset,
                    "class": target_class,
                    "k_shot": k_shot,
                    "seed": seed,
                    "corruption": corruption,
                    "source_mode": source_mode,
                    "source_corruption": source_corruption,
                    **result,
                }
            )
    return pd.DataFrame(rows)


def summarize(detailed: pd.DataFrame) -> pd.DataFrame:
    group = ["dataset", "source_mode", "method", "k_shot", "corruption", "alpha"]
    metrics = [
        "false_alarm_rate",
        "power",
        "alarm_precision",
        "coverage_gap",
        "auroc",
        "ap",
        "ece",
        "brier",
        "source_normal_count",
    ]
    summary = detailed.groupby(group)[metrics].agg(["mean", "std"]).reset_index()
    summary.columns = [
        "_".join(str(part) for part in col if part) if isinstance(col, tuple) else str(col)
        for col in summary.columns
    ]
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--prob-col", default="conformal_prob_loio")
    parser.add_argument("--source-score-col", default=None)
    parser.add_argument("--support-stats", default=None)
    parser.add_argument("--source-modes", nargs="*", default=["matched_condition", "clean_source"])
    parser.add_argument("--alphas", nargs="*", type=float, default=[0.05, 0.10, 0.20])
    parser.add_argument("--mix-weights", nargs="*", type=float, default=[0.25, 0.50, 0.75])
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="representative")
    args = parser.parse_args()

    frame = pd.concat([pd.read_csv(path) for path in args.inputs], ignore_index=True)
    if args.support_stats:
        stats = pd.read_csv(args.support_stats)
        frame = frame.merge(stats, on=["dataset", "class", "k_shot", "seed"], how="left")
        scale = np.maximum(pd.to_numeric(frame["support_cal_mad"], errors="coerce"), 1e-6)
        frame["support_normalized_score"] = (
            pd.to_numeric(frame["raw_score"], errors="coerce")
            - pd.to_numeric(frame["support_cal_median"], errors="coerce")
        ) / scale
    results = [
        evaluate(frame, args.prob_col, args.source_score_col, source_mode, args.alphas, args.mix_weights)
        for source_mode in args.source_modes
    ]
    detailed = pd.concat([result for result in results if not result.empty], ignore_index=True)
    summary = summarize(detailed)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    detailed.to_csv(out / f"source_conditioned_routing_{args.run_tag}_detailed.csv", index=False)
    summary.to_csv(out / f"source_conditioned_routing_{args.run_tag}_summary.csv", index=False)
    print(f"wrote {len(detailed)} detailed rows and {len(summary)} summary rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
