import numpy as np

from scripts.analyze_calibrator_significance import holm_adjust


def test_holm_adjustment_is_monotone_in_sorted_order_and_not_smaller():
    p_values = np.asarray([0.04, 0.001, 0.02, 0.5])
    adjusted = holm_adjust(p_values)
    assert np.all(adjusted >= p_values)
    order = np.argsort(p_values)
    assert np.all(np.diff(adjusted[order]) >= 0)
    assert np.all(adjusted <= 1.0)


def test_holm_adjustment_preserves_nan():
    adjusted = holm_adjust(np.asarray([0.01, np.nan, 0.02]))
    assert np.isnan(adjusted[1])
    assert np.allclose(adjusted[[0, 2]], [0.02, 0.02])
