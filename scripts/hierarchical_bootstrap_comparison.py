from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def paired_cells(frame: pd.DataFrame, baseline: str, candidate: str, metric: str) -> pd.DataFrame:
    if "class" not in frame and "target_class" in frame:
        frame = frame.rename(columns={"target_class": "class"})
    keys = [column for column in [
        "job_id", "analysis_id", "dataset", "source_dataset", "class", "k_shot",
        "seed", "corruption", "source_mode", "normalization_mode", "unit", "alpha",
    ] if column in frame]
    pivot = frame[frame["method"].isin([baseline, candidate])].pivot_table(
        index=keys, columns="method", values=metric, aggfunc="mean"
    ).reset_index()
    if baseline not in pivot or candidate not in pivot:
        return pd.DataFrame()
    pivot = pivot.dropna(subset=[baseline, candidate])
    pivot["delta"] = pivot[candidate] - pivot[baseline]
    return pivot


def hierarchical_bootstrap(
    cells: pd.DataFrame,
    iterations: int = 5000,
    seed: int = 0,
    interval_alpha: float = 0.05,
) -> dict[str, float]:
    if cells.empty:
        raise ValueError("No paired cells")
    rng = np.random.default_rng(seed)
    classes = cells["class"].unique()
    by_class = {
        cls: group.groupby("seed")["delta"].mean().to_numpy(dtype=np.float64)
        for cls, group in cells.groupby("class")
    }
    draws = np.empty(iterations, dtype=np.float64)
    for iteration in range(iterations):
        sampled_classes = rng.choice(classes, size=len(classes), replace=True)
        class_means = []
        for cls in sampled_classes:
            seed_means = by_class[cls]
            sampled = rng.choice(seed_means, size=len(seed_means), replace=True)
            class_means.append(float(np.mean(sampled)))
        draws[iteration] = float(np.mean(class_means))
    if not 0.0 < interval_alpha < 1.0:
        raise ValueError("interval_alpha must be in (0, 1)")
    low = float(np.quantile(draws, interval_alpha / 2.0))
    high = float(np.quantile(draws, 1.0 - interval_alpha / 2.0))
    pointwise_low = float(np.quantile(draws, 0.025))
    pointwise_high = float(np.quantile(draws, 0.975))
    return {
        "delta_mean": float(cells.groupby("class")["delta"].mean().mean()),
        "ci_low": low,
        "ci_high": high,
        # Backward-compatible fields retain their literal pointwise-95% meaning.
        # The primary multiplicity-adjusted limits are ci_low/ci_high.
        "ci95_low": pointwise_low,
        "ci95_high": pointwise_high,
        "interval_alpha": float(interval_alpha),
        "prob_delta_lt_zero": float((draws < 0).mean()),
        "n_classes": int(len(classes)),
        "n_paired_cells": int(len(cells)),
    }


def compare(
    frame: pd.DataFrame,
    baseline: str,
    candidates: list[str],
    metrics: list[str],
    iterations: int,
    seed: int,
    family_alpha: float = 0.05,
    multiplicity: str = "bonferroni",
) -> pd.DataFrame:
    group_columns = [column for column in [
        "job_id", "analysis_id", "dataset", "source_dataset", "k_shot",
        "corruption", "source_mode", "normalization_mode", "unit", "alpha",
    ] if column in frame]
    specifications: list[tuple[dict, str, str, pd.DataFrame]] = []
    for group_key, group in frame.groupby(group_columns, dropna=False):
        values = group_key if isinstance(group_key, tuple) else (group_key,)
        group_info = dict(zip(group_columns, values))
        for candidate in candidates:
            for metric in metrics:
                cells = paired_cells(group, baseline, candidate, metric)
                if cells.empty:
                    continue
                specifications.append((group_info, candidate, metric, cells))
    family_size = len(specifications)
    if family_size == 0:
        return pd.DataFrame()
    if multiplicity not in {"bonferroni", "pointwise"}:
        raise ValueError("multiplicity must be 'bonferroni' or 'pointwise'")
    interval_alpha = family_alpha / family_size if multiplicity == "bonferroni" else family_alpha
    rows: list[dict] = []
    for group_info, candidate, metric, cells in specifications:
        rows.append({
                    **group_info,
                    "baseline": baseline,
                    "candidate": candidate,
                    "metric": metric,
                    "multiplicity_method": multiplicity,
                    "family_alpha": family_alpha,
                    "family_size": family_size,
                    **hierarchical_bootstrap(
                        cells, iterations=iterations, seed=seed, interval_alpha=interval_alpha
                    ),
                })
    return pd.DataFrame(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--baseline", default="target_only")
    parser.add_argument("--candidates", nargs="+", required=True)
    parser.add_argument("--metrics", nargs="+", default=["false_alarm_rate", "power", "alarm_precision"])
    parser.add_argument("--iterations", type=int, default=5000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--family-alpha", type=float, default=0.05)
    parser.add_argument("--multiplicity", choices=["bonferroni", "pointwise"], default="bonferroni")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    frame = pd.read_csv(args.input)
    result = compare(
        frame, args.baseline, args.candidates, args.metrics, args.iterations,
        args.seed, args.family_alpha, args.multiplicity
    )
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(path, index=False)
    print(f"wrote {len(result)} comparisons to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
