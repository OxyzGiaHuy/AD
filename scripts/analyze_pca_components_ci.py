"""Paired hierarchical bootstrap CI for the PCA128-vs-PCA64 AUROC gain on VisA.

PCA64 per-cell metrics come from the benchmark-grid run directories
(`outputs/calib_subspace_head_visa_*/metrics.json`); PCA128 per-cell metrics
come from `visa_pca128_full_visa_detailed.csv`. Cells are paired on
(class, k, seed) and the class-then-seed hierarchical bootstrap from
`hierarchical_bootstrap_comparison` gives the interval.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.hierarchical_bootstrap_comparison import hierarchical_bootstrap, paired_cells

RUN_DIR_RE = re.compile(r"^calib_subspace_head_visa_(?P<cls>.+)_k(?P<k>\d+)_seed(?P<seed>\d+)_calib_subspace_head_k\d+_seed\d+_normal_synthetic$")


def load_pca64_cells(outputs_dir: Path) -> pd.DataFrame:
    rows = []
    for run_dir in sorted(outputs_dir.iterdir()):
        match = RUN_DIR_RE.match(run_dir.name)
        if not match:
            continue
        metrics_path = run_dir / "metrics.json"
        if not metrics_path.exists():
            continue
        metrics = json.loads(metrics_path.read_text())
        rows.append({
            "dataset": "visa",
            "class": match.group("cls"),
            "k_shot": int(match.group("k")),
            "seed": int(match.group("seed")),
            "method": "pca64",
            "auroc": float(metrics["auroc"]),
            "ap": float(metrics.get("ap", float("nan"))),
        })
    return pd.DataFrame(rows)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--pca128-detailed", default="outputs/paper_tables/visa_pca128_full_visa_detailed.csv")
    parser.add_argument("--iterations", type=int, default=5000)
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    args = parser.parse_args()

    pca64 = load_pca64_cells(Path(args.outputs_dir))
    pca128_src = pd.read_csv(args.pca128_detailed)
    pca128 = pca128_src[["dataset", "class", "k_shot", "seed", "auroc", "ap"]].copy()
    pca128["method"] = "pca128"
    frame = pd.concat([pca64, pca128], ignore_index=True)

    results = []
    for k in sorted(frame.k_shot.unique()):
        sub = frame[frame.k_shot == k]
        cells = paired_cells(sub, "pca64", "pca128", "auroc")
        if cells.empty:
            continue
        stats = hierarchical_bootstrap(cells, iterations=args.iterations, seed=0)
        stats["k_shot"] = int(k)
        stats["metric"] = "auroc"
        results.append(stats)
        print(f"k={k}: delta={stats['delta_mean']:+.4f} CI95=[{stats['ci95_low']:+.4f}, {stats['ci95_high']:+.4f}] cells={stats['n_paired_cells']}")

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(results).to_csv(out / "pca128_vs_pca64_visa_hierarchical_ci.csv", index=False)
    print(f"wrote {len(results)} rows to {out / 'pca128_vs_pca64_visa_hierarchical_ci.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
