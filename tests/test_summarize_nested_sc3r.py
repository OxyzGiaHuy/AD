import pandas as pd
import pytest
import shutil
import subprocess

from scripts.summarize_nested_sc3r import (
    aggregate_cells,
    build_empirical_gate_report,
    build_latex_tables,
    paired_cell_audit,
)


def _detailed():
    rows = []
    for target_index, target_class in enumerate(["a", "b"]):
        for method, threshold, far, power, precision in [
            ("target_only", 0.05, 0.00, 0.00, float("nan")),
            ("pooled_source_conformal", 0.05, 0.04, 0.25, 0.80),
            ("nested_sc3r", 0.00 if target_index == 0 else 0.03, 0.03, 0.20, 0.85),
        ]:
            rows.append({
                "job_id": "toy_within", "analysis_id": "primary",
                "dataset": "toy", "source_dataset": "toy",
                "target_class": target_class, "k_shot": 4, "seed": 0,
                "corruption": "clean", "source_mode": "condition_agnostic",
                "normalization_mode": "median_mad", "unit": "class",
                "alpha": 0.05, "method": method,
                "selected_threshold": threshold, "false_alarm_rate": far,
                "power": power, "alarm_precision": precision,
            })
    return pd.DataFrame(rows)


def _simultaneous():
    return pd.DataFrame([{
        "job_id": "toy_within", "analysis_id": "primary",
        "dataset": "toy", "source_dataset": "toy", "k_shot": 4,
        "corruption": "clean", "source_mode": "condition_agnostic",
        "normalization_mode": "median_mad", "unit": "class", "alpha": 0.05,
        "candidate": "nested_sc3r", "metric": "power",
        "ci_low": 0.01, "ci_high": 0.30, "family_size": 1,
        "interval_alpha": 0.05,
    }])


def test_summary_retains_zero_threshold_cells_and_gate_fails_low_coverage():
    cells = paired_cell_audit(_detailed())
    summary = aggregate_cells(cells)
    row = summary[
        (summary.method == "nested_sc3r")
        & (summary.corruption == "all_conditions")
    ].iloc[0]
    assert row.n_zero_threshold_cells == 1
    assert row.n_target_cells == 2
    assert row.nonzero_threshold_rate == 0.5
    gate = build_empirical_gate_report(summary, _simultaneous())
    assert gate["n_empirical_fail"] == 1
    assert "nonzero category-certified threshold rate" in gate["records"][0]["failure_reasons"][0]
    table = build_latex_tables(summary)["tab_nested_sc3r_toy_within.tex"]
    assert "1/2" in table
    assert "0.500" in table


def test_paired_cell_audit_rejects_missing_method():
    incomplete = _detailed().query("method != 'target_only'")
    with pytest.raises(ValueError, match="required paired methods"):
        paired_cell_audit(incomplete)


def test_generated_nested_table_compiles_when_latex_is_available(tmp_path):
    if shutil.which("pdflatex") is None:
        pytest.skip("pdflatex is unavailable")
    summary = aggregate_cells(paired_cell_audit(_detailed()))
    table = build_latex_tables(summary)["tab_nested_sc3r_toy_within.tex"]
    (tmp_path / "table.tex").write_text(table, encoding="utf-8")
    (tmp_path / "main.tex").write_text(
        "\\documentclass{article}\n\\usepackage{booktabs}\n\\begin{document}\n"
        "\\input{table.tex}\n\\end{document}\n",
        encoding="utf-8",
    )
    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "main.tex"],
        cwd=tmp_path, check=True, capture_output=True,
    )
