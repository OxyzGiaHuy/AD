"""Standard scalar score-to-probability calibrators.

These are the classical calibration baselines requested for the journal
comparison: temperature scaling, isotonic regression, and histogram binning.
All of them map a scalar anomaly score to a probability and are fit on the
same label-free calibration set as the Platt-family calibrators (k support
normal scores labeled 0 plus synthetic-anomaly scores labeled 1), so the
comparison against LOIO conformal reliability is information-symmetric.

Raw anomaly scores are PCA residual magnitudes, not logits, so temperature
scaling is applied after centering at the midpoint between the calibration
class means: p = sigmoid((s - c) / T). The single learned parameter is T; the
center c is a fixed function of the calibration set. This is the standard
adaptation of Guo et al. (2017) temperature scaling to score inputs and is
disclosed in the paper.
"""
from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .platt import sigmoid


@dataclass
class TemperatureScaler:
    temperature: float = 1.0
    center: float = 0.0

    def fit(self, scores: np.ndarray, labels: np.ndarray) -> "TemperatureScaler":
        s = np.asarray(scores, dtype=np.float64).reshape(-1)
        y = np.asarray(labels, dtype=np.float64).reshape(-1)
        pos = s[y == 1]
        neg = s[y == 0]
        if len(pos) and len(neg):
            self.center = 0.5 * (float(pos.mean()) + float(neg.mean()))
        else:
            self.center = float(s.mean()) if len(s) else 0.0
        z = s - self.center
        best_t, best_nll = 1.0, float("inf")
        for log_t in np.linspace(-4.0, 4.0, 321):
            t = float(np.exp(log_t))
            p = np.clip(sigmoid(z / t), 1e-7, 1.0 - 1e-7)
            nll = float(-np.mean(y * np.log(p) + (1.0 - y) * np.log(1.0 - p)))
            if nll < best_nll:
                best_t, best_nll = t, nll
        self.temperature = best_t
        return self

    def predict_proba(self, scores: np.ndarray) -> np.ndarray:
        z = np.asarray(scores, dtype=np.float64).reshape(-1) - self.center
        return sigmoid(z / self.temperature).astype(np.float32)


@dataclass
class IsotonicCalibrator:
    model: object | None = None
    fallback: float = 0.5

    def fit(self, scores: np.ndarray, labels: np.ndarray) -> "IsotonicCalibrator":
        from sklearn.isotonic import IsotonicRegression

        s = np.asarray(scores, dtype=np.float64).reshape(-1)
        y = np.asarray(labels, dtype=np.float64).reshape(-1)
        self.fallback = float(y.mean()) if len(y) else 0.5
        model = IsotonicRegression(y_min=0.0, y_max=1.0, increasing=True, out_of_bounds="clip")
        model.fit(s, y)
        self.model = model
        return self

    def predict_proba(self, scores: np.ndarray) -> np.ndarray:
        if self.model is None:
            raise RuntimeError("IsotonicCalibrator must be fit before predict_proba.")
        s = np.asarray(scores, dtype=np.float64).reshape(-1)
        p = np.asarray(self.model.predict(s), dtype=np.float64)
        p = np.where(np.isfinite(p), p, self.fallback)
        return np.clip(p, 0.0, 1.0).astype(np.float32)


@dataclass
class HistogramBinningCalibrator:
    edges: np.ndarray = field(default_factory=lambda: np.array([0.0, 1.0]))
    bin_probs: np.ndarray = field(default_factory=lambda: np.array([0.5]))

    def fit(self, scores: np.ndarray, labels: np.ndarray, bins: int = 10) -> "HistogramBinningCalibrator":
        s = np.asarray(scores, dtype=np.float64).reshape(-1)
        y = np.asarray(labels, dtype=np.float64).reshape(-1)
        n_bins = int(max(1, min(bins, len(s) // 2 if len(s) >= 2 else 1)))
        quantiles = np.linspace(0.0, 1.0, n_bins + 1)
        edges = np.unique(np.quantile(s, quantiles))
        if len(edges) < 2:
            edges = np.array([edges[0] - 1e-6, edges[0] + 1e-6]) if len(edges) else np.array([0.0, 1.0])
        probs = []
        for lo, hi in zip(edges[:-1], edges[1:]):
            mask = (s >= lo) & (s < hi if hi < edges[-1] else s <= hi)
            probs.append(float(y[mask].mean()) if mask.any() else float(y.mean()) if len(y) else 0.5)
        self.edges = edges
        self.bin_probs = np.asarray(probs, dtype=np.float64)
        return self

    def predict_proba(self, scores: np.ndarray) -> np.ndarray:
        s = np.asarray(scores, dtype=np.float64).reshape(-1)
        idx = np.clip(np.searchsorted(self.edges, s, side="right") - 1, 0, len(self.bin_probs) - 1)
        return self.bin_probs[idx].astype(np.float32)


def build_scalar_calibrator(name: str):
    if name == "temperature":
        return TemperatureScaler()
    if name == "isotonic":
        return IsotonicCalibrator()
    if name == "histogram_binning":
        return HistogramBinningCalibrator()
    if name == "scalar_platt":
        from .platt import PlattScaler

        return PlattScaler()
    raise ValueError(f"Unknown scalar calibrator: {name}")
