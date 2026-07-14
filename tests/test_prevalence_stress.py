from __future__ import annotations

import numpy as np
import pytest

pd = pytest.importorskip("pandas")

from scripts.evaluate_prevalence_stress import evaluate, prevalence_sample


def toy_frame() -> pd.DataFrame:
    return pd.DataFrame(
        {
            "dataset": ["toy"] * 20,
            "class": ["part"] * 20,
            "k_shot": [4] * 20,
            "seed": [0] * 20,
            "corruption": ["clean"] * 20,
            "label": [0] * 10 + [1] * 10,
            "prob": np.linspace(0.05, 0.95, 20),
        }
    )


def test_prevalence_sample_matches_requested_prior() -> None:
    sampled = prevalence_sample(toy_frame(), 0.10, np.random.default_rng(0))
    assert len(sampled[sampled["label"] == 0]) == 10
    assert len(sampled[sampled["label"] == 1]) == 1


def test_prevalence_evaluator_keeps_ranking_metrics_valid() -> None:
    result = evaluate(toy_frame(), ["prob"], [0.10, 0.50], repeats=2, bins=5, seed=0)
    assert len(result) == 4
    assert np.all((result["ece"] >= 0.0) & (result["ece"] <= 1.0))
    assert np.allclose(result["auroc"], 1.0)
