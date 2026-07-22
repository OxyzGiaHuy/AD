from __future__ import annotations

import numpy as np

from src.calibration.gated import ShiftGateSummary, anchored_gated_probabilities, gated_probabilities, noise_safe_soft_gate, no_harm_gate_strength, structured_shift_gate
from src.calibration.platt import VectorPlattScaler
from src.calibration.offline_sage_gate import BrierMixtureGate, RidgeECERegressor, SoftmaxLinearGate, hierarchical_shared_dynamic_choice, risk_aware_choice, standardize_train_test
from src.conformal import (
    conformal_p_values,
    effective_sample_size,
    loio_calibration,
    matched_loio_image_p_values,
    weighted_conformal_p_values,
)


def test_conformal_p_values_decrease_with_larger_residuals() -> None:
    calibration = np.asarray([0.1, 0.2, 0.3, 0.4], dtype=np.float32)
    tests = np.asarray([0.15, 0.35], dtype=np.float32)
    p_values = conformal_p_values(calibration, tests)
    assert p_values[0] > p_values[1]
    assert np.all((p_values >= 0.0) & (p_values <= 1.0))


def test_loio_calibration_shapes_for_few_shot() -> None:
    rng = np.random.default_rng(0)
    features = rng.normal(size=(3, 8, 6)).astype(np.float32)
    cal = loio_calibration(features, pca_components=2)
    assert cal.patch_scores.shape == (24,)
    assert cal.patch_covariates.shape[0] == 24
    assert cal.image_scores.shape == (3,)
    assert cal.mode == "loio_conformal"


def test_matched_loio_uses_fold_specific_test_scores() -> None:
    rng = np.random.default_rng(13)
    support = rng.normal(size=(4, 8, 5)).astype(np.float32)
    test = np.stack([
        rng.normal(size=(8, 5)),
        rng.normal(loc=8.0, size=(8, 5)),
    ]).astype(np.float32)
    result = matched_loio_image_p_values(support, test, pca_components=2)
    assert result.test_scores_by_fold.shape == (4, 2)
    assert result.calibration_scores.shape == (4,)
    assert result.attainable_alpha == 0.2
    assert np.all((result.p_values >= 0.2) & (result.p_values <= 1.0))
    assert result.p_values[1] <= result.p_values[0]


def test_k1_spatial_split_does_not_reuse_all_patches() -> None:
    rng = np.random.default_rng(1)
    features = rng.normal(size=(1, 10, 5)).astype(np.float32)
    cal = loio_calibration(features, pca_components=2)
    assert 0 < len(cal.patch_scores) < features.shape[1]
    assert cal.mode == "patch_split_conformal"


def test_weighted_p_values_and_effective_sample_size_bounds() -> None:
    calibration = np.asarray([0.1, 0.2, 0.3], dtype=np.float32)
    tests = np.asarray([0.15, 0.35], dtype=np.float32)
    weights = np.asarray([1.0, 2.0, 4.0], dtype=np.float32)
    p_values = weighted_conformal_p_values(calibration, tests, weights)
    assert np.all((p_values >= 0.0) & (p_values <= 1.0))
    n_eff = effective_sample_size(weights)
    assert 1.0 <= n_eff <= len(weights)


def test_vector_platt_accepts_sample_weights_and_is_monotonic() -> None:
    x = np.asarray([[0.0], [1.0], [2.0], [3.0]], dtype=np.float32)
    y = np.asarray([0, 0, 1, 1], dtype=np.float32)
    sw = np.asarray([1.0, 1.0, 2.0, 2.0], dtype=np.float32)
    cal = VectorPlattScaler().fit(x, y, steps=300, sample_weight=sw, positive_indices=(0,))
    probs = cal.predict_proba(x)
    assert probs[-1] > probs[0]


