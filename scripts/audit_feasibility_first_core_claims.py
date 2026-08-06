"""Regenerate the numerical claims used by the feasibility-first manuscript.

The audit is CPU-only.  It consumes the committed strict-CRESS outputs and the
paper-facing asymmetric-LOIO summaries, checks the manuscript's key rounded
values, and emits a compact JSON record.  A failed assertion means that the
paper text or table must not be released without reconciliation.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import math
import re
import statistics
from pathlib import Path

RUN_TAG = "nc_gpu_20260722_e7f1759"
JOB_LABELS = {
    "mvtec_within": "MVTec->MVTec",
    "visa_within": "VisA->VisA",
    "mvtec_to_visa": "MVTec->VisA",
    "mvtec_to_mpdd": "MVTec->MPDD",
}
EXPECTED_MIN_UCB = {
    "MVTec->MVTec": {"category": 0.950, "image": 0.039},
    "VisA->VisA": {"category": 1.000, "image": 0.042},
    "MVTec->VisA": {"category": 0.961, "image": 0.048},
    "MVTec->MPDD": {"category": 0.986, "image": 0.040},
}
EXPECTED_IMAGE_NONZERO = {
    "MVTec->MVTec": 0.367,
    "VisA->VisA": 0.603,
    "MVTec->VisA": 0.415,
    "MVTec->MPDD": 0.370,
}


def _rounded(value: float) -> float:
    return round(float(value), 3)


def _local_artifact_path(root: Path, recorded_path: str) -> Path:
    normalized = recorded_path.replace("\\", "/")
    for marker in ("outputs/", "configs/", "handoff/"):
        offset = normalized.find(marker)
        if offset >= 0:
            return root / normalized[offset:]
    raise AssertionError(f"Cannot map recorded artifact path into repository: {recorded_path}")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def reproducibility_lineage(root: Path) -> dict:
    manifest_path = (
        root
        / "outputs"
        / "submission_cpu"
        / f"cpu_pipeline_manifest_{RUN_TAG}.json"
    )
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("run_tag") != RUN_TAG:
        raise AssertionError(f"Run-tag mismatch in CPU manifest: {manifest.get('run_tag')}")

    expected_cells = {"mvtec": 1500, "visa": 1200, "mpdd": 600}
    audit_summary = {}
    for dataset, expected in expected_cells.items():
        audit = manifest["artifact_audits"][dataset]
        if audit["status"] != "pass" or audit["issues"] or audit["n_view_cells"] != expected:
            raise AssertionError(f"Artifact-audit mismatch for {dataset}: {audit}")
        audit_summary[dataset] = {
            "status": audit["status"],
            "n_view_cells": int(audit["n_view_cells"]),
            "n_view_rows": int(audit["n_view_rows"]),
        }

    verified_inputs = {}
    for label, entry in manifest["inputs"].items():
        path = _local_artifact_path(root, entry["path"])
        if not path.is_file():
            raise AssertionError(f"Missing manifest input {label}: {path}")
        observed = _sha256(path)
        if observed != entry["sha256"]:
            raise AssertionError(
                f"Input checksum mismatch for {label}: {observed} != {entry['sha256']}"
            )
        verified_inputs[label] = entry["sha256"]

    primary_outputs = [
        name
        for name in manifest["outputs"]
        if "__primary__" in name
        and (
            name.endswith("_candidates.csv")
            or name.endswith("_detailed.csv")
            or name.endswith("_partitions.json")
        )
    ]
    gate_name = f"nested_sc3r_{RUN_TAG}_empirical_gate.json"
    if gate_name not in manifest["outputs"]:
        raise AssertionError(f"Empirical gate is absent from manifest: {gate_name}")
    critical_outputs = primary_outputs + [gate_name]
    if len(primary_outputs) != 16 * 3:
        raise AssertionError(f"Expected 48 primary output artifacts, found {len(primary_outputs)}")
    for name in critical_outputs:
        entry = manifest["outputs"][name]
        path = _local_artifact_path(root, entry["path"])
        if not path.is_file():
            raise AssertionError(f"Missing critical CPU output: {path}")
        observed = _sha256(path)
        if observed != entry["sha256"]:
            raise AssertionError(
                f"Critical-output checksum mismatch for {name}: "
                f"{observed} != {entry['sha256']}"
            )

    run_report = (
        root / "handoff" / RUN_TAG / "GPU_RUN_REPORT.md"
    ).read_text(encoding="utf-8")
    expected_lineage = {
        "declared_protocol_commit": "e7f175990b02aa3cbdb7c92250d57c0272abef9d",
        "source_tree_sha256": "fd85b105a21d0b9fce4377f915a97a330661893f5dbb97846373bbe99520dd65",
        "weight_sha256": "b938bf1bc15cd2ec0feacfe3a1bb553fe8ea9ca46a7e1d8d00217f29aef60cd9",
    }
    if not all(value in run_report for value in expected_lineage.values()):
        raise AssertionError("GPU run report is missing declared lineage identifiers")
    recorded_git = manifest["environment"]["git"]
    if recorded_git != {
        "commit": "07d803154f44584eb03efc16a1057e1eb0341fc3",
        "dirty": True,
    }:
        raise AssertionError(f"Unexpected recorded CPU-manifest worktree state: {recorded_git}")

    return {
        "artifact_audits": audit_summary,
        "verified_manifest_inputs": len(verified_inputs),
        "verified_primary_and_gate_outputs": len(critical_outputs),
        "declared_lineage": expected_lineage,
        "recorded_cpu_manifest_git_state": recorded_git,
        "interpretation": (
            "The protocol revision and content hashes identify the scientific lineage; "
            "the post-checkpoint CPU manifest also retains its dirty-worktree warning."
        ),
    }


def _job_from_candidate(frame: pd.DataFrame) -> str:
    dataset = str(frame.dataset.iloc[0])
    source = str(frame.source_dataset.iloc[0])
    if dataset == source == "mvtec":
        return "MVTec->MVTec"
    if dataset == source == "visa":
        return "VisA->VisA"
    if source == "mvtec" and dataset == "visa":
        return "MVTec->VisA"
    if source == "mvtec" and dataset == "mpdd":
        return "MVTec->MPDD"
    raise ValueError(f"Unexpected source/target pair: {source}->{dataset}")


def theory_counts(delta: float = 0.05, levels: int = 3) -> dict:
    result: dict[str, dict[str, list[int]]] = {"distribution_free": {}, "hoeffding": {}}
    alphas = (0.20, 0.10, 0.05)
    result["distribution_free"]["no_multiplicity"] = [
        math.ceil(math.log(delta) / math.log(1.0 - alpha)) for alpha in alphas
    ]
    for candidates in (1, 5, 20):
        beta = delta / (2 * levels * candidates)
        result["distribution_free"][f"M={candidates}"] = [
            math.ceil(math.log(beta) / math.log(1.0 - alpha)) for alpha in alphas
        ]
        result["hoeffding"][f"M={candidates}"] = [
            math.ceil(math.log(2 * levels * candidates / delta) / (2 * alpha**2))
            for alpha in alphas
        ]
    expected = {
        "distribution_free": {
            "no_multiplicity": [14, 29, 59],
            "M=1": [22, 46, 94],
            "M=5": [29, 61, 125],
            "M=20": [35, 74, 152],
        },
        "hoeffding": {
            "M=1": [60, 240, 958],
            "M=5": [80, 320, 1280],
            "M=20": [98, 390, 1557],
        },
    }
    if result != expected:
        raise AssertionError(f"Theory-count mismatch: {result} != {expected}")
    result["available_budget_interpretation"] = {
        "alpha_0.20_max_confidence_n3": 1.0 - (1.0 - 0.20) ** 3,
        "alpha_0.20_max_confidence_n4": 1.0 - (1.0 - 0.20) ** 4,
        "confidence_0.95_ucb_floor_n3": 1.0 - delta ** (1.0 / 3.0),
        "confidence_0.95_ucb_floor_n4": 1.0 - delta ** (1.0 / 4.0),
    }
    expected_budget = (0.488, 0.590, 0.632, 0.527)
    observed_budget = tuple(
        _rounded(value) for value in result["available_budget_interpretation"].values()
    )
    if observed_budget != expected_budget:
        raise AssertionError(f"Available-category interpretation mismatch: {observed_budget}")
    source_pools = {
        "MVTec within": 14,
        "VisA within": 11,
        "MVTec transfer": 15,
    }
    result["max_certification_with_nonempty_reference_and_proposal"] = {
        name: count - 2 for name, count in source_pools.items()
    }
    if result["max_certification_with_nonempty_reference_and_proposal"] != {
        "MVTec within": 12,
        "VisA within": 9,
        "MVTec transfer": 13,
    }:
        raise AssertionError("Disjoint-role category-budget mismatch")
    if not all(
        count < expected["distribution_free"]["no_multiplicity"][0]
        for count in result["max_certification_with_nonempty_reference_and_proposal"].values()
    ):
        raise AssertionError("A current source pool unexpectedly reaches the 14-category limit")
    return result


def target_only(root: Path) -> dict:
    table_dir = root / "outputs" / "paper_tables"
    cells = pd.read_csv(table_dir / "target_only_asymmetric_nested5_cells.csv")
    aggregate = pd.read_csv(table_dir / "target_only_asymmetric_nested5_aggregate.csv")
    categories = pd.read_csv(table_dir / "target_only_asymmetric_nested5_category_cells.csv")
    cdf = pd.read_csv(table_dir / "target_only_asymmetric_nested5_cdf.csv")

    expected_cells = {
        ("mvtec", 4, "blur"): (0.219, 0.880, 0.904),
        ("mvtec", 4, "brightness_contrast"): (0.214, 0.882, 0.906),
        ("mvtec", 4, "gaussian_noise"): (0.341, 0.873, 0.857),
        ("mvtec", 4, "jpeg"): (0.336, 0.883, 0.860),
        ("mvtec", 8, "blur"): (0.139, 0.870, 0.936),
        ("mvtec", 8, "brightness_contrast"): (0.133, 0.870, 0.939),
        ("mvtec", 8, "gaussian_noise"): (0.281, 0.860, 0.878),
        ("mvtec", 8, "jpeg"): (0.248, 0.872, 0.892),
        ("visa", 4, "blur"): (0.144, 0.606, 0.825),
        ("visa", 4, "brightness_contrast"): (0.146, 0.596, 0.821),
        ("visa", 4, "gaussian_noise"): (0.133, 0.575, 0.829),
        ("visa", 4, "jpeg"): (0.145, 0.602, 0.822),
        ("visa", 8, "blur"): (0.094, 0.566, 0.870),
        ("visa", 8, "brightness_contrast"): (0.098, 0.557, 0.864),
        ("visa", 8, "gaussian_noise"): (0.081, 0.538, 0.881),
        ("visa", 8, "jpeg"): (0.104, 0.559, 0.858),
    }
    observed_cells = {
        (row.dataset, int(row.k_shot), row.corruption): tuple(
            _rounded(value)
            for value in (row.false_alarm_rate, row.detection_rate, row.precision)
        )
        for row in cells.itertuples(index=False)
    }
    if observed_cells != expected_cells:
        raise AssertionError(f"Target-only corruption-table mismatch: {observed_cells}")

    expected_aggregate = {
        ("mvtec", 4): (0.278, 0.880),
        ("mvtec", 8): (0.200, 0.868),
        ("visa", 4): (0.142, 0.595),
        ("visa", 8): (0.094, 0.555),
    }
    observed_aggregate = {
        (row.dataset, int(row.k_shot)): (
            _rounded(row.false_alarm_rate),
            _rounded(row.detection_rate),
        )
        for row in aggregate.itertuples(index=False)
    }
    if observed_aggregate != expected_aggregate:
        raise AssertionError(f"Target-only aggregate-table mismatch: {observed_aggregate}")

    headline = cells[
        (cells.dataset == "mvtec")
        & (cells.k_shot == 4)
        & (cells.corruption == "gaussian_noise")
    ].iloc[0]
    class_headline = categories[
        (categories.dataset == "mvtec")
        & (categories.k_shot == 4)
        & (categories.corruption == "gaussian_noise")
    ].false_alarm_rate
    if int(cells.false_alarm_rate.idxmax()) != int(headline.name):
        raise AssertionError("The declared Gaussian MVTec k=4 headline is not the grid maximum")

    cdf_headline = cdf[
        (cdf.dataset == "mvtec")
        & (cdf.k_shot == 4)
        & (cdf.corruption == "gaussian_noise")
    ].set_index("nominal_cdf")
    visa_k4_at_point_six = cdf[
        (cdf.dataset == "visa")
        & (cdf.k_shot == 4)
        & (cdf.nominal_cdf == 0.6)
    ]
    matched = pd.read_csv(
        table_dir / f"matched_loio_views_mvtec_{RUN_TAG}.csv"
    )
    matched = matched[(matched.k_shot == 4) & matched.corruption.eq("clean")]
    matched_summary = {}
    for label, column in {
        "asymmetric": "image_p_loio_legacy",
        "fold_matched": "image_p_loio",
    }.items():
        alarm = matched[column].le(0.20 + 1e-6)
        matched_summary[label] = {
            "far": float(alarm[matched.label.eq(0)].mean()),
            "power": float(alarm[matched.label.eq(1)].mean()),
        }
    summary = {
        "corruption_cells": {
            f"{dataset}/k={k}/{corruption}": {
                "far": values[0],
                "detection": values[1],
                "precision": values[2],
            }
            for (dataset, k, corruption), values in observed_cells.items()
        },
        "headline_far": float(headline.false_alarm_rate),
        "headline_detection": float(headline.detection_rate),
        "headline_precision": float(headline.precision),
        "category_median_far": float(class_headline.median()),
        "category_q25_far": float(class_headline.quantile(0.25)),
        "category_q75_far": float(class_headline.quantile(0.75)),
        "categories_above_nominal": int((class_headline > 0.20).sum()),
        "n_categories": int(class_headline.size),
        "cdf_gaussian_mvtec_k4": {
            "at_0.2": float(cdf_headline.loc[0.2, "gap"]),
            "at_0.4": float(cdf_headline.loc[0.4, "gap"]),
        },
        "visa_k4_gap_at_0.6": float(visa_k4_at_point_six.gap.min()),
        "matched_loio_sensitivity": matched_summary,
        "four_corruption_aggregate": {
            f"{row.dataset}_k{int(row.k_shot)}": {
                "far": float(row.false_alarm_rate),
                "detection": float(row.detection_rate),
            }
            for row in aggregate.itertuples(index=False)
        },
    }
    checks = {
        "headline": _rounded(summary["headline_far"]) == 0.341,
        "median": _rounded(summary["category_median_far"]) == 0.215,
        "q25": _rounded(summary["category_q25_far"]) == 0.169,
        "q75": _rounded(summary["category_q75_far"]) == 0.481,
        "exceeding_categories": summary["categories_above_nominal"] == 9,
        "category_count": summary["n_categories"] == 15,
        "cdf_at_0.2": _rounded(summary["cdf_gaussian_mvtec_k4"]["at_0.2"]) == 0.141,
        "cdf_at_0.4": _rounded(summary["cdf_gaussian_mvtec_k4"]["at_0.4"]) == 0.204,
        "visa_gap_at_0.6": _rounded(summary["visa_k4_gap_at_0.6"]) == -0.087,
        "asymmetric_clean_sensitivity": (
            _rounded(matched_summary["asymmetric"]["far"]) == 0.212
            and _rounded(matched_summary["asymmetric"]["power"]) == 0.880
        ),
        "fold_matched_clean_sensitivity": (
            _rounded(matched_summary["fold_matched"]["far"]) == 0.257
            and _rounded(matched_summary["fold_matched"]["power"]) == 0.906
        ),
    }
    if not all(checks.values()):
        raise AssertionError(f"Target-only manuscript claim mismatch: {checks}; {summary}")
    summary["checks"] = checks
    return summary


def _run_records(
    root: Path,
    *,
    prefix: str,
    dataset: str,
    model: str,
    include_dataset_in_name: bool = True,
) -> dict[tuple[str, int, int], dict[str, float]]:
    """Read immutable per-run metric notes without relying on deleted summary CSVs."""
    filename_prefix = f"{prefix}_{dataset}" if include_dataset_in_name else prefix
    pattern = re.compile(
        rf"^{re.escape(filename_prefix)}_(.+)_k(1|2|4|8)_seed([0-4])_"
        rf"{re.escape(model)}_k\2_seed\3_normal_synthetic\.md$"
    )
    records: dict[tuple[str, int, int], dict[str, float]] = {}
    metric_pattern = re.compile(r"^- `([^`]+)`: `([^`]+)`$", re.MULTILINE)
    for path in (root / "docs" / "experiments").glob("*.md"):
        match = pattern.match(path.name)
        if match is None:
            continue
        metrics: dict[str, float] = {}
        for name, raw_value in metric_pattern.findall(path.read_text(encoding="utf-8")):
            try:
                metrics[name] = float(raw_value)
            except ValueError:
                continue
        required = {"auroc", "ap", "model_storage_mb", "support_patch_count"}
        if not required.issubset(metrics):
            raise AssertionError(f"Incomplete clean-run record: {path}")
        key = (match.group(1), int(match.group(2)), int(match.group(3)))
        if key in records:
            raise AssertionError(f"Duplicate clean-run record for {prefix}/{dataset}/{key}")
        records[key] = metrics
    return records


def clean_ranking_and_storage(root: Path) -> dict:
    """Rebuild the controlled clean table from class-by-seed run records.

    The local ``subspacead`` configuration is the pure PCA-residual scorer used
    for the PCA64 row; it is not treated as an official SubspaceAD reproduction.
    PCA128 run records use the same raw PCA residual score, while their auxiliary
    calibration head is excluded from the explicitly defined ranker-state count.
    """
    nn = {
        dataset: _run_records(
            root,
            prefix="patchcore",
            dataset=dataset,
            model="patchcore",
        )
        for dataset in ("mvtec", "visa")
    }
    local_nn_alias = {
        dataset: _run_records(
            root,
            prefix="anomalydino",
            dataset=dataset,
            model="anomalydino",
        )
        for dataset in ("mvtec", "visa")
    }
    pca64 = {
        dataset: _run_records(
            root,
            prefix="subspacead",
            dataset=dataset,
            model="subspacead",
        )
        for dataset in ("mvtec", "visa")
    }
    pca128 = {
        "visa": _run_records(
            root,
            prefix="p2_visa_pca128",
            dataset="visa",
            model="calib_subspace_head",
            include_dataset_in_name=False,
        )
    }

    expected_counts = {
        "mvtec": 15 * 4 * 5,
        "visa": 12 * 4 * 5,
    }
    for dataset, expected in expected_counts.items():
        for label, records in {
            "controlled_nn": nn[dataset],
            "local_nn_alias": local_nn_alias[dataset],
            "pca64": pca64[dataset],
        }.items():
            if len(records) != expected:
                raise AssertionError(
                    f"Clean-run coverage mismatch for {dataset}/{label}: "
                    f"{len(records)} != {expected}"
                )
        if nn[dataset].keys() != local_nn_alias[dataset].keys():
            raise AssertionError(f"Controlled-NN cell mismatch for {dataset}")
        for key in nn[dataset]:
            for metric in ("auroc", "ap", "model_storage_mb"):
                if not math.isclose(
                    nn[dataset][key][metric],
                    local_nn_alias[dataset][key][metric],
                    rel_tol=0.0,
                    abs_tol=1e-12,
                ):
                    raise AssertionError(
                        f"Local NN aliases differ for {dataset}/{key}/{metric}"
                    )
    if len(pca128["visa"]) != expected_counts["visa"]:
        raise AssertionError(
            f"PCA128 VisA coverage mismatch: {len(pca128['visa'])}"
        )

    def summarize(records: dict, k: int) -> dict[str, float | int]:
        selected = [metrics for (_, shot, _), metrics in records.items() if shot == k]
        return {
            "n_class_seed_cells": len(selected),
            "auroc": statistics.fmean(row["auroc"] for row in selected),
            "ap": statistics.fmean(row["ap"] for row in selected),
            "logged_storage_mib": statistics.fmean(
                row["model_storage_mb"] for row in selected
            ),
        }

    summaries: dict[str, dict[str, dict[str, float | int]]] = {}
    for dataset in ("mvtec", "visa"):
        summaries[dataset] = {}
        for method, records in (("controlled_nn", nn[dataset]), ("pca64", pca64[dataset])):
            summaries[dataset][method] = {
                f"k={k}": summarize(records, k) for k in (1, 4, 8)
            }
        if dataset == "visa":
            summaries[dataset]["pca128"] = {
                f"k={k}": summarize(pca128[dataset], k) for k in (1, 4, 8)
            }

    expected_rounded = {
        ("mvtec", "controlled_nn", 1): (0.914, 0.952),
        ("mvtec", "controlled_nn", 4): (0.942, 0.967),
        ("mvtec", "controlled_nn", 8): (0.948, 0.970),
        ("mvtec", "pca64", 1): (0.904, 0.951),
        ("mvtec", "pca64", 4): (0.937, 0.967),
        ("mvtec", "pca64", 8): (0.945, 0.972),
        ("visa", "controlled_nn", 1): (0.804, 0.809),
        ("visa", "controlled_nn", 4): (0.862, 0.861),
        ("visa", "controlled_nn", 8): (0.873, 0.870),
        ("visa", "pca64", 1): (0.823, 0.834),
        ("visa", "pca64", 4): (0.870, 0.883),
        ("visa", "pca64", 8): (0.882, 0.894),
        ("visa", "pca128", 1): (0.834, 0.842),
        ("visa", "pca128", 4): (0.885, 0.895),
        ("visa", "pca128", 8): (0.897, 0.905),
    }
    for (dataset, method, k), expected in expected_rounded.items():
        observed = summaries[dataset][method][f"k={k}"]
        rounded = (_rounded(observed["auroc"]), _rounded(observed["ap"]))
        if rounded != expected:
            raise AssertionError(
                f"Clean table mismatch for {dataset}/{method}/k={k}: "
                f"{rounded} != {expected}"
            )

    d = 384
    bytes_per_float = 4
    analytic_storage = {
        "pca64_mib": (64 + 1) * d * bytes_per_float / 2**20,
        "pca128_mib": (128 + 1) * d * bytes_per_float / 2**20,
        "nn_k1_mib": 1369 * d * bytes_per_float / 2**20,
        "nn_capped_mib": 4096 * d * bytes_per_float / 2**20,
    }
    pca128_wrapper_auxiliary_bytes = (
        (d * 256 + 256 + 256 + 1) * bytes_per_float
        + 4 * bytes_per_float
    )
    pca128_historical_wrapper_mib = (
        analytic_storage["pca128_mib"]
        + pca128_wrapper_auxiliary_bytes / 2**20
    )
    expected_storage = (0.095, 0.189, 2.005, 6.000)
    if tuple(_rounded(value) for value in analytic_storage.values()) != expected_storage:
        raise AssertionError(f"Analytic storage mismatch: {analytic_storage}")
    for dataset in ("mvtec", "visa"):
        for k, key in ((1, "nn_k1_mib"), (4, "nn_capped_mib"), (8, "nn_capped_mib")):
            observed = summaries[dataset]["controlled_nn"][f"k={k}"]["logged_storage_mib"]
            if not math.isclose(observed, analytic_storage[key], rel_tol=0.0, abs_tol=1e-9):
                raise AssertionError(f"NN storage mismatch for {dataset}/k={k}: {observed}")
        for k in (1, 4, 8):
            observed = summaries[dataset]["pca64"][f"k={k}"]["logged_storage_mib"]
            if not math.isclose(
                observed, analytic_storage["pca64_mib"], rel_tol=0.0, abs_tol=1e-9
            ):
                raise AssertionError(f"PCA64 storage mismatch for {dataset}/k={k}: {observed}")
    for k in (1, 4, 8):
        observed = summaries["visa"]["pca128"][f"k={k}"]["logged_storage_mib"]
        if not math.isclose(
            observed, pca128_historical_wrapper_mib, rel_tol=0.0, abs_tol=1e-9
        ):
            raise AssertionError(
                f"PCA128 historical-wrapper storage mismatch for VisA/k={k}: {observed}"
            )

    return {
        "coverage": expected_counts,
        "summaries": summaries,
        "analytic_ranker_storage_mib": analytic_storage,
        "pca128_historical_wrapper_storage_mib": pca128_historical_wrapper_mib,
        "provenance_note": (
            "PCA64 uses the pure local PCA-residual run records; local PatchCore and "
            "AnomalyDINO aliases are verified numerically identical and are reported "
            "only as one controlled DINOv2 NN baseline. PCA128 records were produced "
            "by a historical wrapper whose raw ranking path is PCA-residual-only; the "
            "paper reports the 0.189 MiB state required by that ranker and excludes "
            "the wrapper's unused probability-calibration components (historical total "
            "0.566 MiB)."
        ),
    }


def strict_cress(root: Path) -> dict:
    pattern = str(
        root
        / "outputs"
        / "submission_cpu"
        / f"nested_sc3r_{RUN_TAG}__*__primary__*_detailed.csv"
    )
    detailed_files = sorted(glob.glob(pattern))
    candidate_files = sorted(path.replace("_detailed.csv", "_candidates.csv") for path in detailed_files)
    if len(detailed_files) != 16 or not all(Path(path).exists() for path in candidate_files):
        raise AssertionError(
            f"Expected 16 primary detailed/candidate pairs, found {len(detailed_files)}"
        )

    detailed = pd.concat([pd.read_csv(path) for path in detailed_files], ignore_index=True)
    nested = detailed[detailed.method.eq("nested_sc3r")].copy()
    nested["job"] = nested.job_id.map(JOB_LABELS)
    if nested.job.isna().any():
        raise AssertionError("Unknown strict-CRESS job identifier")

    nonzero = nested.groupby(["job", "unit"]).selected_threshold.agg(
        rows="size", fraction=lambda values: float((values > 0).mean())
    )
    category_nonzero = {
        job: float(nonzero.loc[(job, "class"), "fraction"]) for job in JOB_LABELS.values()
    }
    image_nonzero = {
        job: float(nonzero.loc[(job, "image"), "fraction"]) for job in JOB_LABELS.values()
    }
    if any(value != 0.0 for value in category_nonzero.values()):
        raise AssertionError(f"A category-certified threshold is unexpectedly nonzero: {category_nonzero}")
    category_nonzero_without_k1 = float(
        (nested[nested.unit.eq("class") & nested.k_shot.gt(1)].selected_threshold > 0).mean()
    )
    if category_nonzero_without_k1 != 0.0:
        raise AssertionError(
            "The category-level zero-threshold result unexpectedly depends on k=1 cells"
        )
    for job, expected in EXPECTED_IMAGE_NONZERO.items():
        if _rounded(image_nonzero[job]) != expected:
            raise AssertionError(
                f"Image-unit nonzero fraction mismatch for {job}: {image_nonzero[job]}"
            )

    candidate_parts = []
    for path in candidate_files:
        frame = pd.read_csv(path)
        frame["job"] = _job_from_candidate(frame)
        candidate_parts.append(frame)
    candidates = pd.concat(candidate_parts, ignore_index=True)
    candidates["unit_label"] = candidates.unit.replace({"cluster": "category"})
    candidate_summary = candidates.groupby(["job", "unit_label"]).agg(
        min_ucb=("candidate_upper_bound", "min"),
        min_units=("candidate_n_units", "min"),
        max_units=("candidate_n_units", "max"),
    )
    for job, units in EXPECTED_MIN_UCB.items():
        for unit, expected in units.items():
            observed = float(candidate_summary.loc[(job, unit), "min_ucb"])
            if _rounded(observed) != expected:
                raise AssertionError(f"Minimum UCB mismatch for {job}/{unit}: {observed}")

    matched = detailed[
        detailed.source_mode.eq("matched_condition")
        & detailed.method.eq("pooled_source_conformal")
        & detailed.unit.eq("image")
    ].copy()
    matched["job"] = matched.job_id.map(JOB_LABELS)
    pooled = matched.groupby(["job", "alpha"])[["false_alarm_rate", "power"]].mean()

    gate_path = (
        root
        / "outputs"
        / "submission_cpu"
        / f"nested_sc3r_{RUN_TAG}_empirical_gate.json"
    )
    gate = json.loads(gate_path.read_text(encoding="utf-8"))
    if gate["n_gate_cells"] != 960 or gate["n_empirical_fail"] != 960:
        raise AssertionError(f"Frozen gate-count mismatch: {gate}")

    return {
        "primary_file_pairs": len(detailed_files),
        "gate_configurations": gate["n_gate_cells"],
        "failed_gate_configurations": gate["n_empirical_fail"],
        "category_nonzero_fraction": category_nonzero,
        "category_nonzero_fraction_excluding_k1": category_nonzero_without_k1,
        "image_nonzero_fraction": image_nonzero,
        "candidate_summary": {
            f"{job}/{unit}": {
                "min_ucb": float(row.min_ucb),
                "min_units": int(row.min_units),
                "max_units": int(row.max_units),
            }
            for (job, unit), row in candidate_summary.iterrows()
        },
        "pooled_matched_condition": {
            f"{job}/alpha={alpha:.2f}": {
                "far": float(row.false_alarm_rate),
                "power": float(row.power),
            }
            for (job, alpha), row in pooled.iterrows()
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--output")
    parser.add_argument(
        "--theory-only",
        action="store_true",
        help="run the dependency-free feasibility calculations without loading empirical tables",
    )
    args = parser.parse_args()
    root = Path(args.root).resolve()
    report = {"status": "pass", "theory_counts": theory_counts()}
    if not args.theory_only:
        global np, pd
        import numpy as np
        import pandas as pd

        report["reproducibility_lineage"] = reproducibility_lineage(root)
        report["target_only"] = target_only(root)
        report["clean_ranking_and_storage"] = clean_ranking_and_storage(root)
        report["strict_cress"] = strict_cress(root)
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
        print(output)
    else:
        print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
