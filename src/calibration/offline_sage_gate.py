from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np


def standardize_train_test(x_train: np.ndarray, x_test: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    mean = x_train.mean(axis=0, keepdims=True)
    std = x_train.std(axis=0, keepdims=True)
    std = np.where(std < 1e-8, 1.0, std)
    return (x_train - mean) / std, (x_test - mean) / std, mean.reshape(-1), std.reshape(-1)


class SoftmaxLinearGate:
    """Tiny dependency-free multinomial logistic gate for offline routing tests."""

    def __init__(self, lr: float = 0.05, steps: int = 2500, l2: float = 1e-3, seed: int = 0):
        self.lr = lr
        self.steps = steps
        self.l2 = l2
        self.seed = seed
        self.weights: np.ndarray | None = None

    def fit(self, x: np.ndarray, y: np.ndarray, sample_weight: np.ndarray | None = None) -> "SoftmaxLinearGate":
        x = np.asarray(x, dtype=np.float64)
        y = np.asarray(y, dtype=np.int64)
        n, d = x.shape
        k = int(y.max()) + 1 if len(y) else 1
        xb = np.concatenate([np.ones((n, 1), dtype=np.float64), x], axis=1)
        rng = np.random.default_rng(self.seed)
        w = rng.normal(scale=0.01, size=(d + 1, k))
        target = np.zeros((n, k), dtype=np.float64)
        target[np.arange(n), y] = 1.0
        sw = np.ones(n, dtype=np.float64) if sample_weight is None else np.asarray(sample_weight, dtype=np.float64)
        sw = sw / max(sw.mean(), 1e-12)
        for _ in range(self.steps):
            logits = xb @ w
            logits -= logits.max(axis=1, keepdims=True)
            probs = np.exp(logits)
            probs /= np.maximum(probs.sum(axis=1, keepdims=True), 1e-12)
            grad = xb.T @ ((probs - target) * sw[:, None]) / max(n, 1)
            grad[1:] += self.l2 * w[1:]
            w -= self.lr * grad
        self.weights = w
        return self

    def predict_proba(self, x: np.ndarray) -> np.ndarray:
        if self.weights is None:
            raise RuntimeError("Gate has not been fit.")
        x = np.asarray(x, dtype=np.float64)
        xb = np.concatenate([np.ones((len(x), 1), dtype=np.float64), x], axis=1)
        logits = xb @ self.weights
        logits -= logits.max(axis=1, keepdims=True)
        probs = np.exp(logits)
        return probs / np.maximum(probs.sum(axis=1, keepdims=True), 1e-12)

    def predict(self, x: np.ndarray) -> np.ndarray:
        return self.predict_proba(x).argmax(axis=1)


class RidgeECERegressor:
    """Multi-output ridge regressor that predicts per-expert ECE for safe routing."""

    def __init__(self, l2: float = 1e-2):
        self.l2 = l2
        self.coef: np.ndarray | None = None

    def fit(self, x: np.ndarray, y: np.ndarray) -> "RidgeECERegressor":
        x = np.asarray(x, dtype=np.float64)
        y = np.asarray(y, dtype=np.float64)
        xb = np.concatenate([np.ones((len(x), 1), dtype=np.float64), x], axis=1)
        eye = np.eye(xb.shape[1], dtype=np.float64)
        eye[0, 0] = 0.0
        self.coef = np.linalg.pinv(xb.T @ xb + self.l2 * eye) @ xb.T @ y
        return self

    def predict(self, x: np.ndarray) -> np.ndarray:
        if self.coef is None:
            raise RuntimeError("Regressor has not been fit.")
        xb = np.concatenate([np.ones((len(x), 1), dtype=np.float64), x], axis=1)
        return xb @ self.coef


def risk_aware_choice(predicted_ece: np.ndarray, anchor_index: int, margin: float = 0.005) -> np.ndarray:
    pred = np.asarray(predicted_ece, dtype=np.float64)
    best = pred.argmin(axis=1)
    anchor = pred[:, anchor_index]
    chosen = np.full(len(pred), anchor_index, dtype=np.int64)
    gain = anchor - pred[np.arange(len(pred)), best]
    chosen[gain > margin] = best[gain > margin]
    return chosen


def hierarchical_shared_dynamic_choice(
    dynamic_probs: np.ndarray,
    dynamic_expert_probs: np.ndarray,
    expert_indices: Iterable[int],
    anchor_index: int,
    threshold: float = 0.55,
) -> np.ndarray:
    """SAGE-like two-stage routing: shared anchor gate, then dynamic top-1 expert."""

    dynamic_probs = np.asarray(dynamic_probs, dtype=np.float64).reshape(-1)
    dynamic_expert_probs = np.asarray(dynamic_expert_probs, dtype=np.float64)
    expert_indices = np.asarray(list(expert_indices), dtype=np.int64)
    chosen = np.full(len(dynamic_probs), anchor_index, dtype=np.int64)
    use_dynamic = dynamic_probs >= threshold
    if dynamic_expert_probs.size:
        chosen[use_dynamic] = expert_indices[dynamic_expert_probs[use_dynamic].argmax(axis=1)]
    return chosen


def topk_soft_choice(probs: np.ndarray, expert_values: np.ndarray, k: int = 2) -> np.ndarray:
    """Return expected value of top-k routed experts for metric-level analysis."""

    probs = np.asarray(probs, dtype=np.float64)
    values = np.asarray(expert_values, dtype=np.float64)
    k = max(1, min(k, probs.shape[1]))
    out = np.zeros(len(probs), dtype=np.float64)
    for i in range(len(probs)):
        idx = np.argsort(probs[i])[-k:]
        w = probs[i, idx]
        w = w / max(w.sum(), 1e-12)
        out[i] = float(np.sum(w * values[i, idx]))
    return out


class BrierMixtureGate:
    """Linear softmax mixture gate trained directly on probability quality.

    Unlike the oracle-label gate, this optimizes the final mixed probability
    p = sum_e gate_e(x) p_e. It is useful for calibration objectives because
    the target is the probability itself, not a discrete expert id.
    """

    def __init__(self, lr: float = 0.03, steps: int = 2000, l2: float = 1e-3, no_harm: float = 0.0, anchor_reg: float = 0.0, seed: int = 0):
        self.lr = lr
        self.steps = steps
        self.l2 = l2
        self.no_harm = no_harm
        self.anchor_reg = anchor_reg
        self.seed = seed
        self.weights: np.ndarray | None = None

    def fit(self, x: np.ndarray, expert_probs: np.ndarray, y: np.ndarray, anchor_index: int = 0) -> "BrierMixtureGate":
        x = np.asarray(x, dtype=np.float64)
        probs_in = np.asarray(expert_probs, dtype=np.float64)
        y = np.asarray(y, dtype=np.float64).reshape(-1)
        n, d = x.shape
        k = probs_in.shape[1]
        xb = np.concatenate([np.ones((n, 1), dtype=np.float64), x], axis=1)
        rng = np.random.default_rng(self.seed)
        w = rng.normal(scale=0.01, size=(d + 1, k))
        # Start near the safe anchor, not uniform. This mirrors SAGE shared-path stability.
        w[0, :] = -1.0
        w[0, anchor_index] = 1.0
        anchor_prob = probs_in[:, anchor_index]
        anchor_brier = (anchor_prob - y) ** 2
        for _ in range(self.steps):
            logits = xb @ w
            logits -= logits.max(axis=1, keepdims=True)
            gate = np.exp(logits)
            gate /= np.maximum(gate.sum(axis=1, keepdims=True), 1e-12)
            mixed = np.sum(gate * probs_in, axis=1)
            d_mixed = 2.0 * (mixed - y) / max(n, 1)
            if self.no_harm > 0.0:
                mixed_brier = (mixed - y) ** 2
                active = mixed_brier > anchor_brier
                d_mixed = d_mixed + self.no_harm * active.astype(np.float64) * 2.0 * (mixed - y) / max(n, 1)
            if self.anchor_reg > 0.0:
                d_mixed = d_mixed + self.anchor_reg * 2.0 * (mixed - anchor_prob) / max(n, 1)
            # softmax Jacobian-vector product for each sample.
            d_gate = d_mixed[:, None] * probs_in
            dot = np.sum(d_gate * gate, axis=1, keepdims=True)
            d_logits = gate * (d_gate - dot)
            grad = xb.T @ d_logits
            grad[1:] += self.l2 * w[1:]
            w -= self.lr * grad
        self.weights = w
        return self

    def predict_weights(self, x: np.ndarray) -> np.ndarray:
        if self.weights is None:
            raise RuntimeError("Gate has not been fit.")
        x = np.asarray(x, dtype=np.float64)
        xb = np.concatenate([np.ones((len(x), 1), dtype=np.float64), x], axis=1)
        logits = xb @ self.weights
        logits -= logits.max(axis=1, keepdims=True)
        gate = np.exp(logits)
        return gate / np.maximum(gate.sum(axis=1, keepdims=True), 1e-12)

    def predict_proba(self, x: np.ndarray, expert_probs: np.ndarray) -> np.ndarray:
        weights = self.predict_weights(x)
        return np.clip(np.sum(weights * np.asarray(expert_probs, dtype=np.float64), axis=1), 0.0, 1.0)


@dataclass
class GateEvaluation:
    name: str
    dataset: str
    split: str
    n_cases: int
    mean_ece: float
    mean_delta_vs_vector: float
    no_harm_count: int
    no_harm_total: int
    usage: dict[str, int]
