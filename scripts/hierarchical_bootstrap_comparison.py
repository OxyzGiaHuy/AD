from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def paired_cells(frame: pd.DataFrame, baseline: str, candidate: str, metric: str) -> pd.DataFrame:
    keys = [column for column in ["dataset", "class", "k_shot", "seed", "corruption", "source_mode", "alpha"] if column in frame]
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
    return {
        "delta_mean": float(cells.groupby("class")["delta"].mean().mean()),
        "ci95_low": float(np.quantile(draws, 0.025)),
        "ci95_high": float(np.quantile(draws, 0.975)),
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
) -> pd.DataFrame:
    group_columns = [column for column in ["dataset", "k_shot", "corruption", "source_mode", "alpha"] if column in frame]
    rows: list[dict] = []
    for group_key, group in frame.groupby(group_columns, dropna=False):
        values = group_key if isinstance(group_key, tuple) else (group_key,)
        group_info = dict(zip(group_columns, values))
        for candidate in candidates:
            for metric in metrics:
                cells = paired_cells(group, baseline, candidate, metric)
                if cells.empty:
                    continue
                rows.append({
                    **group_info,
                    "baseline": baseline,
                    "candidate": candidate,
                    "metric": metric,
                    **hierarchical_bootstrap(cells, iterations=iterations, seed=seed),
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
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    frame = pd.read_csv(args.input)
    result = compare(frame, args.baseline, args.candidates, args.metrics, args.iterations, args.seed)
    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)
    result.to_csv(path, index=False)
    print(f"wrote {len(result)} comparisons to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
