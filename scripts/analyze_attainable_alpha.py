from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def attainable_alphas(n_calibration: int) -> np.ndarray:
    return np.arange(1, n_calibration + 2, dtype=np.float64) / (n_calibration + 1.0)


def nearest_attainable(nominal: float, n_calibration: int) -> float:
    grid = attainable_alphas(n_calibration)
    valid = grid[grid <= nominal + 1e-12]
    return float(valid.max()) if len(valid) else 0.0


def analyze(frame: pd.DataFrame, pvalue_col: str, alphas: list[float]) -> pd.DataFrame:
    rows = []
    for (dataset, cls, k_shot, seed, corruption), group in frame.groupby(
        ["dataset", "class", "k_shot", "seed", "corruption"]
    ):
        n_cal = int(k_shot)
        p = group[pvalue_col].to_numpy(dtype=np.float64)
        labels = group.label.to_numpy(dtype=np.int64)
        normal = labels == 0
        anomaly = labels == 1
        if not normal.any():
            continue
        for alpha in alphas:
            attainable = nearest_attainable(alpha, n_cal)
            # tolerance absorbs float32 rounding of stored p-values (e.g. 1/5 -> 0.20000000298)
            alarm_nominal = p <= alpha + 1e-6
            rows.append({
                "dataset": dataset,
                "class": cls,
                "k_shot": k_shot,
                "seed": seed,
                "corruption": corruption,
                "pvalue_col": pvalue_col,
                "nominal_alpha": alpha,
                "n_calibration": n_cal,
                "alpha_floor": 1.0 / (n_cal + 1.0),
                "nearest_attainable_alpha": attainable,
                "alpha_resolution_gap": alpha - attainable,
                "below_floor": alpha < 1.0 / (n_cal + 1.0),
                "false_alarm_rate": float(alarm_nominal[normal].mean()),
                "detection_rate": float(alarm_nominal[anomaly].mean()) if anomaly.any() else float("nan"),
                "coverage_gap": float(alarm_nominal[normal].mean() - alpha),
                "n_normal": int(normal.sum()),
                "n_anomaly": int(anomaly.sum()),
            })
    return pd.DataFrame(rows)


def markdown(summary: pd.DataFrame) -> str:
    lines = [
        "# Attainable Alpha Analysis",
        "",
        "Few-shot LOIO conformal p-values are quantized: with n calibration scores the",
        "smallest attainable p-value is 1/(n+1), so any nominal alpha below that floor",
        "cannot raise alarms and empirical false-alarm rates sit below nominal by the",
        "alpha resolution gap. This table explains observed conservativeness.",
        "",
        "| dataset | k | corruption | nominal | floor | attainable | resolution gap | FAR | detection |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|",
    ]
    for _, r in summary.iterrows():
        lines.append(
            f"| {r['dataset']} | {int(r['k_shot'])} | {r['corruption']} | {r['nominal_alpha']:.2f} | "
            f"{r['alpha_floor']:.3f} | {r['nearest_attainable_alpha']:.3f} | {r['alpha_resolution_gap']:+.3f} | "
            f"{r['false_alarm_rate_mean']:.4f} | {r['detection_rate_mean']:.4f} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--pvalue-col", default="image_p_loio")
    parser.add_argument("--alphas", nargs="+", type=float, default=[0.01, 0.05, 0.10, 0.20])
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="attainable_alpha")
    args = parser.parse_args()

    frame = pd.concat([pd.read_csv(path) for path in args.inputs], ignore_index=True)
    frame = frame[frame.label.isin([0, 1])]
    detailed = analyze(frame, args.pvalue_col, args.alphas)
    if detailed.empty:
        raise SystemExit("No analyzable rows found")
    group_cols = ["dataset", "k_shot", "corruption", "pvalue_col", "nominal_alpha", "alpha_floor", "nearest_attainable_alpha", "alpha_resolution_gap", "below_floor"]
    summary = (
        detailed.groupby(group_cols)[["false_alarm_rate", "detection_rate", "coverage_gap"]]
        .agg(["mean", "std"])
        .reset_index()
    )
    summary.columns = ["_".join(str(p) for p in c if p) if isinstance(c, tuple) else str(c) for c in summary.columns]
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    detailed.to_csv(out / f"attainable_alpha_{args.run_tag}_detailed.csv", index=False)
    summary.to_csv(out / f"attainable_alpha_{args.run_tag}_summary.csv", index=False)
    (out / f"attainable_alpha_{args.run_tag}_summary.md").write_text(markdown(summary), encoding="utf-8")
    print(f"wrote {len(detailed)} detailed rows and {len(summary)} summary rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
