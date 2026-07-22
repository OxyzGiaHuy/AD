from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations_with_replacement

import numpy as np

from src.evaluation.metrics import brier_score, ece_binary, nll_binary, roc_auc_score_np, average_precision_np


def normalize_weights(weights: np.ndarray) -> np.ndarray:
    w = np.asarray(weights, dtype=np.float64)
    w = np.maximum(w, 0.0)
    s = w.sum()
    if s <= 0.0:
        return np.full_like(w, 1.0 / max(len(w), 1), dtype=np.float64)
    return w / s


def mixture_probs(expert_probs: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return np.clip(np.asarray(expert_probs, dtype=np.float64) @ normalize_weights(weights), 0.0, 1.0)


def grid_simplex(num_experts: int, step: float = 0.25) -> np.ndarray:
    units = int(round(1.0 / step))
    rows = []
    def rec(prefix: list[int], remaining: int, depth: int) -> None:
        if depth == num_experts - 1:
            rows.append(prefix + [remaining])
            return
        for value in range(remaining + 1):
            rec(prefix + [value], remaining - value, depth + 1)
    rec([], units, 0)
    return np.asarray(rows, dtype=np.float64) / max(units, 1)


def choose_best_expert_by_ece(labels: np.ndarray, expert_probs: np.ndarray) -> int:
    eces = [ece_binary(labels, expert_probs[:, i]) for i in range(expert_probs.shape[1])]
    return int(np.nanargmin(eces))


def choose_best_mixture_by_ece(labels: np.ndarray, expert_probs: np.ndarray, step: float = 0.25) -> tuple[np.ndarray, float]:
    best_w = None
    best_ece = float('inf')
    for w in grid_simplex(expert_probs.shape[1], step=step):
        ece = ece_binary(labels, mixture_probs(expert_probs, w))
        if ece < best_ece:
            best_w = w
            best_ece = ece
    assert best_w is not None
    return best_w, best_ece


def risk_ece_weights(labels: np.ndarray, expert_probs: np.ndarray, anchor_index: int = 0, margin: float = 0.005) -> np.ndarray:
    best = choose_best_expert_by_ece(labels, expert_probs)
    anchor_ece = ece_binary(labels, expert_probs[:, anchor_index])
    best_ece = ece_binary(labels, expert_probs[:, best])
    if anchor_ece - best_ece >= margin:
        w = np.zeros(expert_probs.shape[1], dtype=np.float64)
        w[best] = 1.0
        return w
    w = np.zeros(expert_probs.shape[1], dtype=np.float64)
    w[anchor_index] = 1.0
    return w


def sage_hier_ece_weights(labels: np.ndarray, expert_probs: np.ndarray, anchor_index: int = 0, dynamic_indices: list[int] | None = None, strengths: list[float] | None = None) -> tuple[np.ndarray, float]:
    if dynamic_indices is None:
        dynamic_indices = [i for i in range(expert_probs.shape[1]) if i != anchor_index]
    if strengths is None:
        strengths = [0.0, 0.25, 0.5, 0.75, 1.0]
    best_dynamic = dynamic_indices[int(np.nanargmin([ece_binary(labels, expert_probs[:, i]) for i in dynamic_indices]))] if dynamic_indices else anchor_index
    best_w = np.zeros(expert_probs.shape[1], dtype=np.float64)
    best_w[anchor_index] = 1.0
    best_ece = ece_binary(labels, expert_probs[:, anchor_index])
    for strength in strengths:
        w = np.zeros(expert_probs.shape[1], dtype=np.float64)
        w[anchor_index] = 1.0 - strength
        w[best_dynamic] = strength
        ece = ece_binary(labels, mixture_probs(expert_probs, w))
        if ece < best_ece:
            best_w = w
            best_ece = ece
    return best_w, best_ece


def summarize_probs(labels: np.ndarray, raw_scores: np.ndarray, probs: np.ndarray) -> dict[str, float]:
    return {
        'auroc': roc_auc_score_np(labels, raw_scores),
        'ap': average_precision_np(labels, raw_scores),
        'ece': ece_binary(labels, probs),
        'brier': brier_score(labels, probs),
        'nll': nll_binary(labels, probs),
    }


def coverage_mask(risk_scores: np.ndarray, coverage: float) -> np.ndarray:
    risk = np.asarray(risk_scores, dtype=np.float64)
    n_keep = int(np.ceil(len(risk) * float(coverage)))
    n_keep = max(1, min(len(risk), n_keep))
    order = np.argsort(risk, kind='mergesort')
    mask = np.zeros(len(risk), dtype=bool)
    mask[order[:n_keep]] = True
    return mask


def risk_coverage_auc(coverages: np.ndarray, risks: np.ndarray) -> float:
    order = np.argsort(coverages)
    return float(np.trapezoid(np.asarray(risks)[order], np.asarray(coverages)[order]))


def combined_minmax_score(columns: list[np.ndarray]) -> np.ndarray:
    if not columns:
        raise ValueError('At least one risk score column is required.')
    out = np.zeros(len(columns[0]), dtype=np.float64)
    for col in columns:
        x = np.asarray(col, dtype=np.float64)
        lo = np.nanmin(x)
        hi = np.nanmax(x)
        if hi > lo:
            out += (x - lo) / (hi - lo)
    return out / len(columns)
