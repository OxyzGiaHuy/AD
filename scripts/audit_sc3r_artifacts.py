"""Fail-closed lineage audit for SC3R GPU-export artifacts."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd


VIEW_COLUMNS = {
    "dataset",
    "class",
    "k_shot",
    "seed",
    "corruption",
    "base_image_path",
    "image_path",
    "label",
    "raw_score",
    "sampling_protocol",
    "sampling_seed",
    "max_images",
    "corruption_parameters",
}
SUPPORT_COLUMNS = {"dataset", "class", "k_shot", "seed", "support_index", "image_path"}
STAT_COLUMNS = {
    "dataset", "class", "k_shot", "seed", "support_calibration_mode",
    "support_cal_median", "support_cal_mad", "support_cal_q25",
    "support_cal_q75", "support_cal_count",
}


def _normalise_path(value: object) -> str:
    return str(Path(str(value)).expanduser().resolve(strict=False))


def audit_frames(
    views: pd.DataFrame,
    stats: pd.DataFrame,
    support: pd.DataFrame,
    expected_k_shots: list[int] | None = None,
    expected_seeds: list[int] | None = None,
    expected_corruptions: list[str] | None = None,
) -> dict:
    issues: list[str] = []
    for name, frame, required in (
        ("views", views, VIEW_COLUMNS),
        ("stats", stats, STAT_COLUMNS),
        ("support", support, SUPPORT_COLUMNS),
    ):
        missing = sorted(required - set(frame.columns))
        if missing:
            issues.append(f"{name}: missing columns {missing}")
    if issues:
        return {"status": "fail", "issues": issues}

    view_key = ["dataset", "class", "k_shot", "seed", "corruption", "base_image_path"]
    duplicated_views = int(views.duplicated(view_key, keep=False).sum())
    if duplicated_views:
        issues.append(f"views: {duplicated_views} rows participate in duplicate base-image cell keys")
    stat_key = ["dataset", "class", "k_shot", "seed"]
    duplicated_stats = int(stats.duplicated(stat_key, keep=False).sum())
    if duplicated_stats:
        issues.append(f"stats: {duplicated_stats} rows participate in duplicate keys")
    support_key = stat_key + ["support_index"]
    duplicated_support = int(support.duplicated(support_key, keep=False).sum())
    if duplicated_support:
        issues.append(f"support: {duplicated_support} rows participate in duplicate keys")

    if not set(views["label"].dropna().astype(int).unique()).issubset({0, 1}):
        issues.append("views: labels must be binary")
    if not np.isfinite(views["raw_score"].astype(float)).all():
        issues.append("views: raw_score contains missing or non-finite values")
    if (stats["support_cal_mad"].astype(float) < 0).any():
        issues.append("stats: support_cal_mad contains negative values")
    stat_values = stats[["support_cal_median", "support_cal_mad", "support_cal_q25", "support_cal_q75"]].astype(float)
    if not np.isfinite(stat_values.to_numpy()).all():
        issues.append("stats: support statistics contain missing or non-finite values")
    quantile_order = (
        (stats.support_cal_q25.astype(float) <= stats.support_cal_median.astype(float))
        & (stats.support_cal_median.astype(float) <= stats.support_cal_q75.astype(float))
    )
    if not quantile_order.all():
        issues.append("stats: support quantiles/median are out of order")
    expected_modes = stats["k_shot"].astype(int).map(lambda k: "patch_split_conformal" if k == 1 else "loio_conformal")
    if (stats["support_calibration_mode"].astype(str) != expected_modes).any():
        issues.append("stats: support calibration mode is inconsistent with k")

    support_counts = support.groupby(stat_key).size().rename("manifest_count").reset_index()
    expected = support_counts["k_shot"].astype(int)
    wrong_manifest_count = support_counts[support_counts["manifest_count"] != expected]
    if not wrong_manifest_count.empty:
        issues.append(f"support: {len(wrong_manifest_count)} cells do not contain exactly k images")
    merged_counts = stats.merge(support_counts, on=stat_key, how="outer", indicator=True)
    if (merged_counts["_merge"] != "both").any():
        issues.append("stats/support: key sets differ")
    elif (merged_counts["support_cal_count"].astype(int) != merged_counts["manifest_count"].astype(int)).any():
        issues.append("stats/support: support_cal_count differs from manifest count")

    view_cells = views[stat_key].drop_duplicates()
    stat_cells = stats[stat_key].drop_duplicates()
    missing_stats = view_cells.merge(stat_cells, on=stat_key, how="left", indicator=True)
    missing_stats = missing_stats[missing_stats["_merge"] == "left_only"]
    if not missing_stats.empty:
        issues.append(f"views/stats: {len(missing_stats)} view cells lack support statistics")

    eval_paths = {_normalise_path(path) for path in views["base_image_path"]}
    support_paths = {_normalise_path(path) for path in support["image_path"]}
    overlap = sorted(eval_paths & support_paths)
    if overlap:
        issues.append(f"leakage: {len(overlap)} support paths also occur as evaluation base images")

    if (views.sampling_seed.astype(int) != views.seed.astype(int)).any():
        issues.append("views: sampling_seed differs from experiment seed")
    if views.sampling_protocol.astype(str).str.strip().eq("").any():
        issues.append("views: sampling_protocol contains empty values")
    if views.corruption_parameters.astype(str).str.strip().eq("").any():
        issues.append("views: corruption_parameters contains empty values")

    paired_keys = ["dataset", "class", "k_shot", "seed"]
    for key, group in views.groupby(paired_keys, sort=True):
        condition_sets = {
            str(condition): set(block.base_image_path.astype(str))
            for condition, block in group.groupby("corruption", sort=True)
        }
        if len({frozenset(paths) for paths in condition_sets.values()}) > 1:
            issues.append(f"views: corruption base-image sets differ in cell {key}")
        label_counts = group.groupby("base_image_path").label.nunique()
        if (label_counts > 1).any():
            issues.append(f"views: labels differ across corruption views in cell {key}")

    for key, group in support.groupby(["dataset", "class", "seed"], sort=True):
        support_by_k = {
            int(k): set(block.image_path.astype(str))
            for k, block in group.groupby("k_shot", sort=True)
        }
        ordered_k = sorted(support_by_k)
        for smaller, larger in zip(ordered_k, ordered_k[1:]):
            if not support_by_k[smaller].issubset(support_by_k[larger]):
                issues.append(f"support: k-shot sets are not nested for cell {key}: k={smaller} vs k={larger}")

    observed_k = set(views.k_shot.astype(int))
    observed_seeds = set(views.seed.astype(int))
    observed_corruptions = set(views.corruption.astype(str))
    if expected_k_shots is not None and observed_k != set(expected_k_shots):
        issues.append(f"views: k-shot grid mismatch; observed={sorted(observed_k)} expected={sorted(expected_k_shots)}")
    if expected_seeds is not None and observed_seeds != set(expected_seeds):
        issues.append(f"views: seed grid mismatch; observed={sorted(observed_seeds)} expected={sorted(expected_seeds)}")
    if expected_corruptions is not None and observed_corruptions != set(expected_corruptions):
        issues.append(
            "views: corruption grid mismatch; "
            f"observed={sorted(observed_corruptions)} expected={sorted(expected_corruptions)}"
        )

    condition_counts = views.groupby(["dataset", "class", "k_shot", "seed", "corruption"]).size()
    summary = {
        "status": "pass" if not issues else "fail",
        "issues": issues,
        "n_view_rows": int(len(views)),
        "n_support_rows": int(len(support)),
        "n_stat_rows": int(len(stats)),
        "n_view_cells": int(len(condition_counts)),
        "min_rows_per_cell": int(condition_counts.min()) if len(condition_counts) else 0,
        "max_rows_per_cell": int(condition_counts.max()) if len(condition_counts) else 0,
        "datasets": sorted(views["dataset"].astype(str).unique().tolist()),
        "k_shots": sorted(views["k_shot"].astype(int).unique().tolist()),
        "seeds": sorted(views["seed"].astype(int).unique().tolist()),
        "corruptions": sorted(views["corruption"].astype(str).unique().tolist()),
    }
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--views", required=True)
    parser.add_argument("--support-stats", required=True)
    parser.add_argument("--support-manifest", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--expected-k-shots", nargs="+", type=int, default=None)
    parser.add_argument("--expected-seeds", nargs="+", type=int, default=None)
    parser.add_argument("--expected-corruptions", nargs="+", default=None)
    args = parser.parse_args()
    summary = audit_frames(
        pd.read_csv(args.views), pd.read_csv(args.support_stats), pd.read_csv(args.support_manifest),
        args.expected_k_shots, args.expected_seeds, args.expected_corruptions,
    )
    output = Path(args.out)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0 if summary["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
