"""Strict nested SC3R analysis on precomputed per-image score views.

This script is CPU-only. Feature extraction remains the GPU stage; this stage
must consume its immutable CSV artifacts and writes the exact class partitions,
candidate certificates, and target operating metrics.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import time

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.conformal import conformal_p_values
from src.evaluation.sc3r_certification import (
    ThresholdCertificate,
    certify_thresholds,
    partition_source_classes,
    proposal_candidates,
)


SOURCE_MODES = (
    "matched_condition",
    "clean_source",
    "condition_agnostic",
    "mismatched_condition",
)


def normalize_support_scores(frame: pd.DataFrame, mode: str) -> pd.Series:
    """Apply a frozen per-class normalization using support-only statistics."""
    if "raw_score" not in frame:
        raise ValueError("raw_score is required for score normalization")
    raw = frame.raw_score.to_numpy(dtype=np.float64)
    if mode == "none":
        return pd.Series(raw, index=frame.index)
    if mode == "median_mad":
        required = {"support_cal_median", "support_cal_mad"}
        scale_column = "support_cal_mad"
    elif mode == "median_iqr":
        required = {"support_cal_median", "support_cal_q25", "support_cal_q75"}
        scale_column = None
    else:
        raise ValueError("normalization mode must be none, median_mad, or median_iqr")
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"Missing support statistics for {mode}: {missing}")
    center = frame.support_cal_median.to_numpy(dtype=np.float64)
    if scale_column is None:
        scale = (
            frame.support_cal_q75.to_numpy(dtype=np.float64)
            - frame.support_cal_q25.to_numpy(dtype=np.float64)
        )
    else:
        scale = frame[scale_column].to_numpy(dtype=np.float64)
    if not np.all(np.isfinite(center)) or not np.all(np.isfinite(scale)):
        raise ValueError(f"Non-finite support statistics for {mode}")
    return pd.Series((raw - center) / np.maximum(scale, 1e-6), index=frame.index)


def _stable_rank(value: str, namespace: str) -> bytes:
    return hashlib.sha256(f"{namespace}|{value}".encode("utf-8")).digest()


def _limit_source_pool(
    source: pd.DataFrame,
    target_class: str,
    seed: int,
    source_mode: str,
    class_limit: int | None,
    images_per_class: int | None,
) -> pd.DataFrame:
    """Deterministically limit source resources without reading target metrics."""
    result = source.copy()
    classes = sorted(result["class"].astype(str).unique().tolist())
    if class_limit is not None:
        if class_limit < 6:
            raise ValueError("source_class_limit must be at least 6 for the three-way nested split")
        namespace = f"source-class-limit|{target_class}|{seed}|{source_mode}"
        selected = sorted(classes, key=lambda value: _stable_rank(value, namespace))[:class_limit]
        result = result[result["class"].astype(str).isin(selected)].copy()
    if images_per_class is not None:
        if images_per_class < 1:
            raise ValueError("source_images_per_class must be positive")
        if "base_image_path" not in result:
            raise ValueError("source_images_per_class requires base_image_path for deterministic identity")
        if result.base_image_path.isna().any():
            raise ValueError("source_images_per_class found missing base_image_path values")
        pieces = []
        for cls, group in result.groupby("class", sort=True):
            namespace = f"source-image-limit|{target_class}|{seed}|{source_mode}|{cls}"
            ordered = group.assign(
                _stable_order=group.base_image_path.astype(str).map(
                    lambda value: _stable_rank(value, namespace).hex()
                )
            ).sort_values(["_stable_order", "base_image_path"])
            pieces.append(ordered.head(images_per_class).drop(columns="_stable_order"))
        result = pd.concat(pieces, ignore_index=True) if pieces else result.iloc[0:0].copy()
    return result


def _select_source_pool(
    frame: pd.DataFrame,
    pool_dataset: str,
    target_class: str,
    k_shot: int,
    seed: int,
    target_corruption: str,
    source_mode: str,
) -> tuple[pd.DataFrame, str]:
    """Select source normals without inspecting target labels or scores.

    ``condition_agnostic`` is the deployment-facing blind/pooled rule: it takes
    the median normalized score across available condition views of each base
    image, so repeated corruptions never inflate the source sample size.
    ``mismatched_condition`` is a deterministic negative-control rule using the
    lexicographic successor of the target condition.
    """
    if source_mode not in SOURCE_MODES:
        raise ValueError(f"Unknown source_mode={source_mode!r}; expected one of {SOURCE_MODES}")
    eligible = frame[
        (frame.dataset == pool_dataset)
        & (frame["class"] != target_class)
        & (frame.k_shot == k_shot)
        & (frame.seed == seed)
        & (frame.label == 0)
    ].copy()
    conditions = sorted(eligible.corruption.astype(str).unique().tolist())
    if not conditions:
        raise ValueError("No eligible source-normal conditions")

    if source_mode == "matched_condition":
        source_condition = target_corruption
    elif source_mode == "clean_source":
        source_condition = "clean"
    elif source_mode == "mismatched_condition":
        alternatives = [condition for condition in conditions if condition != target_corruption]
        if not alternatives:
            raise ValueError("mismatched_condition requires at least two source conditions")
        if target_corruption in conditions:
            source_condition = conditions[(conditions.index(target_corruption) + 1) % len(conditions)]
        else:
            source_condition = alternatives[0]
    else:
        if "base_image_path" not in eligible.columns:
            raise ValueError("condition_agnostic requires base_image_path to collapse repeated views")
        if eligible.base_image_path.isna().any():
            raise ValueError("condition_agnostic found missing base_image_path values")
        collapsed = (
            eligible.groupby(["class", "base_image_path"], as_index=False, sort=True)
            ["support_normalized_score"]
            .median()
        )
        collapsed["corruption"] = "condition_agnostic_median"
        collapsed["label"] = 0
        return collapsed, "all_conditions_median_by_base_image"

    source = eligible[eligible.corruption.astype(str) == source_condition].copy()
    if source.empty:
        raise ValueError(f"No source normals for condition {source_condition!r}")
    return source, source_condition


def _certificate_rows(certificate: ThresholdCertificate, base: dict) -> list[dict]:
    return [
        {
            **base,
            "unit": certificate.unit,
            "bound_method": certificate.bound_method,
            "candidate_threshold": candidate.threshold,
            "candidate_empirical_loss": candidate.empirical_loss,
            "candidate_upper_bound": candidate.upper_bound,
            "candidate_n_units": candidate.n_units,
            "candidate_passes": candidate.passes,
            "selected_threshold": certificate.selected_threshold,
        }
        for candidate in certificate.candidates
    ]


def _operating_row(
    base: dict,
    method: str,
    unit: str,
    alpha: float,
    threshold: float,
    p_values: np.ndarray,
    labels: np.ndarray,
    counts: dict[str, int],
    delta: float | None = None,
) -> dict:
    alarms = p_values <= threshold
    normal = labels == 0
    anomaly = labels == 1
    return {
        **base,
        "method": method,
        "unit": unit,
        "alpha": alpha,
        "delta": delta,
        "selected_threshold": threshold,
        "false_alarm_rate": float(alarms[normal].mean()),
        "power": float(alarms[anomaly].mean()),
        "alarm_precision": float(labels[alarms].mean()) if alarms.any() else float("nan"),
        "auroc": float(roc_auc_score(labels, 1.0 - p_values)),
        "ap": float(average_precision_score(labels, 1.0 - p_values)),
        **counts,
    }


def evaluate_nested(
    frame: pd.DataFrame,
    alphas: list[float],
    delta: float,
    max_candidates: int,
    source_mode: str,
    source_dataset: str | None = None,
    target_dataset: str | None = None,
    support_residuals: pd.DataFrame | None = None,
    source_class_limit: int | None = None,
    source_images_per_class: int | None = None,
    normalization_mode: str = "median_mad",
    partition_allocation: tuple[float, float, float] = (0.5, 0.25, 0.25),
) -> tuple[pd.DataFrame, pd.DataFrame, list[dict]]:
    required = {"dataset", "class", "k_shot", "seed", "corruption", "label", "support_normalized_score"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise ValueError(f"Missing input columns: {missing}")
    results: list[dict] = []
    candidate_rows: list[dict] = []
    manifests: list[dict] = []
    residual_groups: dict[tuple, np.ndarray] = {}
    if support_residuals is not None:
        residual_required = {"dataset", "class", "k_shot", "seed", "loio_residual"}
        residual_missing = sorted(residual_required - set(support_residuals.columns))
        if residual_missing:
            raise ValueError(f"Missing support-residual columns: {residual_missing}")
        if "raw_score" not in frame.columns:
            raise ValueError("raw_score is required when support_residuals are supplied")
        residual_groups = {
            key: group.loio_residual.to_numpy(dtype=np.float64)
            for key, group in support_residuals.groupby(["dataset", "class", "k_shot", "seed"])
        }
    keys = ["dataset", "class", "k_shot", "seed", "corruption"]
    for key, target in frame.groupby(keys, sort=True):
        dataset, target_class, k_shot, seed, corruption = key
        if target_dataset is not None and dataset != target_dataset:
            continue
        if target.label.nunique() < 2:
            continue
        pool_dataset = source_dataset or dataset
        source, source_corruption = _select_source_pool(
            frame, pool_dataset, target_class, int(k_shot), int(seed), str(corruption), source_mode
        )
        source = _limit_source_pool(
            source, str(target_class), int(seed), source_mode,
            source_class_limit, source_images_per_class,
        )
        split = partition_source_classes(
            source["class"].unique().tolist(), target_class, int(seed), partition_allocation
        )
        subsets = {name: source[source["class"].isin(classes)] for name, classes in split.items()}
        if any(subset.empty for subset in subsets.values()):
            raise ValueError(f"Empty nested source subset for target cell {key}")
        score_col = "support_normalized_score"
        reference_scores = subsets["reference"][score_col].to_numpy(dtype=np.float64)
        proposal_p = conformal_p_values(reference_scores, subsets["proposal"][score_col].to_numpy(dtype=np.float64))
        certification_p = conformal_p_values(reference_scores, subsets["certification"][score_col].to_numpy(dtype=np.float64))
        candidates = proposal_candidates(proposal_p, max_candidates=max_candidates)
        target_p_start = time.perf_counter()
        target_p = conformal_p_values(reference_scores, target[score_col].to_numpy(dtype=np.float64))
        target_p_seconds = time.perf_counter() - target_p_start
        pooled_p_start = time.perf_counter()
        pooled_target_p = conformal_p_values(
            source[score_col].to_numpy(dtype=np.float64), target[score_col].to_numpy(dtype=np.float64)
        )
        pooled_p_seconds = time.perf_counter() - pooled_p_start
        labels = target.label.to_numpy(dtype=np.int64)
        base = {
            "dataset": dataset,
            "source_dataset": pool_dataset,
            "target_class": target_class,
            "k_shot": int(k_shot),
            "seed": int(seed),
            "corruption": corruption,
            "source_corruption": source_corruption,
            "source_mode": source_mode,
            "normalization_mode": normalization_mode,
            "source_class_limit": source_class_limit,
            "source_images_per_class_limit": source_images_per_class,
            "n_source_classes": int(source["class"].nunique()),
            "partition_allocation": "/".join(f"{value:.6g}" for value in partition_allocation),
        }
        manifests.append({**base, **{f"{name}_classes": list(classes) for name, classes in split.items()}})
        cluster_ids = subsets["certification"]["class"].astype(str).tolist()
        common_counts = {
            "n_reference_images": len(reference_scores),
            "n_proposal_images": len(proposal_p),
            "n_certification_images": len(certification_p),
            "n_source_pool_images": len(source),
            "target_pvalue_seconds_per_image": target_p_seconds / max(len(target), 1),
            "pooled_pvalue_seconds_per_image": pooled_p_seconds / max(len(target), 1),
        }
        target_only_p = None
        target_support = residual_groups.get((dataset, target_class, k_shot, seed))
        if target_support is not None:
            target_only_p = conformal_p_values(
                target_support, target.raw_score.to_numpy(dtype=np.float64)
            )
        certificate_delta = delta / (len(alphas) * 2.0)
        for alpha in alphas:
            for unit, unit_ids, bound_method in (
                ("image", None, "clopper_pearson"),
                ("class", cluster_ids, "hoeffding"),
            ):
                certification_start = time.perf_counter()
                certificate = certify_thresholds(
                    certification_p, candidates, alpha, certificate_delta,
                    unit_ids=unit_ids, bound_method=bound_method,
                )
                certification_seconds = time.perf_counter() - certification_start
                results.append(
                    _operating_row(
                        base, "nested_sc3r", unit, alpha, certificate.selected_threshold,
                        target_p, labels,
                        {**common_counts, "threshold_certification_seconds": certification_seconds,
                         "certificate_delta": certificate_delta,
                         "certificate_bound_method": bound_method},
                        delta,
                    )
                )
                results.append(
                    _operating_row(
                        base, "pooled_source_conformal", unit, alpha, alpha,
                        pooled_target_p, labels,
                        {**common_counts, "threshold_certification_seconds": 0.0,
                         "certificate_delta": certificate_delta,
                         "certificate_bound_method": "not_applicable"},
                    )
                )
                if target_only_p is not None:
                    results.append(
                        _operating_row(
                            base, "target_only", unit, alpha, alpha,
                            target_only_p, labels,
                            {**common_counts, "n_target_support_scores": len(target_support),
                             "threshold_certification_seconds": 0.0,
                             "certificate_delta": certificate_delta,
                             "certificate_bound_method": "not_applicable"},
                        )
                    )
                candidate_rows.extend(_certificate_rows(certificate, {
                    **base, "reported_unit": unit, "alpha": alpha,
                    "family_delta": delta, "certificate_delta": certificate_delta,
                }))
    return pd.DataFrame(results), pd.DataFrame(candidate_rows), manifests


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True)
    parser.add_argument("--support-stats", nargs="+", required=True)
    parser.add_argument("--support-residuals", nargs="+", default=None,
                        help="Optional LOIO residual CSVs; adds a paired target_only baseline.")
    parser.add_argument("--source-mode", choices=SOURCE_MODES, required=True)
    parser.add_argument("--source-dataset", default=None)
    parser.add_argument("--target-dataset", default=None)
    parser.add_argument("--alphas", nargs="+", type=float, default=[0.05, 0.10, 0.20])
    parser.add_argument("--delta", type=float, default=0.05)
    parser.add_argument("--max-candidates", type=int, default=20)
    parser.add_argument("--normalization", choices=["none", "median_mad", "median_iqr"], default="median_mad")
    parser.add_argument("--source-class-limit", type=int, default=None)
    parser.add_argument("--source-images-per-class", type=int, default=None)
    parser.add_argument("--partition-allocation", nargs=3, type=float, default=[0.5, 0.25, 0.25],
                        metavar=("REFERENCE", "PROPOSAL", "CERTIFICATION"))
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", required=True)
    args = parser.parse_args()

    frame = pd.concat([pd.read_csv(path) for path in args.inputs], ignore_index=True)
    stats = pd.concat([pd.read_csv(path) for path in args.support_stats], ignore_index=True)
    frame = frame.merge(stats, on=["dataset", "class", "k_shot", "seed"], how="left", validate="many_to_one")
    frame["support_normalized_score"] = normalize_support_scores(frame, args.normalization)
    results, candidates, manifests = evaluate_nested(
        frame,
        args.alphas,
        args.delta,
        args.max_candidates,
        args.source_mode,
        args.source_dataset,
        args.target_dataset,
        pd.concat([pd.read_csv(path) for path in args.support_residuals], ignore_index=True)
        if args.support_residuals else None,
        args.source_class_limit,
        args.source_images_per_class,
        args.normalization,
        tuple(args.partition_allocation),
    )
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    results.to_csv(out / f"nested_sc3r_{args.run_tag}_detailed.csv", index=False)
    candidates.to_csv(out / f"nested_sc3r_{args.run_tag}_candidates.csv", index=False)
    (out / f"nested_sc3r_{args.run_tag}_partitions.json").write_text(json.dumps(manifests, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {len(results)} result rows, {len(candidates)} candidate rows, and {len(manifests)} manifests")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
