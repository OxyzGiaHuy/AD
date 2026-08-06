"""Dependency-free alignment audit for the feasibility-first CRESS method.

The numerical claim audit validates exported values. This audit protects a
different failure mode: prose that still compiles after drifting away from the
frozen source construction, candidate allocation, or certification code. It
uses explicit source/config markers and therefore fails closed when either the
implementation or manuscript is refactored without updating the other.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def contains_all(text: str, tokens: tuple[str, ...]) -> bool:
    return all(token in text for token in tokens)


def ordered(text: str, tokens: tuple[str, ...]) -> bool:
    positions = [text.find(token) for token in tokens]
    return all(position >= 0 for position in positions) and positions == sorted(positions)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path("."))
    parser.add_argument(
        "--manuscript",
        type=Path,
        default=Path("els-cas-templates-feasibility-first"),
    )
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    root = args.root.resolve()
    manuscript = (root / args.manuscript).resolve()
    certification = (root / "src/evaluation/sc3r_certification.py").read_text(
        encoding="utf-8"
    )
    nested = (root / "scripts/evaluate_nested_sc3r.py").read_text(encoding="utf-8")
    conformal = (root / "src/conformal.py").read_text(encoding="utf-8")
    backbone = (root / "src/backbones/dinov2.py").read_text(encoding="utf-8")
    sampling = (root / "src/data/sampling.py").read_text(encoding="utf-8")
    corruption_driver = (root / "scripts/evaluate_corruptions.py").read_text(
        encoding="utf-8"
    )
    corruptions = (root / "src/robustness/corruptions.py").read_text(
        encoding="utf-8"
    )
    score_export = (root / "scripts/export_sw_cad_image_views.py").read_text(
        encoding="utf-8"
    )
    config = json.loads(
        (root / "configs/submission_cpu_pipeline.final.json").read_text(encoding="utf-8")
    )
    method = (manuscript / "sections/method.tex").read_text(encoding="utf-8")
    experiments = (manuscript / "sections/experiments.tex").read_text(encoding="utf-8")
    limitations = (manuscript / "sections/limitations.tex").read_text(encoding="utf-8")

    checks: dict[str, bool] = {}
    checks["dinov2_preprocessing_matches"] = contains_all(
        backbone,
        (
            "T.Resize((self.image_size, self.image_size), antialias=True)",
            "T.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225))",
            'out["x_norm_patchtokens"]',
        ),
    ) and contains_all(
        method,
        (
            "$518\\times518$ pixels",
            "ImageNet channel mean and standard deviation",
            "$37\\times37$ grid of $d=384$ vectors",
        ),
    )
    checks["top_fraction_score_matches"] = contains_all(
        conformal,
        (
            "k = max(1, int(np.ceil(scores.shape[1] * rho)))",
            "return part.mean(axis=1).astype(np.float32)",
        ),
    ) and contains_all(
        method,
        (
            "$N=1369$ residuals",
            r"q=\lceil0.01N\rceil=14",
            "accuracy-storage benchmark instead uses the patch maximum ($q=1$)",
        ),
    )
    checks["nested_support_sampling_matches"] = contains_all(
        sampling,
        (
            "ordered = sorted(candidates, key=lambda record: record.path)",
            "permutation = rng.permutation(len(ordered))",
            "permutation[:k]",
        ),
    ) and contains_all(
        experiments,
        (
            "one random permutation of the path-sorted normal training images",
            "defines nested support sets",
            "$k$-shot set is contained",
        ),
    )
    checks["corruption_parameters_match"] = contains_all(
        corruption_driver,
        (
            "severity=0.05",
            "kernel=3",
            "brightness=0.05, contrast=1.15",
            "quality=60",
            "out = func(arr, seed + idx)",
            "np.clip(out, 0.0, 1.0) * 255",
        ),
    ) and contains_all(
        corruptions,
        (
            "rng.normal(0.0, severity, size=image.shape)",
            "ImageFilter.BoxBlur(radius)",
            "(image - 0.5) * contrast + 0.5 + brightness",
        ),
    ) and contains_all(
        experiments,
        (
            r"\mathcal N(0,0.05^2)",
            "box-filter radius of one pixel",
            r"1.15(x-0.5)+0.55",
            "quality-60 encode/decode",
            "support seed plus the fixed image index",
        ),
    )
    checks["target_only_asymmetry_matches"] = ordered(
        score_export,
        (
            "pca = PCASubspace.fit(support_features, pca_components)",
            "image_scores = top_fraction_score(patch_scores, rho=rho)",
            "cal = loio_calibration(support_features, pca_components, rho=rho)",
            "image_p_loio_legacy = conformal_p_values(cal.image_scores, image_scores)",
        ),
    ) and contains_all(
        method,
        (
            "each calibration score uses $k-1$ support images",
            "test score uses all $k$",
            "not a split-conformal p-value with an automatic finite-sample guarantee",
        ),
    )
    checks["support_calibration_k1_fallback_matches"] = contains_all(
        conformal,
        (
            'mode = "loio_conformal" if n_images >= 2 else "patch_split_conformal"',
            "even = np.arange(n_patches) % 2 == 0",
            "held = support_features[:, odd, :]",
        ),
    ) and contains_all(
        method,
        (
            "For $k\\geq2$, $\\mathcal{B}_c=\\mathcal{R}_{c,\\mathrm{LOIO}}$",
            "declared $k=1$ stress test uses one patch-split support calibration residual",
        ),
    )
    checks["normalization_precedes_view_selection"] = ordered(
        nested,
        (
            'frame["support_normalized_score"] = normalize_support_scores',
            "results, candidates, manifests = evaluate_nested",
        ),
    ) and "Thus normalization precedes source-view selection or aggregation" in method
    checks["normalization_formula_matches"] = contains_all(
        nested,
        (
            "center = frame.support_cal_median.to_numpy",
            "scale = frame[scale_column].to_numpy",
            "np.maximum(scale, 1e-6)",
        ),
    ) and contains_all(
        method,
        (
            r"m_c &= \operatorname{median}(\mathcal{B}_c)",
            r"d_c &= \operatorname{MAD}(\mathcal{B}_c)",
            r"\max(d_c,\varepsilon)",
            r"\varepsilon=10^{-6}",
        ),
    )
    checks["source_modes_match"] = contains_all(
        nested,
        (
            '"matched_condition"',
            '"clean_source"',
            '"condition_agnostic"',
            '"mismatched_condition"',
            '["class", "base_image_path"]',
            ".median()",
            "conditions[(conditions.index(target_corruption) + 1) % len(conditions)]",
        ),
    ) and contains_all(
        method,
        (
            "Matched-condition mode",
            "Clean-source mode",
            "Condition-agnostic mode",
            "mismatched-condition routing uses the lexicographic successor",
        ),
    )
    checks["source_rows_are_known_normal"] = (
        "& (frame.label == 0)" in nested
        and "discards every anomalous source row" in experiments
        and "source anomaly scores enter neither" in experiments
    )
    checks["partition_hash_and_allocation_match"] = contains_all(
        certification,
        (
            'f"sc3r-partition|{target_class}|{seed}"',
            "raw_counts = fractions * len(shuffled)",
            "remainders = raw_counts - counts",
            "key=lambda item: (remainders[item], item)",
        ),
    ) and contains_all(
        method,
        (
            "largest fractional remainders",
            "equal remainders resolved toward certification",
            "hash of the target-category identity and seed",
            "held fixed across conditions and $k$",
        ),
    )
    checks["rpc_data_roles_are_disjoint"] = contains_all(
        certification,
        (
            '"reference": tuple(sorted(shuffled[:n_reference]))',
            '"proposal": tuple(sorted(shuffled[n_reference : n_reference + n_proposal]))',
            '"certification": tuple(sorted(shuffled[n_reference + n_proposal :]))',
        ),
    ) and contains_all(
        method,
        (
            "disjoint reference, proposal, and certification sets",
            "Certification data influence neither $\\mathcal T$ nor $M$",
        ),
    )
    checks["reference_proposal_certification_flow_matches"] = ordered(
        nested,
        (
            'reference_scores = subsets["reference"]',
            "proposal_p = conformal_p_values(reference_scores",
            "certification_p = conformal_p_values(reference_scores",
            "candidates = proposal_candidates(proposal_p",
            "certificate = certify_thresholds(",
        ),
    ) and contains_all(
        method,
        (
            "The reference categories define the source-reference rank map",
            "Applying the reference map to the proposal categories",
            "The same reference map is then applied to every certification image",
        ),
    )
    checks["rank_map_plus_one_matches"] = (
        "((1.0 + counts) / (len(calibration) + 1.0))" in conformal
        and r"\frac{1+\sum_{r\in\mathcal{Z}_{\mathcal{R}}}" in method
        and r"{1+|\mathcal{Z}_{\mathcal{R}}|}" in method
    )
    checks["candidate_cap_matches"] = contains_all(
        certification,
        (
            "unique = np.unique(values)",
            "np.linspace(0, len(unique) - 1, max_candidates, dtype=int)",
        ),
    ) and contains_all(
        method,
        ("realized size is $M=|\\mathcal T|$", "$M_{\\max}=20$"),
    ) and config.get("max_candidates") == 20
    checks["category_loss_matches"] = (
        "grouped.setdefault(unit_id, []).append(float(alarm))" in certification
        and "np.mean(grouped[key])" in certification
        and r"L_c(\tau)=\frac{1}{n_c}\sum_{x\in c}L_x(\tau)" in method
    )
    checks["family_allocation_matches"] = contains_all(
        nested,
        (
            "certificate_delta = delta / (len(alphas) * 2.0)",
            "certify_thresholds(",
        ),
    ) and "per_candidate_delta = delta / len(thresholds)" in certification and contains_all(
        method,
        (
            r"\log(2AM/\delta)",
            "tail probability $\\delta/(2AM)$",
            "factor $2A$ allocates the family error",
        ),
    )
    checks["hoeffding_formula_matches"] = (
        "np.sqrt(np.log(1.0 / delta) / (2.0 * len(values)))" in certification
        and r"\sqrt{\frac{\log(2AM/\delta)}{2n}}" in method
    )
    checks["clopper_pearson_formula_matches"] = contains_all(
        certification,
        (
            "beta.ppf(1.0 - delta, successes + 1, len(values) - successes)",
            "if successes == len(values):",
            "return 1.0",
        ),
    ) and "exact one-sided Clopper--Pearson upper bound" in method
    checks["fail_closed_selection_matches"] = (
        "selected_threshold=max(passing, default=0.0)" in certification
        and r"\max\bigl(\{\tau\in\mathcal{T}:U(\tau)\leq\alpha\}\cup\{0\}\bigr)" in method
        and "deterministic fail-closed fallback" in method
    )
    checks["frozen_grid_matches"] = (
        config.get("grid", {}).get("k_shots") == [1, 2, 4, 8]
        and config.get("grid", {}).get("seeds") == [0, 1, 2, 3, 4]
        and config.get("grid", {}).get("corruptions")
        == ["clean", "gaussian_noise", "blur", "brightness_contrast", "jpeg"]
        and config.get("alphas") == [0.05, 0.10, 0.20]
        and config.get("delta") == 0.05
        and len(config.get("jobs", [])) == 4
        and all(len(job.get("source_modes", [])) == 4 for job in config.get("jobs", []))
    )
    checks["target_transfer_scope_matches_proof"] = contains_all(
        method,
        (
            "under the support construction being evaluated",
            "a fresh independent draw from the same meta-population",
            "iid category sampling supplies the weaker marginal new-category statement",
        ),
    ) and contains_all(
        limitations,
        (
            "their interpretation as iid draws from a source-category meta-population",
            "An independent target draw from the same category meta-population",
        ),
    )

    failed = [name for name, passed in checks.items() if not passed]
    report = {
        "status": "pass" if not failed else "fail",
        "checks": checks,
        "failed_checks": failed,
        "scope": (
            "Static alignment of the compiled feasibility-first Method with the frozen "
            "CRESS implementation and final CPU configuration; numerical outputs are "
            "covered by the separate core-claim audit."
        ),
    }
    output = args.output or (
        root / "outputs/paper_tables/feasibility_first_method_alignment_audit.json"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(output)
    if failed:
        print("failed: " + ", ".join(failed))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
