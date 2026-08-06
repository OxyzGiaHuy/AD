"""Fail-fast structural and terminology audit for the compiled manuscript.

This complements the numerical audit. It checks the declared first-use
expansions, guards against retired claims/legacy method names, and verifies the
Elsevier CAS entry point. It intentionally does not edit or validate
``references.bib``, which remains an author-owned submission task.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


EXPECTED_INPUTS = (
    "abstract",
    "introduction",
    "related_work",
    "method",
    "experiments",
    "results",
    "limitations",
    "conclusion",
    "appendix",
    "declarations",
)

COMPILED_TABLES = (
    "tab_certificate_feasibility",
    "tab_attainable_alpha",
    "tab_false_alarm_control",
    "tab_strict_nested_sc3r",
    "tab_pooled_source_conformal",
    "tab_clean_efficiency",
    "tab_agg_ablation",
)

COMPILED_TABLE_LABELS = (
    "tab:certificate-feasibility",
    "tab:attainable-alpha",
    "tab:false-alarm-control",
    "tab:strict-cress",
    "tab:pooled-source-conformal",
    "tab:clean-efficiency",
    "tab:agg-ablation",
)

COMPILED_FIGURE_LABELS = (
    "fig:certificate-feasibility",
    "fig:target-pipeline",
    "fig:cress-pipeline",
    "fig:uniformity",
)

EXPANSIONS = {
    "sections/abstract.tex": (
        r"leave-one-image-out \(LOIO\)",
        r"principal component analysis \(PCA\)",
        r"Cross-category Reliability Estimation with Source Support \(CRESS\)",
        r"independent and identically distributed \(iid\)",
        r"false-alarm rate \(FAR\)",
        r"upper confidence bound \(UCB\)",
    ),
    "sections/introduction.tex": (
        r"area under the receiver operating characteristic curve \(AUROC\)",
        r"average precision \(AP\)",
        r"anomaly detection \(AD\)",
        r"nearest-neighbor \(NN\)",
        r"Metal Parts Defect Dataset \(MPDD\)",
    ),
    "sections/related_work.tex": (
        r"probably approximately correct \(PAC\)",
        r"Heterophily-Aware Diffused Conformal Prediction \(HeAD-CP\)",
        r"graph neural network \(GNN\)",
        r"Shape-Adapting Gated Experts \(SAGE\)",
    ),
    "sections/method.tex": (
        r"Vision Transformer using \$14\\times14\$ patches \(ViT-S/14\)",
        r"median absolute deviation \(MAD\)",
    ),
    "sections/experiments.tex": (
        r"graphics processing unit \(GPU\)",
        r"32-bit floating-point \(fp32\)",
        r"Secure Hash Algorithm 256-bit \(SHA-256\)",
        r"cumulative distribution function \(CDF\)",
    ),
    "sections/results.tex": (
        r"area under the precision-recall curve \(AUPR\)",
    ),
    "tables/tab_clean_efficiency.tex": (
        r"mebibytes \(MiB\)",
    ),
}

# The paper-wide convention is stricter than merely requiring an expansion:
# after the first ``full form (abbreviation)'', prose uses the abbreviation.
# Keywords are excluded because they are indexing metadata rather than prose.
FULL_FORMS = (
    r"leave-one-image-out",
    r"principal component analysis",
    r"Cross-category Reliability Estimation with Source Support",
    r"independent and identically distributed",
    r"false-alarm rate",
    r"upper confidence bound",
    r"area under the receiver operating characteristic curve",
    r"average precision",
    r"anomaly detection",
    r"nearest-neighbor",
    r"Metal Parts Defect Dataset",
    r"probably approximately correct",
    r"Heterophily-Aware Diffused Conformal Prediction",
    r"graph neural network",
    r"Shape-Adapting Gated Experts",
    r"Vision Transformer using",
    r"median absolute deviation",
    r"graphics processing unit",
    r"32-bit floating-point",
    r"Secure Hash Algorithm 256-bit",
    r"cumulative distribution function",
    r"area under the precision-recall curve",
    r"mebibytes",
)

FORBIDDEN = {
    "retired FAR headline": r"\b0\.463\b",
    "legacy method name": r"\bSC3R\b",
    "legacy configuration name": r"CalibSubspaceHead",
    "independence overclaim": r"(?<!not )960 independent",
    "ranking overclaim": r"claim(?:s|ed|ing)? (?:a )?state[- ]of[- ]the[- ]art",
    "AI handoff wording": r"\bhandoff\b",
    "unsupported official AnomalyDINO label": r"\bofficial AnomalyDINO\b",
    "unsupported cached-feature latency claim": r"(?:scoring takes approximately|reported scoring latency)",
    "target-certification scope ambiguity": r"category-certified target cell",
}


def prose_word_count(latex: str) -> int:
    """Approximate the submission-system count after removing LaTeX markup.

    Displayed mathematics is excluded because Elsevier's abstract limit applies
    to prose. Hyphenated compounds and decimal values are each counted once.
    The function is intentionally conservative about visible command arguments.
    """
    text = re.sub(r"(?m)(?<!\\)%.*$", " ", latex)
    text = re.sub(r"\\begin\{[^}]+\}|\\end\{[^}]+\}", " ", text)
    text = re.sub(r"\$.*?\$|\\\[.*?\\\]", " ", text, flags=re.DOTALL)
    text = re.sub(r"\\(?:textbf|emph|textrm|textit)\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z@]+\*?(?:\[[^\]]*\])?", " ", text)
    text = text.replace(r"\%", "%")
    text = re.sub(r"[{}~]", " ", text)
    return len(re.findall(r"[A-Za-z0-9]+(?:[.'-][A-Za-z0-9]+)*%?", text))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    root = args.root.resolve()

    main_text = (root / "main.tex").read_text(encoding="utf-8")
    observed_inputs = tuple(re.findall(r"\\input\{sections/([^}]+)\}", main_text))
    checks: dict[str, bool] = {
        "cas_double_column": r"\documentclass[a4paper,fleqn]{cas-dc}" in main_text,
        "official_cas_bibliography_style": (
            r"\bibliographystyle{cas-model2-names}" in main_text
        ),
        "compiled_section_order": observed_inputs == EXPECTED_INPUTS,
    }

    compiled_paths = [
        root / "main.tex",
        *(root / "sections" / f"{name}.tex" for name in EXPECTED_INPUTS),
        *(root / "tables" / f"{name}.tex" for name in COMPILED_TABLES),
    ]
    all_tex = "\n".join(path.read_text(encoding="utf-8") for path in compiled_paths)
    terminology_tex = "\n".join(
        path.read_text(encoding="utf-8") for path in compiled_paths if path.name != "main.tex"
    )
    checks["pipeline_placeholders_are_replaced"] = all_tex.count("Placeholder:") == 0
    checks["final_pipeline_assets_exist"] = all(
        (root / "figures" / filename).is_file()
        for filename in ("fig_target_pipeline.pdf", "fig_cress_pipeline.pdf")
    ) and all(
        token in all_tex
        for token in (
            r"\includegraphics[width=0.98\textwidth]{fig_target_pipeline}",
            r"\includegraphics[width=0.98\textwidth]{fig_cress_pipeline}",
        )
    )
    observed_table_labels = tuple(re.findall(r"\\label\{(tab:[^}]+)\}", all_tex))
    observed_figure_labels = tuple(re.findall(r"\\label\{(fig:[^}]+)\}", all_tex))
    checks["compiled_table_set_is_exact"] = set(observed_table_labels) == set(
        COMPILED_TABLE_LABELS
    ) and len(observed_table_labels) == len(COMPILED_TABLE_LABELS)
    checks["compiled_figure_set_is_exact"] = set(observed_figure_labels) == set(
        COMPILED_FIGURE_LABELS
    ) and len(observed_figure_labels) == len(COMPILED_FIGURE_LABELS)
    checks["every_compiled_table_is_called_out"] = all(
        re.search(r"\\ref\{" + re.escape(label) + r"\}", all_tex)
        for label in COMPILED_TABLE_LABELS
    )
    checks["every_compiled_figure_is_called_out"] = all(
        re.search(r"\\ref\{" + re.escape(label) + r"\}", all_tex)
        for label in COMPILED_FIGURE_LABELS
    )
    feasibility_figure_source = root / "figures" / "fig_certificate_feasibility.tex"
    feasibility_figure_pdf = root / "figures" / "fig_certificate_feasibility.pdf"
    figure_text = (
        feasibility_figure_source.read_text(encoding="utf-8")
        if feasibility_figure_source.exists()
        else ""
    )
    checks["feasibility_figure_vector_assets_exist"] = (
        feasibility_figure_source.is_file() and feasibility_figure_pdf.is_file()
    )
    checks["feasibility_figure_formulas_match_theory"] = all(
        token in figure_text
        for token in (
            "1 - 0.05^(1/x)",
            "1 - (0.05/6)^(1/x)",
            "sqrt(ln(120)/(2*x))",
        )
    )
    checks["feasibility_figure_preserves_key_quantities"] = all(
        token in figure_text
        for token in (
            "0.527",
            "14 (optimistic), 22 (frozen), 60 (Hoeffding)",
            "only $n=3$ or $4$",
        )
    )
    checks["feasibility_figure_has_collision_and_print_guards"] = all(
        token in figure_text
        for token in (
            "forget plot",
            "fill=white",
            "dash pattern=on 7pt off 2.2pt",
            "dash pattern=on 8pt off 2pt on 1.2pt off 2pt",
        )
    )
    method_text = (root / "sections" / "method.tex").read_text(encoding="utf-8")
    experiment_text = (root / "sections" / "experiments.tex").read_text(encoding="utf-8")
    checks["candidate_family_size_is_unambiguous"] = all(
        token in method_text
        for token in (r"M=|\mathcal T|", r"M_{\max}=20", "realized size")
    ) and all(
        token in experiment_text for token in ("realized $M=|\\mathcal T|", r"\leq20")
    )
    limitation_text = (root / "sections" / "limitations.tex").read_text(
        encoding="utf-8"
    )
    result_text = (root / "sections" / "results.tex").read_text(encoding="utf-8")
    checks["category_unit_includes_support_and_views"] = all(
        token in method_text
        for token in (
            "category unit comprises the category, its support-set construction",
            "category units that include their support construction and held-out views",
            "together with its support construction and normal-view sampling mechanism",
        )
    )
    checks["category_bound_places_independence_at_the_correct_level"] = all(
        token in method_text
        for token in (
            "allows arbitrary dependence among its archived views",
            "Hoeffding requires iid sampling across complete category units",
            "within-category archive represents the declared deployment distribution",
        )
    )
    checks["image_iid_model_is_explicitly_idealized"] = all(
        token in text
        for text, token in (
            (method_text, "The stratified archive does not imply this idealized model"),
            (limitation_text, "iid pooled alarm indicators are an idealized sensitivity assumption"),
            (result_text, "idealized conditional iid source-image assumption"),
        )
    )
    checks["distribution_free_impossibility_scope_is_explicit"] = all(
        token in text
        for text, token in (
            (method_text, "deterministic uniformly valid distribution-free bound"),
            (result_text, "within the deterministic distribution-free class of Proposition~3"),
            (limitation_text, "deterministic, uniformly valid, distribution-free UCBs"),
        )
    )
    checks["certificate_multiplicity_scope_is_per_cell"] = all(
        token in text
        for text, token in (
            (experiment_text, "not a simultaneous 95\\% guarantee over the complete experimental grid"),
            (result_text, "per-cell rather than grid-wide simultaneous guarantee"),
            (limitation_text, "does not claim one simultaneous 95\\% event over all reported cells"),
        )
    )
    introduction_text = (root / "sections" / "introduction.tex").read_text(
        encoding="utf-8"
    )
    abstract_text = (root / "sections" / "abstract.tex").read_text(encoding="utf-8")
    conclusion_text = (root / "sections" / "conclusion.tex").read_text(
        encoding="utf-8"
    )
    checks["category_transfer_requires_iid_draw"] = all(
        token in text
        for text, token in (
            (introduction_text, "An iid category-sampling model supports only a marginal bound"),
            (method_text, "a fresh independent draw from the same meta-population"),
            (method_text, "iid category sampling supplies the weaker marginal new-category statement"),
            (limitation_text, "their interpretation as iid draws from a source-category meta-population"),
            (limitation_text, "An independent target draw from the same category meta-population"),
        )
    )
    checks["benchmark_category_independence_is_not_asserted"] = all(
        token in text
        for text, token in (
            (introduction_text, "three or four distinct certification categories"),
            (introduction_text, "interpreting them as iid units is a modeling assumption"),
            (limitation_text, "benchmark categories are a fixed heterogeneous collection"),
            (limitation_text, "their interpretation as iid draws"),
        )
    )
    checks["necessary_category_counts_never_become_sufficiency_claims"] = all(
        token in text
        for text, token in (
            (abstract_text, "These counts are necessary, not sufficient"),
            (introduction_text, "optimistic impossibility-side limits, not sufficient sample sizes"),
            (method_text, "necessary lower limits, not claims that the corresponding sample sizes suffice"),
            (result_text, "not sufficient sample sizes for a positive CRESS threshold"),
            (limitation_text, "optimistic necessary limits without multiplicity, not sufficient sample sizes"),
            (conclusion_text, "necessary lower limits, not sufficient budgets for CRESS"),
        )
    )
    checks["source_certificate_is_never_promoted_to_unconditional_target_control"] = all(
        token in text
        for text, token in (
            (abstract_text, "selected source mixture rather than marginal risk over a new-category draw"),
            (introduction_text, "not category-conditional control for every realized target"),
            (method_text, "This is a source-domain certificate; target-category control additionally requires"),
            (result_text, "rather than certified new-category risk"),
            (limitation_text, "CRESS certifies source-domain risk under the assumptions of Proposition~1"),
            (conclusion_text, "convert a source-domain certificate into unconditional target control"),
        )
    )
    checks["cress_is_positioned_as_protocol_not_ranker"] = all(
        token in text
        for text, token in (
            (introduction_text, "CRESS is a source-assisted thresholding and audit protocol, not a new anomaly ranker"),
            (experiment_text, "the frozen DINOv2 subspace residual is inherited"),
            (result_text, "not a ranking contribution or state-of-the-art claim"),
            (limitation_text, "the paper does not claim ranking state of the art"),
        )
    )
    checks["target_only_conformal_form_is_not_claimed_valid_without_exchangeability"] = all(
        token in text
        for text, token in (
            (method_text, "call Eq.~\\eqref{eq:loio} a rank value unless its validity conditions are invoked"),
            (method_text, "not a split-conformal p-value with an automatic finite-sample guarantee"),
            (result_text, "rather than presuming validity"),
            (result_text, "treat the CDF comparison as descriptive"),
        )
    )
    checks["headline_shift_remains_dataset_specific_and_noncausal"] = all(
        token in text
        for text, token in (
            (introduction_text, "not a population-level failure probability"),
            (result_text, "neither the MVTec average nor a population false-alarm probability"),
            (result_text, "do not identify a causal mechanism"),
            (limitation_text, "not a population failure probability or a universal response to Gaussian noise"),
        )
    )
    checks["strict_grid_is_not_counted_as_independent_replication"] = all(
        token in text
        for text, token in (
            (introduction_text, "not 960 independent failures"),
            (result_text, "not independent statistical trials"),
            (result_text, "does not provide 960 replications of the theoretical result"),
            (conclusion_text, "not independent trials"),
        )
    )
    checks["corruption_parameters_are_declared"] = all(
        token in experiment_text
        for token in (
            r"\mathcal N(0,0.05^2)",
            "box-filter radius of one pixel",
            "Support images remain clean; each corruption is applied only to evaluation views",
            r"1.15(x-0.5)+0.55",
            "JPEG uses a quality-60 encode/decode",
            "quantized to 8-bit, and stored as a PNG",
            "support seed plus the fixed image index",
        )
    )
    checks["backbone_preprocessing_is_declared"] = all(
        token in method_text
        for token in (
            r"$518\times518$ pixels",
            "ImageNet channel mean and standard deviation",
            r"$37\times37$ grid",
            r"$d=384$ vectors",
            "all target-support patches",
        )
    )
    checks["score_aggregation_is_fully_declared"] = all(
        token in method_text
        for token in (
            r"$N=1369$ residuals",
            r"q=\lceil0.01N\rceil=14",
            "top-$1\\%$ mean",
            "patch maximum ($q=1$)",
        )
    )
    checks["nested_support_sampling_is_declared"] = all(
        token in experiment_text
        for token in (
            "one random permutation of the path-sorted normal training images",
            "defines nested support sets",
            "$k$-shot set is contained",
        )
    )
    checks["strict_archive_sampling_and_label_scope_are_declared"] = all(
        token in experiment_text
        for token in (
            "at most 120 evaluation records per category, seed, and condition",
            "deterministic label-stratified sampling",
            "dataset labels determine the retained evaluation strata",
            "Target labels are then used only to score evaluation outcomes",
            "discards every anomalous source row",
            "source anomaly scores enter neither",
        )
    )
    clean_table_text = (root / "tables" / "tab_clean_efficiency.tex").read_text(
        encoding="utf-8"
    )
    strict_table_text = (root / "tables" / "tab_strict_nested_sc3r.tex").read_text(
        encoding="utf-8"
    )
    pooled_table_text = (root / "tables" / "tab_pooled_source_conformal.tex").read_text(
        encoding="utf-8"
    )
    checks["strict_table_separates_configuration_and_cell_denominators"] = all(
        token in strict_table_text
        for token in (
            "240 per source-to-target job",
            "18,000",
            "14,400",
            "7,200",
        )
    )
    checks["pooled_table_declares_unweighted_cell_aggregation"] = (
        "unweighted means of within-target-cell" in pooled_table_text
    )
    checks["external_ranker_rows_are_reported_not_reproduced"] = all(
        token in clean_table_text
        for token in (
            "AnomalyDINO-S (reported)",
            r"\cite{damm2025anomalydino,winclip2023}",
        )
    ) and "Official AnomalyDINO" not in clean_table_text
    declaration_text = (root / "sections" / "declarations.tex").read_text(
        encoding="utf-8"
    )
    checks["elsevier_ai_use_is_declared_at_both_relevant_levels"] = all(
        token in text
        for text, token in (
            (experiment_text, "OpenAI Codex assisted code review, test generation, and audit scripting"),
            (experiment_text, "no AI tool generated or altered empirical data"),
            (
                declaration_text,
                "Declaration of generative AI and AI-assisted technologies in the manuscript preparation process",
            ),
            (declaration_text, "The authors reviewed and edited all tool-assisted material"),
        )
    )

    highlights = [
        line.strip()
        for line in (root / "highlights.txt").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    checks["elsevier_highlight_count_and_length"] = (
        3 <= len(highlights) <= 5 and all(len(line) <= 85 for line in highlights)
    )
    checks["highlights_are_bulleted"] = all(line.startswith("- ") for line in highlights)
    abstract_text = (root / "sections" / "abstract.tex").read_text(encoding="utf-8")
    abstract_word_count = prose_word_count(abstract_text)
    checks["abstract_at_most_250_words"] = abstract_word_count <= 250
    keyword_match = re.search(
        r"\\begin\{keywords\}(.*?)\\end\{keywords\}", main_text, flags=re.DOTALL
    )
    keywords = (
        [item.strip() for item in keyword_match.group(1).split(r"\sep") if item.strip()]
        if keyword_match
        else []
    )
    checks["one_to_six_keywords"] = 1 <= len(keywords) <= 6
    checks["portable_pdf_metadata_declared"] = all(
        token in main_text
        for token in (
            "pdfauthor={Gia Huy Thai and Anh Nguyen}",
            "pdfsubject={Reliability and certification limits",
            "pdfkeywords={industrial anomaly detection",
        )
    )
    checks["no_unicode_dashes_in_compiled_tex"] = "–" not in all_tex and "—" not in all_tex

    missing_expansions = []
    for relative, patterns in EXPANSIONS.items():
        text = (root / relative).read_text(encoding="utf-8")
        for pattern in patterns:
            if re.search(pattern, text) is None:
                missing_expansions.append(f"{relative}: {pattern}")
    checks["declared_first_use_expansions"] = not missing_expansions

    duplicate_expansions = []
    for relative, patterns in EXPANSIONS.items():
        for pattern in patterns:
            count = len(re.findall(pattern, terminology_tex))
            if count != 1:
                duplicate_expansions.append(
                    f"{relative}: expected exactly one occurrence of {pattern}, found {count}"
                )
    checks["each_declared_expansion_occurs_once"] = not duplicate_expansions

    repeated_full_forms = {
        pattern: len(re.findall(pattern, terminology_tex, flags=re.IGNORECASE))
        for pattern in FULL_FORMS
        if len(re.findall(pattern, terminology_tex, flags=re.IGNORECASE)) != 1
    }
    checks["full_forms_used_only_at_first_expansion"] = not repeated_full_forms

    forbidden_hits = {
        label: len(re.findall(pattern, all_tex, flags=re.IGNORECASE))
        for label, pattern in FORBIDDEN.items()
    }
    checks["no_retired_or_overclaim_terms"] = not any(forbidden_hits.values())

    report = {
        "status": "pass" if all(checks.values()) else "fail",
        "checks": checks,
        "observed_section_order": observed_inputs,
        "abstract_word_count_approximate": abstract_word_count,
        "keywords": keywords,
        "missing_expansions": missing_expansions,
        "duplicate_expansions": duplicate_expansions,
        "repeated_full_forms": repeated_full_forms,
        "forbidden_hits": forbidden_hits,
        "bibliography_note": "references.bib is intentionally outside this audit",
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
