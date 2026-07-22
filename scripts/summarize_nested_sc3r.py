"""Aggregate strict nested-SC3R outputs without hiding failed cells.

All methods must be paired at the exact target cell. Zero selected thresholds
remain explicit in cell, summary, gate, and LaTeX outputs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

import numpy as np
import pandas as pd


METHODS = ("target_only", "pooled_source_conformal", "nested_sc3r")
MIN_NONZERO_THRESHOLD_RATE = 0.80
CELL_KEYS = (
    "job_id", "analysis_id", "dataset", "source_dataset", "target_class",
    "k_shot", "seed", "corruption", "source_mode", "normalization_mode",
    "unit", "alpha",
)
METRICS = ("selected_threshold", "false_alarm_rate", "power", "alarm_precision")


def paired_cell_audit(detailed: pd.DataFrame) -> pd.DataFrame:
    required = set(CELL_KEYS) | {"method", *METRICS}
    missing = sorted(required - set(detailed.columns))
    if missing:
        raise ValueError(f"Detailed nested output is missing columns: {missing}")
    relevant = detailed[detailed.method.isin(METHODS)].copy()
    duplicates = relevant.duplicated([*CELL_KEYS, "method"], keep=False)
    if duplicates.any():
        raise ValueError(f"Detailed nested output has {int(duplicates.sum())} duplicate paired-method rows")
    method_sets = relevant.groupby(list(CELL_KEYS), dropna=False).method.agg(lambda values: set(values))
    incomplete = method_sets[method_sets.map(lambda values: values != set(METHODS))]
    if not incomplete.empty:
        raise ValueError(f"{len(incomplete)} target cells do not contain exactly the required paired methods")

    pivot = relevant.pivot(index=list(CELL_KEYS), columns="method", values=list(METRICS))
    pivot.columns = [f"{metric}__{method}" for metric, method in pivot.columns]
    cells = pivot.reset_index()
    cells["alpha_floor"] = 1.0 / (cells.k_shot.astype(float) + 1.0)
    cells["below_target_floor"] = cells.alpha.astype(float) < cells.alpha_floor - 1e-12
    cells["nested_threshold_nonzero"] = cells.selected_threshold__nested_sc3r.astype(float) > 0.0
    cells["nested_empirical_far_budget_pass"] = (
        cells.false_alarm_rate__nested_sc3r.astype(float) <= cells.alpha.astype(float) + 0.02
    )
    cells["nested_no_harm"] = (
        cells.false_alarm_rate__nested_sc3r.astype(float)
        <= np.maximum(cells.alpha.astype(float), cells.false_alarm_rate__target_only.astype(float)) + 0.02
    )
    cells["nested_power_gain"] = cells.power__nested_sc3r - cells.power__target_only
    cells["pooled_power_gain"] = cells.power__pooled_source_conformal - cells.power__target_only
    return cells


def _aggregate(cells: pd.DataFrame, include_corruption: bool) -> pd.DataFrame:
    group_columns = [
        "job_id", "analysis_id", "dataset", "source_dataset", "k_shot",
        "source_mode", "normalization_mode", "unit", "alpha",
    ]
    if include_corruption:
        group_columns.insert(5, "corruption")
    rows: list[dict] = []
    for key, group in cells.groupby(group_columns, dropna=False, sort=True):
        info = dict(zip(group_columns, key if isinstance(key, tuple) else (key,)))
        if not include_corruption:
            info["corruption"] = "all_conditions"
        for method in METHODS:
            threshold = group[f"selected_threshold__{method}"].astype(float)
            far = group[f"false_alarm_rate__{method}"].astype(float)
            power = group[f"power__{method}"].astype(float)
            precision = group[f"alarm_precision__{method}"].astype(float)
            row = {
                **info, "method": method, "n_target_cells": len(group),
                "n_zero_threshold_cells": int((threshold <= 0.0).sum()),
                "nonzero_threshold_rate": float((threshold > 0.0).mean()),
                "selected_threshold_mean": float(threshold.mean()),
                "false_alarm_rate_mean": float(far.mean()),
                "power_mean": float(power.mean()),
                "alarm_precision_mean": float(precision.mean()) if precision.notna().any() else float("nan"),
                "empirical_far_budget_pass": bool(far.mean() <= float(group.alpha.iloc[0]) + 0.02),
                "below_target_floor": bool(group.below_target_floor.iloc[0]),
                "no_harm_rate": float(group.nested_no_harm.mean()) if method == "nested_sc3r" else float("nan"),
            }
            rows.append(row)
    return pd.DataFrame(rows)


def aggregate_cells(cells: pd.DataFrame) -> pd.DataFrame:
    return pd.concat([_aggregate(cells, True), _aggregate(cells, False)], ignore_index=True)


def build_empirical_gate_report(summary: pd.DataFrame, simultaneous: pd.DataFrame) -> dict:
    primary = summary[
        (summary.method == "nested_sc3r")
        & (summary.unit == "class")
        & (summary.corruption != "all_conditions")
    ].copy()
    comparisons = simultaneous[
        (simultaneous.candidate == "nested_sc3r") & (simultaneous.metric == "power")
    ].copy()
    join_keys = [
        key for key in [
            "job_id", "analysis_id", "dataset", "source_dataset", "k_shot",
            "corruption", "source_mode", "normalization_mode", "unit", "alpha",
        ] if key in primary.columns and key in comparisons.columns
    ]
    ci = comparisons[join_keys + ["ci_low", "ci_high", "family_size", "interval_alpha"]]
    merged = primary.merge(ci, on=join_keys, how="left", validate="one_to_one")
    records: list[dict] = []
    for row in merged.to_dict(orient="records"):
        row = {
            key: (value.item() if isinstance(value, np.generic) else value)
            for key, value in row.items()
        }
        reasons = []
        if row["nonzero_threshold_rate"] < MIN_NONZERO_THRESHOLD_RATE:
            reasons.append(
                f"nonzero category-certified threshold rate is below {MIN_NONZERO_THRESHOLD_RATE:.2f}"
            )
        if not row["empirical_far_budget_pass"]:
            reasons.append("mean target FAR exceeds alpha+0.02")
        if row["power_mean"] <= 0.0:
            reasons.append("target power is zero")
        if row["no_harm_rate"] < 0.80:
            reasons.append("target no-harm rate is below 0.80")
        if bool(row["below_target_floor"]):
            if not np.isfinite(row.get("ci_low", np.nan)):
                reasons.append("simultaneous power-gain interval is missing")
            elif row["ci_low"] <= 0.0:
                reasons.append("simultaneous power-gain lower bound is not positive")
        row["empirical_gate"] = "pass" if not reasons else "fail"
        row["failure_reasons"] = reasons
        records.append({
            key: (None if isinstance(value, float) and not np.isfinite(value) else value)
            for key, value in row.items()
        })
    return {
        "claim_boundary": (
            "This is an empirical target gate, not a target-domain validity certificate. "
            "The formal certificate applies to the declared source-unit population under Proposition 2 assumptions."
        ),
        "minimum_nonzero_threshold_rate": MIN_NONZERO_THRESHOLD_RATE,
        "n_gate_cells": len(records),
        "n_empirical_pass": sum(record["empirical_gate"] == "pass" for record in records),
        "n_empirical_fail": sum(record["empirical_gate"] == "fail" for record in records),
        "records": records,
    }


def _latex_escape(value: object) -> str:
    return str(value).replace("_", r"\_")


def _latex_label(value: object) -> str:
    return re.sub(r"[^A-Za-z0-9:-]+", "-", str(value)).strip("-")


def _file_slug(value: object) -> str:
    slug = re.sub(r"[^A-Za-z0-9_-]+", "-", str(value)).strip("-_")
    if not slug:
        raise ValueError("job_id does not contain a safe filename character")
    return slug


def build_latex_tables(summary: pd.DataFrame) -> dict[str, str]:
    selected = summary[
        (summary.method == "nested_sc3r")
        & (summary.unit == "class")
        & (summary.corruption == "all_conditions")
        & (summary.source_mode.isin(["matched_condition", "condition_agnostic"]))
    ].copy()
    outputs: dict[str, str] = {}
    for job_id, job in selected.groupby("job_id", sort=True):
        lines = [
            r"\begin{table*}[t]", r"\centering",
            (r"\caption{Strict nested SC3R summary for job \texttt{" + _latex_escape(job_id)
             + r"}, using category-level source certification. Target FAR, power, precision, and no-harm are empirical; "
               r"the source certificate does not imply unconditional target control. All zero-threshold cells are retained.}"),
            r"\label{tab:nested-sc3r-" + _latex_label(job_id) + "}",
            r"\footnotesize", r"\setlength{\tabcolsep}{4pt}",
            r"\begin{tabular}{llrrrrrr}", r"\toprule",
            r"source mode & $k$ / $\alpha$ & nonzero & zero cells & FAR & power & prec. & no-harm \\",
            r"\midrule",
        ]
        for mode, block in job.groupby("source_mode", sort=True):
            first = True
            for _, row in block.sort_values(["k_shot", "alpha"]).iterrows():
                label = _latex_escape(mode) if first else ""
                first = False
                precision = "--" if not np.isfinite(row.alarm_precision_mean) else f"{row.alarm_precision_mean:.3f}"
                lines.append(
                    f"{label} & {int(row.k_shot)} / {row.alpha:.2f} & {row.nonzero_threshold_rate:.3f} & "
                    f"{int(row.n_zero_threshold_cells)}/{int(row.n_target_cells)} & "
                    f"{row.false_alarm_rate_mean:.3f} & {row.power_mean:.3f} & {precision} & {row.no_harm_rate:.3f} \\\\"
                )
            lines.append(r"\addlinespace[2pt]")
        lines.extend([r"\bottomrule", r"\end{tabular}", r"\end{table*}"])
        outputs[f"tab_nested_sc3r_{_file_slug(job_id)}.tex"] = "\n".join(lines) + "\n"
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--detailed", required=True)
    parser.add_argument("--simultaneous", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--run-tag", required=True)
    args = parser.parse_args()
    detailed = pd.read_csv(args.detailed)
    simultaneous = pd.read_csv(args.simultaneous)
    cells = paired_cell_audit(detailed)
    summary = aggregate_cells(cells)
    gate = build_empirical_gate_report(summary, simultaneous)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    cells.to_csv(out / f"nested_sc3r_{args.run_tag}_paired_cells.csv", index=False)
    summary.to_csv(out / f"nested_sc3r_{args.run_tag}_summary.csv", index=False)
    (out / f"nested_sc3r_{args.run_tag}_empirical_gate.json").write_text(
        json.dumps(gate, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8"
    )
    for name, content in build_latex_tables(summary).items():
        (out / name).write_text(content, encoding="utf-8")
    print(f"wrote {len(cells)} paired cells, {len(summary)} summary rows, and {len(gate['records'])} gate rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
