import numpy as np
import pytest
import pandas as pd

from src.evaluation.sc3r_certification import (
    clopper_pearson_upper_bound,
    certify_thresholds,
    hoeffding_upper_bound,
    partition_source_classes,
    proposal_candidates,
)


def test_proposal_candidates_are_positive_bounded_and_capped():
    candidates = proposal_candidates(np.linspace(0.01, 1.0, 100), max_candidates=9)
    assert len(candidates) == 9
    assert np.all(np.diff(candidates) > 0)
    assert candidates.min() > 0.0 and candidates.max() <= 1.0


def test_hoeffding_upper_is_not_below_empirical_loss():
    losses = np.asarray([0.0] * 95 + [1.0] * 5)
    upper = hoeffding_upper_bound(losses, delta=0.05)
    assert 0.05 <= upper <= 1.0


def test_clopper_pearson_zero_alarm_bound_matches_closed_form():
    losses = np.zeros(100, dtype=np.float64)
    upper = clopper_pearson_upper_bound(losses, delta=0.05)
    assert abs(upper - (1.0 - 0.05 ** (1.0 / 100.0))) < 1e-12


def test_clopper_pearson_rejects_nonbinary_cluster_means():
    with pytest.raises(ValueError, match="Bernoulli"):
        clopper_pearson_upper_bound(np.asarray([0.0, 0.5, 1.0]), delta=0.05)


def test_image_certificate_records_exact_binomial_method():
    p_values = np.linspace(0.001, 1.0, 2000)
    result = certify_thresholds(
        p_values, np.asarray([0.01]), alpha=0.10, delta=0.05,
        bound_method="clopper_pearson",
    )
    assert result.bound_method == "clopper_pearson"
    assert result.candidates[0].passes


def test_simultaneous_selection_returns_largest_passing_candidate():
    p_values = np.linspace(0.001, 1.0, 2000)
    result = certify_thresholds(p_values, np.asarray([0.01, 0.05, 0.10]), alpha=0.10, delta=0.05)
    passing = [candidate.threshold for candidate in result.candidates if candidate.passes]
    assert passing
    assert result.selected_threshold == max(passing)
    assert all(candidate.upper_bound <= result.alpha for candidate in result.candidates if candidate.passes)


def test_cluster_unit_does_not_count_rows_as_independent():
    p_values = np.linspace(0.001, 1.0, 1000)
    image_result = certify_thresholds(p_values, np.asarray([0.01]), alpha=0.20, delta=0.05)
    cluster_ids = [f"class-{index // 100}" for index in range(1000)]
    cluster_result = certify_thresholds(p_values, np.asarray([0.01]), alpha=0.20, delta=0.05, unit_ids=cluster_ids)
    assert image_result.candidates[0].n_units == 1000
    assert cluster_result.candidates[0].n_units == 10
    assert cluster_result.candidates[0].upper_bound > image_result.candidates[0].upper_bound


def test_candidate_validation_rejects_zero_p_values():
    with pytest.raises(ValueError, match="p-values"):
        certify_thresholds(np.asarray([0.0, 0.5]), np.asarray([0.1]), alpha=0.2, delta=0.05)


def test_partition_is_deterministic_disjoint_and_excludes_target():
    classes = [f"class-{index}" for index in range(15)]
    first = partition_source_classes(classes, target_class="class-3", seed=7)
    second = partition_source_classes(classes, target_class="class-3", seed=7)
    assert first == second
    sets = [set(first[name]) for name in ("reference", "proposal", "certification")]
    assert not sets[0] & sets[1] and not sets[0] & sets[2] and not sets[1] & sets[2]
    assert set.union(*sets) == set(classes) - {"class-3"}


def test_partition_allocation_is_deterministic_and_nonempty():
    classes = [f"class-{index}" for index in range(15)]
    split = partition_source_classes(classes, target_class="class-3", seed=7, allocation=(0.4, 0.3, 0.3))
    assert [len(split[name]) for name in ("reference", "proposal", "certification")] == [6, 4, 4]
    with pytest.raises(ValueError, match="allocation"):
        partition_source_classes(classes, "class-3", 7, allocation=(0.5, 0.5, 0.5))


def test_nested_evaluator_never_uses_target_in_source_partitions():
    from scripts.evaluate_nested_sc3r import evaluate_nested

    rows = []
    for class_index in range(8):
        for label in (0, 1):
            for image_index in range(10):
                rows.append(
                    {
                        "dataset": "toy",
                        "class": f"c{class_index}",
                        "k_shot": 4,
                        "seed": 0,
                        "corruption": "clean",
                        "label": label,
                        "support_normalized_score": image_index / 10 + 3 * label,
                    }
                )
    results, candidates, manifests = evaluate_nested(
        pd.DataFrame(rows), [0.2], delta=0.05, max_candidates=5, source_mode="matched_condition"
    )
    assert not results.empty and not candidates.empty and manifests
    assert set(results.method) == {"nested_sc3r", "pooled_source_conformal"}
    for manifest in manifests:
        target = manifest["target_class"]
        source_classes = (
            manifest["reference_classes"] + manifest["proposal_classes"] + manifest["certification_classes"]
        )
        assert target not in source_classes


