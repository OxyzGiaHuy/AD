from __future__ import annotations

import numpy as np


def roc_auc_score_np(labels: np.ndarray, scores: np.ndarray) -> float:
    labels = labels.astype(int)
    scores = scores.astype(float)
    n_pos = int(np.sum(labels == 1))
    n_neg = int(np.sum(labels == 0))
    if n_pos == 0 or n_neg == 0:
        return float("nan")
    order = np.argsort(scores, kind="mergesort")
    sorted_scores = scores[order]
    ranks = np.empty(len(scores), dtype=np.float64)
    start = 0
    while start < len(scores):
        end = start + 1
        while end < len(scores) and sorted_scores[end] == sorted_scores[start]:
            end += 1
        avg_rank = 0.5 * (start + 1 + end)
        ranks[order[start:end]] = avg_rank
        start = end
    rank_sum_pos = float(np.sum(ranks[labels == 1]))
    return (rank_sum_pos - n_pos * (n_pos + 1) / 2.0) / (n_pos * n_neg)


def average_precision_np(labels: np.ndarray, scores: np.ndarray) -> float:
    labels = labels.astype(int)
    order = np.argsort(-scores)
    y = labels[order]
    positives = y.sum()
    if positives == 0:
        return float("nan")
    tp = np.cumsum(y)
    precision = tp / (np.arange(len(y)) + 1)
    return float((precision * y).sum() / positives)


def max_f1_np(labels: np.ndarray, scores: np.ndarray) -> float:
    labels = labels.astype(int)
    thresholds = np.unique(scores)
    best = 0.0
    for threshold in thresholds:
        pred = scores >= threshold
        tp = float(np.sum((pred == 1) & (labels == 1)))
        fp = float(np.sum((pred == 1) & (labels == 0)))
        fn = float(np.sum((pred == 0) & (labels == 1)))
        denom = 2 * tp + fp + fn
        if denom > 0:
            best = max(best, 2 * tp / denom)
    return best


def ece_binary(labels: np.ndarray, probs: np.ndarray, bins: int = 15) -> float:
    labels = labels.astype(float)
    probs = np.clip(probs.astype(float), 0.0, 1.0)
    edges = np.linspace(0.0, 1.0, bins + 1)
    total = len(labels)
    if total == 0:
        return float("nan")
    ece = 0.0
    for lo, hi in zip(edges[:-1], edges[1:]):
        mask = (probs >= lo) & (probs < hi if hi < 1.0 else probs <= hi)
        if np.any(mask):
            conf = probs[mask].mean()
            acc = labels[mask].mean()
            ece += float(mask.mean()) * abs(conf - acc)
    return ece


def brier_score(labels: np.ndarray, probs: np.ndarray) -> float:
    return float(np.mean((probs.astype(float) - labels.astype(float)) ** 2))


def nll_binary(labels: np.ndarray, probs: np.ndarray) -> float:
    p = np.clip(probs.astype(float), 1e-8, 1.0 - 1e-8)
    y = labels.astype(float)
    return float(-np.mean(y * np.log(p) + (1.0 - y) * np.log(1.0 - p)))


def summarize_binary(labels: np.ndarray, raw_scores: np.ndarray, probs: np.ndarray, bins: int = 15) -> dict[str, float]:
    return {
        "auroc": roc_auc_score_np(labels, raw_scores),
        "ap": average_precision_np(labels, raw_scores),
        "max_f1": max_f1_np(labels, raw_scores),
        "ece": ece_binary(labels, probs, bins=bins),
        "brier": brier_score(labels, probs),
        "nll": nll_binary(labels, probs),
    }

