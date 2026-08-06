"""Audit that the numbers printed in the feasibility-first paper match evidence.

The core, method-alignment, and table-aggregation audits validate artifacts and
implementation.  This script closes the remaining direction of traceability:
it reads their JSON reports and verifies the numerical and scope-bearing claims
that are actually exposed in the manuscript and its compiled tables.

The audit is dependency-free.  It deliberately checks rounded publication
values, while retaining the source JSON paths in the emitted claim ledger.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def r3(value: float) -> str:
    return f"{float(value):.3f}"


def contains_all(text: str, tokens: tuple[str, ...] | list[str]) -> bool:
    return all(token in text for token in tokens)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument("--manuscript", type=Path, required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()
    manuscript = args.manuscript.resolve()

    report_paths = {
        "core": root / "outputs/paper_tables/feasibility_first_core_claim_audit.json",
        "method": root / "outputs/paper_tables/feasibility_first_method_alignment_audit.json",
        "aggregation": root / "outputs/paper_tables/feasibility_first_table_aggregation_audit.json",
        "manuscript": root / "outputs/paper_tables/feasibility_first_manuscript_audit.json",
    }
    reports = {
        name: json.loads(path.read_text(encoding="utf-8"))
        for name, path in report_paths.items()
    }

    sections = {
        name: (manuscript / "sections" / f"{name}.tex").read_text(encoding="utf-8")
        for name in (
            "abstract",
            "introduction",
            "method",
            "experiments",
            "results",
            "limitations",
            "conclusion",
        )
    }
    tables = {
        path.stem: path.read_text(encoding="utf-8")
        for path in (manuscript / "tables").glob("*.tex")
    }
    checks: dict[str, bool] = {
        f"upstream_{name}_audit_passes": report.get("status") == "pass"
        for name, report in reports.items()
    }
    ledger: dict[str, dict[str, object]] = {}

    core = reports["core"]
    target = core["target_only"]
    theory = core["theory_counts"]
    strict = core["strict_cress"]
    clean = core["clean_ranking_and_storage"]

    headline = r3(target["headline_far"])
    headline_surfaces = ("abstract", "introduction", "results", "limitations", "conclusion")
    checks["headline_far_is_consistent_across_narrative"] = all(
        headline in sections[name] for name in headline_surfaces
    )
    checks["headline_scope_is_not_promoted_to_population_risk"] = all(
        contains_all(sections[name], tokens)
        for name, tokens in (
            ("introduction", ("dataset-level aggregate", "not a population-level failure probability")),
            ("results", ("neither the MVTec average", "nor a population false-alarm probability")),
            ("limitations", ("largest dataset-level aggregate", "not a population failure probability")),
        )
    )
    ledger["headline_shift_far"] = {
        "value": target["headline_far"],
        "rounded_publication_value": headline,
        "scope": "MVTec, Gaussian noise, k=4, alpha=0.20, pooled benchmark FAR",
        "source": str(report_paths["core"]),
        "surfaces": list(headline_surfaces),
    }

    theory_rows = {
        "Distribution-free, no multiplicity": theory["distribution_free"]["no_multiplicity"],
        "Distribution-free, $M=1$": theory["distribution_free"]["M=1"],
        "Distribution-free, $M=5$": theory["distribution_free"]["M=5"],
        "Distribution-free, $M=20$": theory["distribution_free"]["M=20"],
        "Hoeffding, $M=1$": theory["hoeffding"]["M=1"],
        "Hoeffding, $M=5$": theory["hoeffding"]["M=5"],
        "Hoeffding, $M=20$": theory["hoeffding"]["M=20"],
    }
    feasibility_table = tables["tab_certificate_feasibility"]
    for label, values in theory_rows.items():
        normalized = re.sub(r"\s+", " ", feasibility_table)
        pattern = re.escape(label) + r"\s*&\s*" + r"\s*&\s*".join(
            re.escape(f"{value:,}") for value in values
        )
        checks[f"theory_table_{re.sub('[^a-z0-9]+', '_', label.lower()).strip('_')}"] = (
            re.search(pattern, normalized) is not None
        )
    checks["necessary_counts_remain_labeled_not_sufficient"] = all(
        token in text
        for text, token in (
            (sections["abstract"], "These counts are necessary, not sufficient"),
            (sections["introduction"], "optimistic impossibility-side limits, not sufficient sample sizes"),
            (feasibility_table, "does not itself guarantee a positive CRESS threshold"),
            (sections["results"], "necessary within the scope of Proposition~3"),
            (sections["limitations"], "optimistic necessary limits without multiplicity, not sufficient sample sizes"),
        )
    )
    ledger["distribution_free_category_counts"] = {
        "values_alpha_0.20_0.10_0.05": theory["distribution_free"]["no_multiplicity"],
        "scope": "necessary all-zero counts for deterministic uniformly valid distribution-free UCBs without multiplicity",
        "source": str(report_paths["core"]),
        "surfaces": ["abstract", "introduction", "method", "results", "limitations", "conclusion", "Table 1"],
    }

    # Target-only corruption table: each expected metric triple must be printed.
    false_alarm_table = tables["tab_false_alarm_control"]
    for key, metrics in target["corruption_cells"].items():
        _, k_text, corruption = key.split("/")
        k = int(k_text.split("=")[1])
        triple = (
            r3(metrics["far"]),
            r3(metrics["detection"]),
            r3(metrics["precision"]),
        )
        pattern = rf"&\s*{k}\s*&\s*{triple[0]}\s*&\s*{triple[1]}\s*&\s*{triple[2]}"
        checks[f"false_alarm_table_{key.replace('/', '_')}"] = (
            re.search(pattern, false_alarm_table) is not None
        )

    aggregate_table = tables["tab_attainable_alpha"]
    for key, metrics in target["four_corruption_aggregate"].items():
        k = int(key.rsplit("k", 1)[1])
        attainable = "0.200" if k == 4 else "0.111"
        pattern = (
            rf"&\s*&\s*&\s*0\.20\s*&\s*{attainable}\s*&\s*"
            rf"{r3(metrics['far'])}\s*&\s*{r3(metrics['detection'])}"
        )
        checks[f"attainable_table_{key}"] = re.search(pattern, aggregate_table) is not None

    # Strict CRESS table and scope-bearing narrative.
    strict_table = tables["tab_strict_nested_sc3r"]
    label_to_tex = {
        "MVTec->MVTec": r"MVTec $\rightarrow$ MVTec",
        "VisA->VisA": r"VisA $\rightarrow$ VisA",
        "MVTec->VisA": r"MVTec $\rightarrow$ VisA",
        "MVTec->MPDD": r"MVTec $\rightarrow$ MPDD",
    }
    for job, tex_label in label_to_tex.items():
        category = strict["candidate_summary"][f"{job}/category"]
        image = strict["candidate_summary"][f"{job}/image"]
        checks[f"strict_category_row_{job}"] = contains_all(
            strict_table,
            (tex_label, str(category["min_units"]), r3(category["min_ucb"]), "0.000"),
        )
        checks[f"strict_image_row_{job}"] = contains_all(
            strict_table,
            (
                tex_label,
                f"{image['min_units']} to {image['max_units']}",
                r3(image["min_ucb"]),
                r3(strict["image_nonzero_fraction"][job]),
            ),
        )
    checks["strict_gate_count_and_dependence_scope_are_jointly_printed"] = contains_all(
        sections["results"],
        ("960 gate configurations", "not independent statistical trials", "per-cell rather than grid-wide"),
    )
    checks["strict_zero_result_survives_without_k1"] = (
        strict["category_nonzero_fraction_excluding_k1"] == 0.0
        and "does not depend on the patch-split fallback" in sections["results"]
    )
    ledger["strict_cress_boundary"] = {
        "gate_configurations": strict["gate_configurations"],
        "failed_gate_configurations": strict["failed_gate_configurations"],
        "category_nonzero_fractions": strict["category_nonzero_fraction"],
        "scope": "frozen configurations, not independent trials; per-cell certificate",
        "source": str(report_paths["core"]),
        "surfaces": ["abstract", "introduction", "results", "conclusion", "Table 4"],
    }

    pooled_table = tables["tab_pooled_source_conformal"]
    for key, metrics in strict["pooled_matched_condition"].items():
        job, alpha_text = key.split("/alpha=")
        pattern = (
            rf"&\s*{float(alpha_text):.2f}\s*&\s*{r3(metrics['far'])}\s*&\s*"
            rf"{r3(metrics['power'])}"
        )
        checks[f"pooled_table_{job}_{alpha_text}"] = re.search(pattern, pooled_table) is not None
    checks["pooled_baseline_remains_uncertified"] = all(
        "uncertified" in text
        for text in (pooled_table, sections["experiments"], sections["results"])
    )

    clean_table = tables["tab_clean_efficiency"]
    method_labels = {
        "controlled_nn": "Controlled DINOv2 NN",
        "pca64": "PCA64 (controlled)",
        "pca128": "PCA128 (controlled)",
    }
    for dataset, methods in clean["summaries"].items():
        for method, shots in methods.items():
            if method not in method_labels:
                continue
            for shot, metrics in shots.items():
                k = int(shot.split("=")[1])
                checks[f"clean_table_{dataset}_{method}_k{k}"] = contains_all(
                    clean_table,
                    (method_labels[method], r3(metrics["auroc"]), r3(metrics["ap"])),
                )
    storage = clean["analytic_ranker_storage_mib"]
    checks["ranker_storage_values_match_audit"] = contains_all(
        sections["results"],
        tuple(r3(storage[key]) + r"\,MiB" for key in ("pca64_mib", "pca128_mib", "nn_k1_mib"))
        + (r3(storage["nn_capped_mib"]) + r"\,MiB",),
    )
    checks["pca128_ranker_wrapper_accounting_is_transparent"] = all(
        token in sections["results"]
        for token in (
            "Historical PCA128 artifacts include a 0.566\\,MiB calibration wrapper",
            "raw ranking uses only PCA residuals",
            "counts the 0.189\\,MiB ranker state",
        )
    ) and round(clean["pca128_historical_wrapper_storage_mib"], 3) == 0.566

    # Aggregation ablation is table-derived and deliberately subset-scoped.
    agg_table = tables["tab_agg_ablation"]
    numeric_rows = []
    for line in agg_table.splitlines():
        values = [float(value) for value in re.findall(r"0\.\d{4}", line)]
        if len(values) == 5:
            numeric_rows.append(values)
    largest_gap = max(max(row) - min(row[0], row[2]) for row in numeric_rows)
    checks["aggregation_ablation_gap_is_recomputed"] = (
        f"{largest_gap:.3f}" in sections["results"] and round(largest_gap, 3) == 0.018
    )
    checks["aggregation_ablation_scope_is_not_generalized"] = all(
        token in sections["results"]
        for token in ("limited subset", "does not establish full-dataset invariance")
    )

    checks["three_contributions_have_matching_evidence_sections"] = all(
        token in sections["introduction"]
        for token in (
            "A category-count feasibility calculus",
            "An operational shift audit",
            "An estimand-aware source protocol",
        )
    ) and all(
        token in sections["results"]
        for token in (
            r"\subsection{Category-Count Feasibility}",
            r"\subsection{Shift-Induced False-Alarm Inflation}",
            r"\subsection{CRESS Boundary Test: Categories versus Images}",
        )
    )

    contribution_evidence = {
        "category_count_feasibility_calculus": {
            "claim": "Necessary all-zero category budgets and the declared Hoeffding feasibility calculation",
            "manuscript_evidence": [
                "Method, Propositions 2 and 3",
                "Figure 1",
                "Table 1",
                "Results: Category-Count Feasibility",
            ],
            "artifact_evidence": [
                str(report_paths["core"]),
                str(report_paths["method"]),
            ],
            "excluded_claims": [
                "14/29/59 are sufficient for CRESS",
                "a new generic concentration inequality",
            ],
        },
        "operational_shift_audit": {
            "claim": "Dataset- and condition-specific target-only false-alarm behavior at attainable operating points",
            "manuscript_evidence": [
                "Tables 2 and 3",
                "Figure 4",
                "Results: Shift-Induced False-Alarm Inflation",
            ],
            "artifact_evidence": [str(report_paths["core"])],
            "excluded_claims": [
                "0.341 is a population false-alarm probability",
                "Gaussian noise universally causes the observed failure",
            ],
        },
        "estimand_aware_source_protocol": {
            "claim": "Disjoint source roles and explicit separation of image-mixture and category-unit conclusions",
            "manuscript_evidence": [
                "Method: Nested CRESS Threshold Selection",
                "Table 4",
                "Table 5",
                "Results: CRESS Boundary Test: Categories versus Images",
            ],
            "artifact_evidence": [
                str(report_paths["core"]),
                str(report_paths["method"]),
                str(report_paths["aggregation"]),
            ],
            "excluded_claims": [
                "unconditional target-category control",
                "960 independent replications",
                "image-unit evidence certifies a new-category draw",
                "a ranking state-of-the-art result",
            ],
        },
    }

    failed = [name for name, passed in checks.items() if not passed]
    report = {
        "status": "pass" if not failed else "fail",
        "checks": checks,
        "failed_checks": failed,
        "claim_ledger": ledger,
        "contribution_evidence": contribution_evidence,
        "source_reports": {name: str(path) for name, path in report_paths.items()},
        "interpretation": (
            "A pass means the rounded values and their principal scope qualifiers are present "
            "on the manuscript surface and agree with the upstream audit reports. It does not "
            "replace the artifact, implementation, bibliography, or human scientific review."
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
