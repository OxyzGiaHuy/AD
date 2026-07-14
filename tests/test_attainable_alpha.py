import numpy as np
import pandas as pd

from scripts.analyze_attainable_alpha import analyze, attainable_alphas, nearest_attainable


def test_attainable_grid_matches_conformal_quantization():
    grid = attainable_alphas(4)
    assert np.allclose(grid, [0.2, 0.4, 0.6, 0.8, 1.0])
    assert nearest_attainable(0.05, 4) == 0.0
    assert nearest_attainable(0.10, 4) == 0.0
    assert nearest_attainable(0.20, 4) == 0.2
    assert abs(nearest_attainable(0.25, 8) - 2.0 / 9.0) < 1e-12


def test_analyze_flags_below_floor_cells():
    frame = pd.DataFrame({
        "dataset": ["mvtec"] * 4,
        "class": ["bottle"] * 4,
        "k_shot": [4] * 4,
        "seed": [0] * 4,
        "corruption": ["clean"] * 4,
        "label": [0, 0, 1, 1],
        "image_p_loio": [0.4, 0.6, 0.2, 0.2],
    })
    result = analyze(frame, "image_p_loio", [0.05, 0.20])
    below = result[result.nominal_alpha == 0.05].iloc[0]
    assert bool(below.below_floor)
    assert below.false_alarm_rate == 0.0
    at_floor = result[result.nominal_alpha == 0.20].iloc[0]
    assert not bool(at_floor.below_floor)
    assert at_floor.detection_rate == 1.0
    assert at_floor.false_alarm_rate == 0.0
