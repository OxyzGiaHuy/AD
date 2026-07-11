from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -40, 40)))


@dataclass
class PlattScaler:
    a: float = 1.0
    b: float = 0.0

    def fit(self, scores: np.ndarray, labels: np.ndarray, lr: float = 0.05, steps: int = 1000) -> "PlattScaler":
        scores = scores.astype(np.float64)
        labels = labels.astype(np.float64)
        a = float(self.a)
        b = float(self.b)
        for _ in range(steps):
            probs = sigmoid(a * scores + b)
            grad = probs - labels
            a -= lr * float(np.mean(grad * scores))
            b -= lr * float(np.mean(grad))
        self.a = a
        self.b = b
        return self

    def predict_proba(self, scores: np.ndarray) -> np.ndarray:
        return sigmoid(self.a * scores.astype(np.float64) + self.b).astype(np.float32)


def entropy_binary(probs: np.ndarray) -> np.ndarray:
    p = np.clip(probs.astype(np.float64), 1e-8, 1.0 - 1e-8)
    return (-(p * np.log(p) + (1.0 - p) * np.log(1.0 - p))).astype(np.float32)



@dataclass
class VectorPlattScaler:
    weights: np.ndarray | None = None
    bias: float = 0.0
    mean: np.ndarray | None = None
    std: np.ndarray | None = None

    def fit(
        self,
        features: np.ndarray,
        labels: np.ndarray,
        lr: float = 0.05,
        steps: int = 2000,
        l2: float = 1e-4,
        positive_indices: tuple[int, ...] = (),
        sample_weight: np.ndarray | None = None,
    ) -> "VectorPlattScaler":
        x = np.asarray(features, dtype=np.float64)
        if x.ndim == 1:
            x = x[:, None]
        y = labels.astype(np.float64)
        sw = np.ones(len(x), dtype=np.float64) if sample_weight is None else np.asarray(sample_weight, dtype=np.float64).reshape(-1)
        sw = np.maximum(sw, 1e-8)
        sw = sw / np.mean(sw)
        self.mean = x.mean(axis=0, keepdims=True)
        self.std = np.maximum(x.std(axis=0, keepdims=True), 1.0)
        z = (x - self.mean) / self.std
        weights = np.zeros(z.shape[1], dtype=np.float64) if self.weights is None else self.weights.astype(np.float64)
        bias = float(self.bias)
        for _ in range(steps):
            probs = sigmoid(z @ weights + bias)
            grad = (probs - y) * sw
            weights -= lr * (z.T @ grad / len(z) + l2 * weights)
            if positive_indices:
                for index in positive_indices:
                    weights[index] = max(0.0, weights[index])
            bias -= lr * float(np.mean(grad))
        probs = sigmoid(z @ weights + bias)
        if np.any(y == 1) and np.any(y == 0) and probs[y == 1].mean() < probs[y == 0].mean():
            weights = -weights
            bias = -bias
        self.weights = weights.astype(np.float32)
        self.bias = bias
        return self

    def predict_proba(self, features: np.ndarray) -> np.ndarray:
        if self.weights is None or self.mean is None or self.std is None:
            raise RuntimeError("VectorPlattScaler must be fit before predict_proba.")
        x = np.asarray(features, dtype=np.float64)
        if x.ndim == 1:
            x = x[:, None]
        z = (x - self.mean) / self.std
        return sigmoid(z @ self.weights.astype(np.float64) + self.bias).astype(np.float32)

    def storage_bytes(self) -> int:
        total = 0
        for item in (self.weights, self.mean, self.std):
            if item is not None:
                total += int(item.nbytes)
        total += np.asarray(self.bias, dtype=np.float32).nbytes
        return int(total)


def reliability_bins(labels: np.ndarray, probs: np.ndarray, bins: int = 15) -> list[dict[str, float]]:
    labels = labels.astype(float)
    probs = np.clip(probs.astype(float), 0.0, 1.0)
    edges = np.linspace(0.0, 1.0, bins + 1)
    rows: list[dict[str, float]] = []
    for index, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
        mask = (probs >= lo) & (probs < hi if hi < 1.0 else probs <= hi)
        count = int(mask.sum())
        rows.append(
            {
                "bin": index,
                "lo": float(lo),
                "hi": float(hi),
                "count": count,
                "confidence": float(probs[mask].mean()) if count else float("nan"),
                "accuracy": float(labels[mask].mean()) if count else float("nan"),
            }
        )
    return rows
