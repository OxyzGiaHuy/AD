from __future__ import annotations

import numpy as np

from src.evaluation.reliability_routing import (
    choose_best_expert_by_ece,
    choose_best_mixture_by_ece,
    coverage_mask,
    grid_simplex,
    mixture_probs,
    risk_coverage_auc,
    risk_ece_weights,
)


def test_grid_ece_selects_good_expert_on_toy_data() -> None:
    labels = np.asarray([0, 0, 1, 1], dtype=np.int64)
    probs = np.asarray([[0.1, 0.4], [0.2, 0.5], [0.8, 0.6], [0.9, 0.7]], dtype=np.float32)
    assert choose_best_expert_by_ece(labels, probs) == 0
    weights, ece = choose_best_mixture_by_ece(labels, probs, step=0.5)
    assert weights.shape == (2,)
    assert np.isclose(weights.sum(), 1.0)
    assert ece >= 0.0


def test_risk_ece_gate_falls_back_to_anchor_when_gain_small() -> None:
    labels = np.asarray([0, 1], dtype=np.int64)
    probs = np.asarray([[0.2, 0.21], [0.8, 0.79]], dtype=np.float32)
    weights = risk_ece_weights(labels, probs, anchor_index=0, margin=0.1)
    assert weights.tolist() == [1.0, 0.0]


def test_coverage_mask_keeps_requested_fraction() -> None:
    risk = np.asarray([0.4, 0.1, 0.3, 0.2], dtype=np.float32)
    mask = coverage_mask(risk, 0.5)
    assert mask.sum() == 2
    assert mask[1] and mask[3]


def test_risk_coverage_auc_is_finite() -> None:
    auc = risk_coverage_auc(np.asarray([1.0, 0.8, 0.6]), np.asarray([0.2, 0.15, 0.1]))
    assert np.isfinite(auc)


def test_mixture_probs_are_valid() -> None:
    probs = np.asarray([[0.1, 0.9], [0.2, 0.8]], dtype=np.float32)
    mixed = mixture_probs(probs, np.asarray([0.25, 0.75]))
    assert np.all((mixed >= 0.0) & (mixed <= 1.0))
