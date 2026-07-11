from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass
class PCASubspace:
    mean: np.ndarray
    components: np.ndarray

    @classmethod
    def fit(cls, features: np.ndarray, n_components: int) -> "PCASubspace":
        x = features.reshape(-1, features.shape[-1]).astype(np.float64)
        mean = x.mean(axis=0, keepdims=True)
        centered = x - mean
        _, _, vt = np.linalg.svd(centered, full_matrices=False)
        n = max(1, min(n_components, vt.shape[0]))
        return cls(mean=mean.astype(np.float32), components=vt[:n].astype(np.float32))

    def residual_scores(self, features: np.ndarray) -> np.ndarray:
        original_shape = features.shape[:-1]
        x = features.reshape(-1, features.shape[-1]).astype(np.float32)
        centered = x - self.mean
        projected = centered @ self.components.T @ self.components
        residual = centered - projected
        scores = np.linalg.norm(residual, axis=1)
        return scores.reshape(original_shape)

