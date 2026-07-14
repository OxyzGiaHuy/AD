import numpy as np

from src.calibration.scalar import (
    HistogramBinningCalibrator,
    IsotonicCalibrator,
    TemperatureScaler,
    build_scalar_calibrator,
)
from src.models.head_pca import make_synthetic_feature_batch


def _toy_calibration_set(n: int = 8, seed: int = 0):
    rng = np.random.default_rng(seed)
    neg = rng.normal(10.0, 1.0, size=n)
    pos = rng.normal(16.0, 1.0, size=n)
    scores = np.concatenate([neg, pos])
    labels = np.concatenate([np.zeros(n), np.ones(n)])
    return scores, labels


def test_temperature_scaler_separates_classes():
    scores, labels = _toy_calibration_set()
    scaler = TemperatureScaler().fit(scores, labels)
    probs = scaler.predict_proba(scores)
    assert probs[labels == 1].mean() > probs[labels == 0].mean()
    assert scaler.temperature > 0
    # Monotone in the score.
    grid = np.linspace(scores.min(), scores.max(), 50)
    p = scaler.predict_proba(grid)
    assert np.all(np.diff(p) >= -1e-9)


def test_temperature_scaler_centers_between_class_means():
    scores, labels = _toy_calibration_set()
    scaler = TemperatureScaler().fit(scores, labels)
    lo = scores[labels == 0].mean()
    hi = scores[labels == 1].mean()
    assert lo < scaler.center < hi


def test_isotonic_calibrator_monotone_and_bounded():
    scores, labels = _toy_calibration_set()
    calibrator = IsotonicCalibrator().fit(scores, labels)
    grid = np.linspace(scores.min() - 5, scores.max() + 5, 100)
    probs = calibrator.predict_proba(grid)
    assert np.all(np.diff(probs) >= -1e-9)
    assert probs.min() >= 0.0 and probs.max() <= 1.0
    # Out-of-range inputs clip instead of failing.
    assert calibrator.predict_proba(np.array([1e9]))[0] <= 1.0


def test_histogram_binning_small_sample():
    # k=4 few-shot regime: 4 normals + 4 synthetics.
    scores = np.array([10.0, 10.5, 11.0, 11.5, 15.0, 15.5, 16.0, 16.5])
    labels = np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype=float)
    calibrator = HistogramBinningCalibrator().fit(scores, labels)
    probs = calibrator.predict_proba(scores)
    assert probs[labels == 1].mean() > probs[labels == 0].mean()
    assert probs.min() >= 0.0 and probs.max() <= 1.0
    # Values far outside the calibration range map to the edge bins.
    assert calibrator.predict_proba(np.array([0.0]))[0] == probs[0]
    assert calibrator.predict_proba(np.array([100.0]))[0] == probs[-1]


def test_histogram_binning_constant_scores():
    scores = np.full(6, 3.0)
    labels = np.array([0, 0, 0, 1, 1, 1], dtype=float)
    calibrator = HistogramBinningCalibrator().fit(scores, labels)
    probs = calibrator.predict_proba(np.array([3.0, 5.0]))
    assert np.all((probs >= 0.0) & (probs <= 1.0))


def test_build_scalar_calibrator_names():
    for name in ["temperature", "isotonic", "histogram_binning", "scalar_platt"]:
        calibrator = build_scalar_calibrator(name)
        scores, labels = _toy_calibration_set()
        calibrator.fit(scores, labels)
        probs = calibrator.predict_proba(scores)
        assert probs.shape == scores.shape
        assert probs[labels == 1].mean() > probs[labels == 0].mean(), name


def test_make_synthetic_feature_batch_matches_method():
    from src.models.head_pca import CalibSubspaceHead

    rng = np.random.default_rng(0)
    feats = rng.normal(size=(4, 16, 8)).astype(np.float32)
    module_batch = make_synthetic_feature_batch(feats, seed=3, ratio=1.0)
    model = CalibSubspaceHead.fit(feats, pca_components=2, seed=0, head_type="linear")
    method_batch = model._make_synthetic_feature_batch(feats, seed=3, ratio=1.0)
    np.testing.assert_allclose(module_batch, method_batch)
    assert module_batch.shape == feats.shape
