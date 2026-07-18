"""Randomized (smoothed) conformal p-values as a below-the-floor baseline for SC3R.

The natural objection to SC3R is: "to alarm below the attainable floor
1/(k+1), just randomize the p-value." The smoothed conformal p-value

    p_rand(x) = (#{r > s(x)} + U * (1 + #{r = s(x)})) / (k + 1),  U ~ Uniform(0,1)

is exactly Uniform(0,1) under exchangeability and is continuous, so alarms at
any nominal alpha are attainable. This script evaluates that baseline on the
same target-only LOIO residuals and the same label-stratified test images as
SC3R, using the closed-form expected alarm indicator

    P(p_rand <= alpha) = clip((alpha * (k+1) - #{r > s}) / (1 + #{r = s}), 0, 1),

so no Monte Carlo is needed: reported FAR/power are exact expectations over
the randomization. Output matches the source_validated_threshold schema so the
comparison against SC3R and the deterministic anchor is direct.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score


def expected_alarm_prob(residuals: np.ndarray, scores: np.ndarray, alpha: float) -> np.ndarray:
    r = np.asarray(residuals, dtype=np.float64).reshape(-1, 1)
    s = np.asarray(scores, dtype=np.float64).reshape(1, -1)
    n_gt = (r > s).sum(axis=0).astype(np.float64)
    n_eq = (r == s).sum(axis=0).astype(np.float64)
    k = len(residuals)
    return np.clip((alpha * (k + 1) - n_gt) / (1.0 + n_eq), 0.0, 1.0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--views", required=True, help="SC3R views CSV (raw_score per image)")
    parser.add_argument("--support-residuals", required=True, help="Long CSV of per-support LOIO residuals")
    parser.add_argument("--alphas", nargs="+", type=float, default=[0.05, 0.10, 0.20])
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", required=True)
    args = parser.parse_args()

    views = pd.read_csv(args.views)
    views = views[views.label.isin([0, 1])]
    residuals = pd.read_csv(args.support_residuals)
    residual_groups = {
        key: group.loio_residual.to_numpy(dtype=np.float64)
        for key, group in residuals.groupby(["dataset", "class", "k_shot", "seed"])
    }

    rows = []
    for key, target in views.groupby(["dataset", "class", "k_shot", "seed", "corruption"]):
        dataset, cls, k_shot, seed, corruption = key
        support = residual_groups.get((dataset, cls, k_shot, seed))
        if support is None or target.label.nunique() < 2:
            continue
        scores = target.raw_score.to_numpy(dtype=np.float64)
        labels = target.label.to_numpy(dtype=np.int64)
        normal = labels == 0
        anomaly = labels == 1
        anomaly_rank = 1.0 - expected_alarm_prob(support, scores, 0.5)  # rank-preserving view
        for alpha in args.alphas:
            alarm_prob = expected_alarm_prob(support, scores, alpha)
            far = float(alarm_prob[normal].mean())
            power = float(alarm_prob[anomaly].mean())
            expected_alarms = float(alarm_prob.sum())
            precision = float(alarm_prob[anomaly].sum() / expected_alarms) if expected_alarms > 0 else float("nan")
            rows.append({
                "dataset": dataset, "class": cls, "k_shot": int(k_shot), "seed": int(seed),
                "corruption": corruption, "source_mode": "target_only",
                "method": "randomized_pvalue", "alpha": alpha,
                "false_alarm_rate": far, "power": power, "alarm_precision": precision,
                "coverage_gap": far - alpha,
                "auroc": float(roc_auc_score(labels, scores)),
                "ap": float(average_precision_score(labels, scores)),
            })

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    detailed = pd.DataFrame(rows)
    detailed.to_csv(out / f"randomized_pvalue_{args.run_tag}_detailed.csv", index=False)
    summary = detailed.groupby(["dataset", "k_shot", "corruption", "alpha"]).agg(
        far_mean=("false_alarm_rate", "mean"), far_std=("false_alarm_rate", "std"),
        power_mean=("power", "mean"), power_std=("power", "std"),
        precision_mean=("alarm_precision", "mean"), n_cells=("false_alarm_rate", "size"),
    ).reset_index()
    summary.to_csv(out / f"randomized_pvalue_{args.run_tag}_summary.csv", index=False)
    pooled = detailed.groupby(["dataset", "k_shot", "alpha"])[["false_alarm_rate", "power"]].mean().round(3)
    print(pooled.to_string())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
