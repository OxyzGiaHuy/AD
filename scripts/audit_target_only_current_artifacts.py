"""Recompute the target-only operating audit from the frozen GPU artifacts.

The current manuscript defines the asymmetric LOIO construction: calibration
scores use leave-one-image-out subspaces and each test score uses the full
support fit.  In the July 2026 export this construction is stored in
``image_p_loio_legacy``; ``image_p_loio`` stores the separate fold-matched
sensitivity analysis.  This script keeps that distinction explicit and emits
only descriptive pooled operating rates and CDF coordinates.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


CORRUPTIONS = ("blur", "brightness_contrast", "gaussian_noise", "jpeg")


def summarize(frame: pd.DataFrame, pvalue_col: str, alpha: float, tolerance: float) -> pd.DataFrame:
    rows: list[dict] = []
    selected = frame[
        frame["k_shot"].isin([4, 8])
        & frame["corruption"].isin(CORRUPTIONS)
        & frame["label"].isin([0, 1])
    ].copy()
    selected["alarm"] = selected[pvalue_col].astype(float) <= alpha + tolerance
    for (dataset, k_shot, corruption), group in selected.groupby(
        ["dataset", "k_shot", "corruption"], sort=True
    ):
        normal = group.label.eq(0)
        anomaly = group.label.eq(1)
        alarm = group.alarm
        n_alarm = int(alarm.sum())
        rows.append(
            {
                "dataset": dataset,
                "k_shot": int(k_shot),
                "corruption": corruption,
                "pvalue_col": pvalue_col,
                "alpha": alpha,
                "n_rows": len(group),
                "n_normal": int(normal.sum()),
                "n_anomaly": int(anomaly.sum()),
                "false_alarm_rate": float(alarm[normal].mean()),
                "detection_rate": float(alarm[anomaly].mean()),
                "precision": float((alarm & anomaly).sum() / n_alarm) if n_alarm else float("nan"),
            }
        )
    return pd.DataFrame(rows)


def aggregate(cells: pd.DataFrame) -> pd.DataFrame:
    return (
        cells.groupby(["dataset", "k_shot", "pvalue_col", "alpha"], as_index=False)
        .agg(
            false_alarm_rate=("false_alarm_rate", "mean"),
            detection_rate=("detection_rate", "mean"),
        )
    )


def category_cells(
    frame: pd.DataFrame, pvalue_col: str, alpha: float, tolerance: float
) -> pd.DataFrame:
    """Pool repeated support seeds within each declared category cell."""
    selected = frame[
        frame["k_shot"].isin([4, 8])
        & frame["corruption"].isin(CORRUPTIONS)
        & frame["label"].isin([0, 1])
    ].copy()
    selected["alarm"] = selected[pvalue_col].astype(float) <= alpha + tolerance
    rows: list[dict] = []
    for (dataset, category, k_shot, corruption), group in selected.groupby(
        ["dataset", "class", "k_shot", "corruption"], sort=True
    ):
        normal = group.label.eq(0)
        anomaly = group.label.eq(1)
        rows.append(
            {
                "dataset": dataset,
                "class": category,
                "k_shot": int(k_shot),
                "corruption": corruption,
                "pvalue_col": pvalue_col,
                "alpha": alpha,
                "n_normal": int(normal.sum()),
                "n_anomaly": int(anomaly.sum()),
                "false_alarm_rate": float(group.loc[normal, "alarm"].mean()),
                "detection_rate": float(group.loc[anomaly, "alarm"].mean()),
            }
        )
    return pd.DataFrame(rows)


def cdf_coordinates(frame: pd.DataFrame, pvalue_col: str, tolerance: float) -> pd.DataFrame:
    rows: list[dict] = []
    selected = frame[
        frame["k_shot"].isin([4, 8])
        & frame["corruption"].isin(CORRUPTIONS)
        & frame["label"].eq(0)
    ]
    for (dataset, k_shot, corruption), group in selected.groupby(
        ["dataset", "k_shot", "corruption"], sort=True
    ):
        p_values = group[pvalue_col].to_numpy(dtype=float)
        grid = np.arange(1, int(k_shot) + 2, dtype=float) / (int(k_shot) + 1)
        for point in grid:
            empirical = float(np.mean(p_values <= point + tolerance))
            rows.append(
                {
                    "dataset": dataset,
                    "k_shot": int(k_shot),
                    "corruption": corruption,
                    "pvalue_col": pvalue_col,
                    "nominal_cdf": point,
                    "empirical_cdf": empirical,
                    "gap": empirical - point,
                }
            )
    return pd.DataFrame(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--pvalue-col", default="image_p_loio_legacy")
    parser.add_argument("--alpha", type=float, default=0.20)
    parser.add_argument("--tolerance", type=float, default=1e-6)
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="target_only_current")
    args = parser.parse_args()

    frame = pd.concat([pd.read_csv(path) for path in args.inputs], ignore_index=True)
    required = {"dataset", "class", "k_shot", "corruption", "label", args.pvalue_col}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    cells = summarize(frame, args.pvalue_col, args.alpha, args.tolerance)
    aggregate_rows = aggregate(cells)
    category_rows = category_cells(frame, args.pvalue_col, args.alpha, args.tolerance)
    cdf = cdf_coordinates(frame, args.pvalue_col, args.tolerance)

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    cells.to_csv(out / f"{args.run_tag}_cells.csv", index=False)
    aggregate_rows.to_csv(out / f"{args.run_tag}_aggregate.csv", index=False)
    category_rows.to_csv(out / f"{args.run_tag}_category_cells.csv", index=False)
    cdf.to_csv(out / f"{args.run_tag}_cdf.csv", index=False)
    print(
        f"wrote {len(cells)} corruption cells, {len(aggregate_rows)} aggregates, "
        f"{len(category_rows)} category cells, and {len(cdf)} CDF coordinates"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
