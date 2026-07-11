import numpy as np

from src.calibration.platt import VectorPlattScaler, reliability_bins


def test_vector_platt_learns_ordered_toy_data():
    x = np.array([[0.0, 0.1, 0.1], [0.2, 0.1, 0.1], [1.0, 0.9, 0.1], [1.2, 1.0, 0.2]], dtype="float32")
    y = np.array([0, 0, 1, 1], dtype="int64")
    scaler = VectorPlattScaler().fit(x, y, steps=400)
    probs = scaler.predict_proba(x)
    assert probs[-1] > probs[0]
    assert scaler.storage_bytes() > 0
    bins = reliability_bins(y, probs, bins=2)
    assert len(bins) == 2


def test_vector_platt_positive_constraint_keeps_weight_nonnegative():
    x = np.array([[0.0, 1.0], [1.0, 0.0]], dtype="float32")
    y = np.array([1, 0], dtype="int64")
    scaler = VectorPlattScaler().fit(x, y, steps=50, positive_indices=(0,))
    assert scaler.weights[0] >= 0.0