def test_condition_agnostic_collapses_repeated_views_by_base_image():
    from scripts.evaluate_nested_sc3r import _select_source_pool

    rows = []
    for cls in ["a", "b"]:
        for image_index in range(3):
            for corruption, offset in [("clean", 0.0), ("jpeg", 2.0)]:
                rows.append({
                    "dataset": "toy", "class": cls, "k_shot": 4, "seed": 0,
                    "corruption": corruption, "label": 0,
                    "base_image_path": f"{cls}/{image_index}.png",
                    "support_normalized_score": image_index + offset,
                })
    source, description = _select_source_pool(
        pd.DataFrame(rows), "toy", "target", 4, 0, "clean", "condition_agnostic"
    )
    assert len(source) == 6
    assert description == "all_conditions_median_by_base_image"
    assert sorted(source.support_normalized_score.unique()) == [1.0, 2.0, 3.0]


def test_mismatched_condition_never_selects_target_condition():
    from scripts.evaluate_nested_sc3r import _select_source_pool

    frame = pd.DataFrame([
        {"dataset": "toy", "class": cls, "k_shot": 4, "seed": 0,
         "corruption": corruption, "label": 0, "support_normalized_score": 0.1}
        for cls in ["a", "b"] for corruption in ["clean", "jpeg"]
    ])
    source, selected = _select_source_pool(
        frame, "toy", "target", 4, 0, "clean", "mismatched_condition"
    )
    assert selected == "jpeg"
    assert set(source.corruption) == {"jpeg"}


def test_source_resource_limits_are_deterministic_and_class_safe():
    from scripts.evaluate_nested_sc3r import _limit_source_pool

    frame = pd.DataFrame([
        {"class": f"c{class_index}", "base_image_path": f"c{class_index}/{image_index}.png",
         "support_normalized_score": image_index / 10}
        for class_index in range(10) for image_index in range(5)
    ])
    first = _limit_source_pool(frame, "target", 3, "matched_condition", 6, 2)
    second = _limit_source_pool(frame.sample(frac=1.0, random_state=9), "target", 3, "matched_condition", 6, 2)
    assert first["class"].nunique() == 6
    assert len(first) == 12
    assert set(zip(first["class"], first.base_image_path)) == set(zip(second["class"], second.base_image_path))


def test_support_normalization_modes_use_only_supplied_support_statistics():
    from scripts.evaluate_nested_sc3r import normalize_support_scores

    frame = pd.DataFrame({
        "raw_score": [2.0, 4.0], "support_cal_median": [1.0, 2.0],
        "support_cal_mad": [0.5, 1.0], "support_cal_q25": [0.0, 1.0],
        "support_cal_q75": [2.0, 5.0],
    })
    assert normalize_support_scores(frame, "none").tolist() == [2.0, 4.0]
    assert normalize_support_scores(frame, "median_mad").tolist() == [2.0, 2.0]
    assert normalize_support_scores(frame, "median_iqr").tolist() == [0.5, 0.5]


def test_nested_evaluator_adds_paired_target_only_when_residuals_are_supplied():
    from scripts.evaluate_nested_sc3r import evaluate_nested

    rows = []
    residual_rows = []
    for class_index in range(8):
        cls = f"c{class_index}"
        residual_rows.extend([
            {"dataset": "toy", "class": cls, "k_shot": 4, "seed": 0, "loio_residual": value}
            for value in [0.1, 0.2, 0.3, 0.4]
        ])
        for label in (0, 1):
            for image_index in range(4):
                raw = 0.1 * image_index + label
                rows.append({
                    "dataset": "toy", "class": cls, "k_shot": 4, "seed": 0,
                    "corruption": "clean", "label": label, "raw_score": raw,
                    "support_normalized_score": raw,
                })
    results, _, _ = evaluate_nested(
        pd.DataFrame(rows), [0.2], delta=0.05, max_candidates=5,
        source_mode="matched_condition", support_residuals=pd.DataFrame(residual_rows)
    )
    assert set(results.method) == {"nested_sc3r", "pooled_source_conformal", "target_only"}
    counts = results.groupby(["target_class", "unit", "alpha"]).method.nunique()
    assert (counts == 3).all()