def test_gate_weights_sum_to_one_and_gated_probability_is_valid() -> None:
    expert_names = ["vector_platt", "shift_aware_vector_platt", "weighted_platt"]
    hard = structured_shift_gate("blur", expert_names)
    assert np.isclose(hard.sum(), 1.0)
    summary = ShiftGateSummary(domain_confidence=0.8, n_eff_ratio=0.7, pca_concentration=2.0, residual_std=1.0)
    soft = noise_safe_soft_gate(summary, expert_names)
    assert np.isclose(soft.sum(), 1.0)
    probs = gated_probabilities(np.asarray([[0.2, 0.8, 0.5]], dtype=np.float32), soft)
    assert probs.shape == (1,)
    assert 0.0 <= probs[0] <= 1.0


def test_anchored_gate_stays_between_anchor_and_mixture() -> None:
    anchor = np.asarray([0.2, 0.8], dtype=np.float32)
    expert_probs = np.asarray([[0.2, 0.9], [0.8, 0.1]], dtype=np.float32)
    weights = np.asarray([0.0, 1.0], dtype=np.float32)
    out = anchored_gated_probabilities(anchor, expert_probs, weights, strength=0.25)
    assert np.all((out >= 0.0) & (out <= 1.0))
    assert np.allclose(out, anchor + 0.25 * (expert_probs[:, 1] - anchor))


def test_no_harm_gate_strength_is_conservative() -> None:
    summary = ShiftGateSummary(domain_confidence=0.9, n_eff_ratio=1.0, pca_concentration=2.0, residual_std=1.0)
    assert 0.0 <= no_harm_gate_strength(summary) <= 0.35

def test_offline_sage_gate_shapes_and_choices() -> None:
    x = np.asarray([[0.0, 0.0], [0.1, 0.2], [1.0, 1.0], [1.2, 0.9]], dtype=np.float32)
    y = np.asarray([0, 0, 1, 1], dtype=np.int64)
    gate = SoftmaxLinearGate(steps=100, lr=0.1).fit(x, y)
    probs = gate.predict_proba(x)
    assert probs.shape == (4, 2)
    assert np.allclose(probs.sum(axis=1), 1.0)

    ece = np.asarray([[0.2, 0.1], [0.1, 0.3], [0.4, 0.2], [0.3, 0.5]], dtype=np.float32)
    reg = RidgeECERegressor().fit(x, ece)
    pred = reg.predict(x)
    choice = risk_aware_choice(pred, anchor_index=0, margin=0.0)
    assert choice.shape == (4,)
    assert set(choice.tolist()) <= {0, 1}

    hierarchical = hierarchical_shared_dynamic_choice(
        dynamic_probs=np.asarray([0.1, 0.9], dtype=np.float32),
        dynamic_expert_probs=np.asarray([[0.8], [0.7]], dtype=np.float32),
        expert_indices=[1],
        anchor_index=0,
        threshold=0.5,
    )
    assert hierarchical.tolist() == [0, 1]


def test_standardize_train_test_uses_train_statistics() -> None:
    train = np.asarray([[1.0, 2.0], [3.0, 2.0]], dtype=np.float32)
    test = np.asarray([[5.0, 2.0]], dtype=np.float32)
    train_z, test_z, mean, std = standardize_train_test(train, test)
    assert np.allclose(train_z.mean(axis=0), 0.0)
    assert np.isfinite(test_z).all()
    assert std[1] == 1.0

def test_brier_mixture_gate_outputs_valid_probabilities() -> None:
    x = np.asarray([[0.0], [0.2], [1.0], [1.2]], dtype=np.float32)
    expert_probs = np.asarray([[0.1, 0.4], [0.2, 0.5], [0.8, 0.6], [0.9, 0.7]], dtype=np.float32)
    y = np.asarray([0, 0, 1, 1], dtype=np.int64)
    gate = BrierMixtureGate(steps=100, lr=0.1, no_harm=1.0).fit(x, expert_probs, y, anchor_index=0)
    weights = gate.predict_weights(x)
    probs = gate.predict_proba(x, expert_probs)
    assert weights.shape == expert_probs.shape
    assert np.allclose(weights.sum(axis=1), 1.0)
    assert np.all((probs >= 0.0) & (probs <= 1.0))
