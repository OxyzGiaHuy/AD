"""Uniformity diagnostics for few-shot conformal p-values on normal images.

Under exchangeability, a conformal p-value with n=k calibration scores is
super-uniform and satisfies P(p <= j/(k+1)) = j/(k+1) exactly at the grid
points j/(k+1). Because the p-values are discrete, a continuous KS test
against U(0,1) is invalid (it always rejects). This script therefore:

1. computes the empirical CDF at each attainable grid point (Q-Q data);
2. computes a discrete KS statistic D = max_j |F_hat(j/(k+1)) - j/(k+1)|;
3. calibrates D against an idealized exchangeable null by Monte Carlo while
   preserving dependence from shared calibration scores within each cluster.

Outputs per (dataset, k, corruption): D, Monte Carlo p-value, per-grid-point
empirical vs nominal CDF, and the direction of deviation (conservative if
empirical < nominal, anti-conservative if empirical > nominal).
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd


def discrete_ks(p_values: np.ndarray, k: int) -> tuple[float, np.ndarray, np.ndarray]:
    grid = np.arange(1, k + 2, dtype=np.float64) / (k + 1.0)
    empirical = np.array([(p_values <= g + 1e-6).mean() for g in grid])
    d_stat = float(np.max(np.abs(empirical - grid)))
    return d_stat, grid, empirical


def monte_carlo_pvalue(d_stat: float, n: int, k: int, iterations: int, rng: np.random.Generator) -> float:
    """IID discrete-uniform sensitivity analysis retained for compatibility."""
    grid = np.arange(1, k + 2, dtype=np.float64) / (k + 1.0)
    exceed = 0
    for _ in range(iterations):
        draws = rng.choice(grid, size=n, replace=True)
        d_null, _, _ = discrete_ks(draws, k)
        if d_null >= d_stat - 1e-12:
            exceed += 1
    return (1.0 + exceed) / (iterations + 1.0)


def monte_carlo_clustered_pvalue(
    d_stat: float,
    cluster_sizes: list[int],
    k: int,
    iterations: int,
    rng: np.random.Generator,
) -> float:
    """Simulate an exchangeable null with shared calibration per cluster."""

    if not cluster_sizes or any(size < 1 for size in cluster_sizes):
        raise ValueError("cluster_sizes must contain positive integers")
    exceed = 0
    for _ in range(iterations):
        simulated = []
        for size in cluster_sizes:
            calibration = rng.standard_normal(k)
            test = rng.standard_normal(size)
            counts = (calibration[:, None] >= test[None, :]).sum(axis=0)
            simulated.append((1.0 + counts) / (k + 1.0))
        d_null, _, _ = discrete_ks(np.concatenate(simulated), k)
        if d_null >= d_stat - 1e-12:
            exceed += 1
    return (1.0 + exceed) / (iterations + 1.0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--pvalue-col", default="image_p_loio")
    parser.add_argument("--iterations", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="pvalue_uniformity")
    parser.add_argument("--cluster-cols", nargs="+", default=["class", "seed"])
    args = parser.parse_args()

    frame = pd.concat([pd.read_csv(path) for path in args.inputs], ignore_index=True)
    frame = frame[(frame.label == 0) & frame[args.pvalue_col].notna()]
    rng = np.random.default_rng(args.seed)

    summary_rows = []
    qq_rows = []
    for (dataset, k_shot, corruption), group in frame.groupby(["dataset", "k_shot", "corruption"]):
        k = int(k_shot)
        p = group[args.pvalue_col].to_numpy(dtype=np.float64)
        d_stat, grid, empirical = discrete_ks(p, k)
        missing_cluster_cols = [column for column in args.cluster_cols if column not in group.columns]
        if missing_cluster_cols:
            raise ValueError(f"Missing cluster columns: {missing_cluster_cols}")
        cluster_sizes = group.groupby(args.cluster_cols, dropna=False).size().astype(int).tolist()
        mc_p = monte_carlo_clustered_pvalue(d_stat, cluster_sizes, k, args.iterations, rng)
        worst_idx = int(np.argmax(np.abs(empirical - grid)))
        summary_rows.append({
            "dataset": dataset,
            "k_shot": k,
            "corruption": corruption,
            "pvalue_col": args.pvalue_col,
            "n_normal": len(p),
            "n_clusters": len(cluster_sizes),
            "ks_discrete": d_stat,
            "mc_pvalue": mc_p,
            "worst_grid_point": grid[worst_idx],
            "worst_empirical_cdf": empirical[worst_idx],
            "direction": "anti-conservative" if empirical[worst_idx] > grid[worst_idx] else "conservative",
        })
        for g, e in zip(grid, empirical):
            qq_rows.append({
                "dataset": dataset,
                "k_shot": k,
                "corruption": corruption,
                "pvalue_col": args.pvalue_col,
                "nominal_cdf": g,
                "empirical_cdf": e,
                "gap": e - g,
            })

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    summary = pd.DataFrame(summary_rows)
    qq = pd.DataFrame(qq_rows)
    summary.to_csv(out / f"{args.run_tag}_summary.csv", index=False)
    qq.to_csv(out / f"{args.run_tag}_qq.csv", index=False)

    lines = [
        "# Normal P-Value Uniformity (Discrete-Grid KS)",
        "",
        "Under exchangeability P(p <= j/(k+1)) = j/(k+1); the discrete KS statistic",
        "uses a cluster-aware Monte Carlo reference under an idealized exchangeable null.",
        "",
        "| dataset | k | corruption | n | clusters | KS_D | MC p-value | worst grid | empirical | direction |",
        "|---|---:|---|---:|---:|---:|---:|---:|---:|---|",
    ]
    for _, r in summary.iterrows():
        lines.append(
            f"| {r.dataset} | {r.k_shot} | {r.corruption} | {r.n_normal} | {r.n_clusters} | {r.ks_discrete:.4f} | "
            f"{r.mc_pvalue:.4f} | {r.worst_grid_point:.3f} | {r.worst_empirical_cdf:.4f} | {r.direction} |"
        )
    (out / f"{args.run_tag}_summary.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {len(summary)} uniformity rows and {len(qq)} qq rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
