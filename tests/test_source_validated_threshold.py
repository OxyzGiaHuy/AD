import numpy as np
import pandas as pd

from scripts.evaluate_source_validated_threshold import (
    conservative_threshold,
    evaluate_target_only,
    source_validated_threshold,
)


def test_conservative_threshold_respects_empirical_alpha():
    values = np.linspace(0.01, 1.0, 100)
    threshold = conservative_threshold(values, 0.1)
    assert np.mean(values <= threshold) <= 0.1
    assert threshold > 0


def test_source_validation_uses_held_out_classes():
    frame = pd.DataFrame({
        "class": ["a"] * 5 + ["b"] * 5 + ["c"] * 5,
        "score": np.linspace(0.0, 1.0, 15),
    })
    threshold, far, count = source_validated_threshold(frame, "score", 0.2)
    assert 0.0 <= threshold <= 1.0
    assert far <= 0.2
    assert count == 15


def test_target_only_respects_attainable_alpha_floor():
    frame = pd.DataFrame({
        "dataset": ["mvtec"] * 6,
        "class": ["bottle"] * 6,
        "k_shot": [4] * 6,
        "seed": [0] * 6,
        "corruption": ["clean"] * 6,
        "label": [0, 0, 0, 1, 1, 1],
        "raw_score": [0.1, 0.2, 0.3, 5.0, 6.0, 7.0],
    })
    residuals = pd.DataFrame({
        "dataset": ["mvtec"] * 4,
        "class": ["bottle"] * 4,
        "k_shot": [4] * 4,
        "seed": [0] * 4,
        "residual_index": [0, 1, 2, 3],
        "loio_residual": [0.5, 0.6, 0.7, 0.8],
    })
    result = evaluate_target_only(frame, residuals, [0.05, 0.10, 0.20])
    assert set(result["method"]) == {"target_only"}
    below_floor = result[result.alpha < 1.0 / 5.0]
    # k=4 support gives a minimum attainable p-value of 1/(k+1)=0.2, so no alarms below it
    assert (below_floor.power == 0.0).all()
    assert (below_floor.false_alarm_rate == 0.0).all()
    at_floor = result[result.alpha == 0.20].iloc[0]
    # anomaly scores exceed all support residuals -> p=0.2 -> alarms fire exactly at the floor
    assert at_floor.power == 1.0
    assert at_floor.false_alarm_rate == 0.0


def _two_dataset_frame():
    rows = []
    rng = np.random.default_rng(0)
    for dataset, classes in [("mvtec", ["a", "b", "c"]), ("visa", ["x", "y", "z"])]:
        for cls in classes:
            for label in [0, 1]:
                for i in range(6):
                    rows.append({
                        "dataset": dataset,
                        "class": cls,
                        "k_shot": 4,
                        "seed": 0,
                        "corruption": "clean",
                        "label": label,
                        "score": float(rng.normal(0.0 if label == 0 else 4.0, 1.0)),
                    })
    return pd.DataFrame(rows)


def test_evaluate_cross_dataset_source_pool():
    from scripts.evaluate_source_validated_threshold import evaluate

    frame = _two_dataset_frame()
    result = evaluate(frame, "score", "matched_condition", [0.2], source_dataset="mvtec", target_dataset="visa")
    # Only visa targets are evaluated, and every row records the mvtec source pool.
    assert set(result["dataset"]) == {"visa"}
    assert set(result["source_dataset"]) == {"mvtec"}
    assert set(result["class"]) == {"x", "y", "z"}


def test_evaluate_default_stays_within_dataset():
    from scripts.evaluate_source_validated_threshold import evaluate

    frame = _two_dataset_frame()
    result = evaluate(frame, "score", "matched_condition", [0.2])
    assert set(result["dataset"]) == {"mvtec", "visa"}
    assert (result["source_dataset"] == result["dataset"]).all()
