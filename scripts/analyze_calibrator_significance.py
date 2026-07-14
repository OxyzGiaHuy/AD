"""Paired statistical comparison of calibrators + adaptive ECE.

Addresses two journal-review requirements:
1. Every headline "LOIO beats Platt" claim gets a paired Wilcoxon signed-rank
   test over class x seed x corruption cells (per k and per k x corruption),
   plus mean +/- std, instead of point estimates.
2. ECE binning is disclosed and complemented by an adaptive (equal-mass) ECE
   that is robust to the discreteness of few-shot conformal outputs: with at
   most k+1 distinct confidence values, equal-width bins can hide or inflate
   gaps; equal-mass bins group by value.

Inputs:
- per-image conformal views CSV (raw_score, conformal_prob_loio, label);
- per-cell calibrator detailed CSV (vector_platt / shift_aware_vector_platt
  ECE per class x seed x corruption) from the gated shift-aware evaluation.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np
import pandas as pd
from scipy.stats import wilcoxon

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.evaluation.metrics import ece_binary


def adaptive_ece(labels: np.ndarray, probs: np.ndarray, bins: int = 15) -> float:
    labels = labels.astype(float)
    probs = np.clip(probs.astype(float), 0.0, 1.0)
    if len(labels) == 0:
        return float("nan")
    n_bins = min(bins, len(np.unique(probs)))
    order = np.argsort(probs, kind="stable")
    splits = np.array_split(order, n_bins)
    ece = 0.0
    for idx in splits:
        if len(idx) == 0:
            continue
        ece += (len(idx) / len(labels)) * abs(probs[idx].mean() - labels[idx].mean())
    return float(ece)


def per_cell_conformal_ece(views: pd.DataFrame, prob_col: str) -> pd.DataFrame:
    rows = []
    for (dataset, cls, k, seed, corruption), g in views.groupby(["dataset", "class", "k_shot", "seed", "corruption"]):
        if g.label.nunique() < 2:
            continue
        y = g.label.to_numpy(dtype=np.int64)
        p = g[prob_col].to_numpy(dtype=np.float64)
        rows.append({
            "dataset": dataset, "class": cls, "k_shot": int(k), "seed": int(seed), "corruption": corruption,
            "method": prob_col,
            "ece": ece_binary(y, p),
            "adaptive_ece": adaptive_ece(y, p),
        })
    return pd.DataFrame(rows)


def paired_tests(cells: pd.DataFrame, baseline: str, candidate: str, metric: str) -> pd.DataFrame:
    keys = ["dataset", "class", "k_shot", "seed", "corruption"]
    pivot = cells.pivot_table(index=keys, columns="method", values=metric, aggfunc="mean").reset_index()
    pivot = pivot.dropna(subset=[baseline, candidate])
    out = []
    for (dataset, k), g in pivot.groupby(["dataset", "k_shot"]):
        groups = [("all", g)] + [(c, cg) for c, cg in g.groupby("corruption")]
        for corruption, cg in groups:
            delta = cg[candidate] - cg[baseline]
            if len(delta) < 5:
                continue
            try:
                stat, pval = wilcoxon(delta)
            except ValueError:
                stat, pval = float("nan"), float("nan")
            out.append({
                "dataset": dataset, "k_shot": k, "corruption": corruption, "metric": metric,
                "baseline": baseline, "candidate": candidate, "n_cells": len(delta),
                f"{baseline}_mean": cg[baseline].mean(), f"{baseline}_std": cg[baseline].std(),
                f"{candidate}_mean": cg[candidate].mean(), f"{candidate}_std": cg[candidate].std(),
                "delta_mean": delta.mean(), "delta_std": delta.std(),
                "wilcoxon_stat": stat, "wilcoxon_p": pval,
                "candidate_better_frac": float((delta < 0).mean()),
            })
    return pd.DataFrame(out)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--views", required=True, help="Per-image conformal views CSV")
    parser.add_argument("--platt-detailed", required=True, help="Per-cell calibrator detailed CSV (gated shift-aware)")
    parser.add_argument("--platt-methods", nargs="+", default=["vector_platt", "shift_aware_vector_platt"])
    parser.add_argument(
        "--extra-cells",
        nargs="*",
        default=[],
        help="Additional per-cell CSVs (dataset,class,k_shot,seed,corruption,method,ece[,adaptive_ece]) to include as baselines, e.g. scalar calibrator baselines",
    )
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", required=True)
    args = parser.parse_args()

    views = pd.read_csv(args.views)
    views = views[views.label.isin([0, 1])]
    conformal_cells = per_cell_conformal_ece(views, "conformal_prob_loio")

    platt = pd.read_csv(args.platt_detailed)
    platt = platt[platt.method.isin(args.platt_methods)]
    platt_cells = platt[["dataset", "class", "k_shot", "seed", "corruption", "method", "ece"]].copy()
    platt_cells["adaptive_ece"] = np.nan

    extra_methods: list[str] = []
    extra_frames: list[pd.DataFrame] = []
    for path in args.extra_cells:
        extra = pd.read_csv(path)
        cols = ["dataset", "class", "k_shot", "seed", "corruption", "method", "ece"]
        extra_cells = extra[cols].copy()
        extra_cells["adaptive_ece"] = extra["adaptive_ece"] if "adaptive_ece" in extra.columns else np.nan
        extra_frames.append(extra_cells)
        extra_methods.extend(m for m in extra_cells.method.unique() if m not in extra_methods)

    cells = pd.concat([conformal_cells, platt_cells, *extra_frames], ignore_index=True)
    tests = pd.concat(
        [paired_tests(cells, baseline, "conformal_prob_loio", "ece") for baseline in [*args.platt_methods, *extra_methods]],
        ignore_index=True,
    )

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    conformal_cells.to_csv(out / f"calibrator_cells_{args.run_tag}.csv", index=False)
    tests.to_csv(out / f"calibrator_significance_{args.run_tag}.csv", index=False)

    lines = [
        "# Paired Calibrator Comparison (Wilcoxon signed-rank over class x seed x corruption cells)",
        "",
        "ECE uses 15 equal-width bins (disclosed); conformal cells also report equal-mass adaptive ECE.",
        "",
        "| dataset | k | corruption | baseline | base mean+/-std | LOIO mean+/-std | delta | Wilcoxon p | LOIO better |",
        "|---|---:|---|---|---|---|---:|---:|---:|",
    ]
    for _, r in tests.iterrows():
        base = r["baseline"]
        lines.append(
            f"| {r.dataset} | {r.k_shot} | {r.corruption} | {base} | "
            f"{r[f'{base}_mean']:.4f}+/-{r[f'{base}_std']:.4f} | "
            f"{r['conformal_prob_loio_mean']:.4f}+/-{r['conformal_prob_loio_std']:.4f} | "
            f"{r.delta_mean:+.4f} | {r.wilcoxon_p:.2e} | {r.candidate_better_frac:.2f} |"
        )
    adaptive = conformal_cells.groupby("k_shot")[["ece", "adaptive_ece"]].mean()
    lines += ["", "## LOIO equal-width vs adaptive (equal-mass) ECE", "", "| k | equal-width ECE | adaptive ECE |", "|---:|---:|---:|"]
    for k, r in adaptive.iterrows():
        lines.append(f"| {k} | {r.ece:.4f} | {r.adaptive_ece:.4f} |")
    (out / f"calibrator_significance_{args.run_tag}.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(tests)} significance rows, {len(conformal_cells)} conformal cells")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
