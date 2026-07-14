from __future__ import annotations

import numpy as np
import pytest

pd = pytest.importorskip("pandas")

from scripts.evaluate_source_conditioned_routing import conformalize, evaluate


def test_source_conformal_probability_is_bounded_and_monotonic() -> None:
    source = np.asarray([0.1, 0.2, 0.3, 0.4])
    target = np.asarray([0.15, 0.35])
    p_values = conformalize(source, target)
    assert np.all((p_values >= 0.0) & (p_values <= 1.0))
    assert p_values[0] > p_values[1]


def test_loco_source_archive_excludes_target_class() -> None:
    frame = pd.DataFrame(
        {
            "dataset": ["toy"] * 8,
            "class": ["a"] * 4 + ["b"] * 4,
            "k_shot": [4] * 8,
            "seed": [0] * 8,
            "corruption": ["clean"] * 8,
            "label": [0, 0, 1, 1] * 2,
            "conformal_prob_loio": [0.1, 0.2, 0.8, 0.9, 0.2, 0.3, 0.7, 0.8],
        }
    )
    result = evaluate(frame, "conformal_prob_loio", None, "clean_source", [0.2], [0.5])
    assert not result.empty
    assert set(result["source_normal_count"]) == {2}
