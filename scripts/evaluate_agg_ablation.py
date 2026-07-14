"""Aggregation-sensitivity ablation: max versus top-rho patch-residual pooling.

The clean accuracy-storage benchmark aggregates patch residuals with max,
while the conformal pipeline uses the mean of the top-1% residuals. This
ablation quantifies how sensitive image-level ranking (AUROC/AP) is to that
choice, on representative classes of both datasets, using cached clean eval
features so no backbone forward is needed.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.export_sw_cad_image_views import get_features
from src.config import load_config
from src.conformal import top_fraction_score
from src.data.datasets import load_records
from src.data.sampling import evaluation_records, few_shot_support
from src.evaluation.metrics import average_precision_np, roc_auc_score_np
from src.models.pca import PCASubspace

REPRESENTATIVE = {
    "visa": ["candle", "cashew", "pcb1", "pipe_fryum"],
    "mvtec": ["bottle", "cable", "hazelnut"],
}


def aggregate(patch_scores: np.ndarray, mode: str) -> np.ndarray:
    if mode == "max":
        return patch_scores.max(axis=1).astype(np.float32)
    rho = float(mode.split("_")[1])
    return top_fraction_score(patch_scores, rho=rho)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-config", default="configs/generated/visa_full/calib_subspace_head_visa_candle_k1_seed0.yaml")
    parser.add_argument("--datasets", nargs="+", default=["mvtec", "visa"])
    parser.add_argument("--k-shots", nargs="*", type=int, default=[4, 8])
    parser.add_argument("--seeds", nargs="*", type=int, default=[0, 1, 2])
    parser.add_argument("--aggregators", nargs="*", default=["max", "top_0.005", "top_0.01", "top_0.02", "top_0.05"])
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    args = parser.parse_args()

    config = load_config(args.base_config)
    pca_components = int(config.get("model", {}).get("pca_components", 64))
    backbone_name = config.get("backbone", {}).get("name", "dinov2_vits14")

    rows = []
    for dataset in args.datasets:
        for cls in REPRESENTATIVE[dataset]:
            records = load_records(dataset, f"data/{dataset}", [cls])
            eval_recs = evaluation_records(records)
            labels = np.asarray([r.label for r in eval_recs], dtype=np.int64)
            eval_feats = get_features(config, eval_recs, f"{dataset}_eval_{backbone_name}", 0, cache_seed=0)
            for k in args.k_shots:
                for seed in args.seeds:
                    support = few_shot_support(records, k=k, seed=seed)
                    support_feats = get_features(config, support, f"{dataset}_support_{backbone_name}_k{k}_seed{seed}", seed)
                    pca = PCASubspace.fit(support_feats, pca_components)
                    patch_scores = pca.residual_scores(eval_feats).astype(np.float32)
                    for agg in args.aggregators:
                        image_scores = aggregate(patch_scores, agg)
                        rows.append({
                            "dataset": dataset, "class": cls, "k_shot": k, "seed": seed,
                            "aggregator": agg,
                            "auroc": roc_auc_score_np(labels, image_scores),
                            "ap": average_precision_np(labels, image_scores),
                        })
                    print(f"agg_ablation dataset={dataset} class={cls} k={k} seed={seed}", flush=True)

    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    detailed = pd.DataFrame(rows)
    detailed.to_csv(out / "agg_ablation_detailed.csv", index=False)
    summary = detailed.groupby(["dataset", "k_shot", "aggregator"]).agg(
        auroc_mean=("auroc", "mean"), auroc_std=("auroc", "std"),
        ap_mean=("ap", "mean"), ap_std=("ap", "std"), n=("auroc", "size"),
    ).reset_index()
    summary.to_csv(out / "agg_ablation_summary.csv", index=False)
    print(summary.round(4).to_string(index=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
