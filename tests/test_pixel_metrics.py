from __future__ import annotations

import numpy as np

from src.evaluation.pixel_metrics import connected_components, pro_auc_score, resize_score_map, summarize_pixel


def test_connected_components_counts_regions():
    mask = np.zeros((5, 5), dtype=bool)
    mask[0, 0] = True
    mask[3:5, 3:5] = True
    comps = connected_components(mask)
    assert len(comps) == 2
    assert sorted(int(c.sum()) for c in comps) == [1, 4]


def test_summarize_pixel_toy_perfect_scores():
    mask = np.array([[0, 1], [0, 1]], dtype=bool)
    score = np.array([[0.1, 0.9], [0.2, 0.8]], dtype=np.float32)
    summary = summarize_pixel([mask], [score])
    assert summary["pixel_auroc"] == 1.0
    assert summary["pixel_ap"] == 1.0
    assert summary["max_pixel_f1"] == 1.0


def test_pro_auc_returns_unit_interval():
    masks = [np.array([[0, 1], [0, 1]], dtype=bool), np.zeros((2, 2), dtype=bool)]
    scores = [np.array([[0.1, 0.9], [0.1, 0.8]], dtype=np.float32), np.zeros((2, 2), dtype=np.float32)]
    value = pro_auc_score(masks, scores, steps=10)
    assert 0.0 <= value <= 1.0
