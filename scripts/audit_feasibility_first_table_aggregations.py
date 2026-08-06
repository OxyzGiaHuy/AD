"""Dependency-free audit of the manuscript's strict-CRESS table aggregations.

The full numerical audit depends on NumPy and pandas.  This smaller audit uses
only the Python standard library so that the two easily confused denominators
remain checkable in a clean submission checkout:

* 960 is the number of job/mode/k/alpha/condition gate configurations;
* nonzero-threshold fractions are computed from target-category/seed cells
  underneath those configurations.

It also verifies that direct pooled-source conformal is averaged once per
target cell.  The raw evaluator writes identical bookkeeping copies for the
image and category certification units, which must not be double weighted.
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
from collections import defaultdict
from pathlib import Path


RUN_TAG = "nc_gpu_20260722_e7f1759"
JOB_INFO = {
    "mvtec_within": {"label": "MVTec->MVTec", "targets": 15, "cells": 18_000},
    "visa_within": {"label": "VisA->VisA", "targets": 12, "cells": 14_400},
    "mvtec_to_visa": {"label": "MVTec->VisA", "targets": 12, "cells": 14_400},
    "mvtec_to_mpdd": {"label": "MVTec->MPDD", "targets": 6, "cells": 7_200},
}
EXPECTED_POOLED = {
    ("mvtec_within", 0.05): (0.075, 0.404),
    ("mvtec_within", 0.10): (0.131, 0.566),
    ("mvtec_within", 0.20): (0.242, 0.754),
    ("visa_within", 0.05): (0.060, 0.320),
    ("visa_within", 0.10): (0.111, 0.466),
    ("visa_within", 0.20): (0.208, 0.639),
    ("mvtec_to_visa", 0.05): (0.028, 0.171),
    ("mvtec_to_visa", 0.10): (0.048, 0.282),
    ("mvtec_to_visa", 0.20): (0.099, 0.441),
    ("mvtec_to_mpdd", 0.05): (0.030, 0.186),
    ("mvtec_to_mpdd", 0.10): (0.066, 0.283),
    ("mvtec_to_mpdd", 0.20): (0.157, 0.423),
}


def rounded(value: float) -> float:
    return round(float(value), 3)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--manuscript", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    manuscript = args.manuscript.resolve()

    pattern = str(
        root
        / "outputs"
        / "submission_cpu"
        / f"nested_sc3r_{RUN_TAG}__*__primary__*_detailed.csv"
    )
    paths = sorted(glob.glob(pattern))
    if len(paths) != 16:
        raise AssertionError(f"Expected 16 primary detailed files, found {len(paths)}")

    nested_counts: dict[tuple[str, str], int] = defaultdict(int)
    nested_nonzero: dict[tuple[str, str], int] = defaultdict(int)
    configurations: dict[str, set[tuple[str, str, str, str]]] = defaultdict(set)
    configuration_cells: dict[tuple[str, str, str, str, str, str], int] = defaultdict(int)
    seen_nested: set[tuple[str, ...]] = set()
    pooled_by_unit: dict[tuple[str, ...], dict[str, tuple[float, float]]] = defaultdict(dict)
    pooled_values: dict[tuple[str, float], list[tuple[float, float]]] = defaultdict(list)

    for path in paths:
        with open(path, newline="", encoding="utf-8") as handle:
            for row in csv.DictReader(handle):
                job = row["job_id"]
                if job not in JOB_INFO:
                    raise AssertionError(f"Unexpected job identifier: {job}")
                if row["method"] == "nested_sc3r":
                    unit = row["unit"]
                    key = (
                        job,
                        row["source_mode"],
                        row["k_shot"],
                        row["alpha"],
                        row["corruption"],
                        row["target_class"],
                        row["seed"],
                        unit,
                    )
                    if key in seen_nested:
                        raise AssertionError(f"Duplicate strict-CRESS target cell: {key}")
                    seen_nested.add(key)
                    nested_counts[(job, unit)] += 1
                    nested_nonzero[(job, unit)] += float(row["selected_threshold"]) > 0.0
                    config = (
                        row["source_mode"], row["k_shot"], row["alpha"], row["corruption"]
                    )
                    configurations[job].add(config)
                    configuration_cells[(job, *config, unit)] += 1

                if (
                    row["method"] == "pooled_source_conformal"
                    and row["source_mode"] == "matched_condition"
                ):
                    cell_key = (
                        job,
                        row["target_class"],
                        row["k_shot"],
                        row["seed"],
                        row["corruption"],
                        row["alpha"],
                    )
                    metrics = (float(row["false_alarm_rate"]), float(row["power"]))
                    pooled_by_unit[cell_key][row["unit"]] = metrics
                    if row["unit"] == "image":
                        pooled_values[(job, float(row["alpha"]))].append(metrics)

    checks: dict[str, bool] = {}
    denominator_report = {}
    for job, info in JOB_INFO.items():
        checks[f"{job}_has_240_configurations"] = len(configurations[job]) == 240
        expected_per_config = info["targets"] * 5
        for unit in ("class", "image"):
            observed = nested_counts[(job, unit)]
            checks[f"{job}_{unit}_underlying_cell_count"] = observed == info["cells"]
            checks[f"{job}_{unit}_configuration_width"] = all(
                configuration_cells[(job, *config, unit)] == expected_per_config
                for config in configurations[job]
            )
        checks[f"{job}_category_thresholds_all_zero"] = nested_nonzero[(job, "class")] == 0
        denominator_report[job] = {
            "gate_configurations": len(configurations[job]),
            "target_category_seed_cells_per_configuration": expected_per_config,
            "underlying_cells_per_unit": nested_counts[(job, "class")],
        }

    checks["total_gate_configurations_is_960"] = sum(
        len(value) for value in configurations.values()
    ) == 960
    checks["pooled_bookkeeping_units_are_identical"] = all(
        set(units) == {"class", "image"} and units["class"] == units["image"]
        for units in pooled_by_unit.values()
    )

    pooled_report = {}
    for key, expected in EXPECTED_POOLED.items():
        values = pooled_values[key]
        if not values:
            raise AssertionError(f"No pooled-source rows for {key}")
        observed = (
            sum(value[0] for value in values) / len(values),
            sum(value[1] for value in values) / len(values),
        )
        checks[f"pooled_{key[0]}_alpha_{key[1]:.2f}"] = tuple(
            rounded(value) for value in observed
        ) == expected
        pooled_report[f"{key[0]}/alpha={key[1]:.2f}"] = {
            "n_target_cells": len(values),
            "mean_far": observed[0],
            "mean_power": observed[1],
        }

    strict_tex = (manuscript / "tables" / "tab_strict_nested_sc3r.tex").read_text(
        encoding="utf-8"
    )
    pooled_tex = (manuscript / "tables" / "tab_pooled_source_conformal.tex").read_text(
        encoding="utf-8"
    )
    checks["strict_caption_declares_both_denominators"] = all(
        token in strict_tex
        for token in ("240 per source-to-target job", "18,000", "14,400", "7,200")
    )
    checks["pooled_caption_declares_unweighted_cell_mean"] = (
        "unweighted means of within-target-cell" in pooled_tex
    )

    report = {
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "denominators": denominator_report,
        "pooled_matched_condition": pooled_report,
        "interpretation": (
            "Gate configurations and their underlying target-category/seed cells are "
            "different denominators. Pooled-source means use one image-unit bookkeeping "
            "copy per target cell; the category-unit copy is verified identical and is not reweighted."
        ),
    }
    rendered = json.dumps(report, indent=2, sort_keys=True) + "\n"
    if args.output:
        output = args.output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(rendered, encoding="utf-8")
        print(output)
    else:
        print(rendered, end="")
    return 0 if report["status"] == "pass" else 1


if __name__ == "__main__":
    raise SystemExit(main())
