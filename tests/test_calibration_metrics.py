import numpy as np

from src.calibration.platt import PlattScaler, entropy_binary
from src.evaluation.metrics import brier_score, ece_binary, nll_binary, roc_auc_score_np


def test_platt_scaler_monotonic_on_ordered_scores():
    scores = np.array([-2.0, -1.0, 1.0, 2.0], dtype="float32")
    labels = np.array([0, 0, 1, 1], dtype="int64")
    scaler = PlattScaler().fit(scores, labels, steps=200)
    probs = scaler.predict_proba(scores)
    assert np.all(np.diff(probs) >= -1e-6)
    assert probs[-1] > probs[0]
    assert entropy_binary(probs).shape == probs.shape


def test_binary_metrics_on_toy_data():
    labels = np.array([0, 0, 1, 1])
    scores = np.array([0.1, 0.2, 0.8, 0.9])
    assert roc_auc_score_np(labels, scores) == 1.0
    assert ece_binary(labels, scores, bins=2) >= 0.0
    assert brier_score(labels, scores) >= 0.0
    assert nll_binary(labels, scores) >= 0.0

