from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .models.pca import PCASubspace


def top_fraction_score(patch_scores: np.ndarray, rho: float = 0.01) -> np.ndarray:
    scores = np.asarray(patch_scores, dtype=np.float32)
    if scores.ndim == 1:
        scores = scores[None, :]
    k = max(1, int(np.ceil(scores.shape[1] * rho)))
    part = np.partition(scores, scores.shape[1] - k, axis=1)[:, -k:]
    return part.mean(axis=1).astype(np.float32)


def conformal_p_values(calibration_scores: np.ndarray, test_scores: np.ndarray) -> np.ndarray:
    calibration = np.asarray(calibration_scores, dtype=np.float64).reshape(-1)
    test = np.asarray(test_scores, dtype=np.float64)
    flat = test.reshape(-1)
    counts = np.empty(len(flat), dtype=np.float64)
    chunk = max(1, int(5_000_000 // max(len(calibration), 1)))
    for start in range(0, len(flat), chunk):
        end = min(start + chunk, len(flat))
        counts[start:end] = (calibration[:, None] >= flat[None, start:end]).sum(axis=0)
    return ((1.0 + counts) / (len(calibration) + 1.0)).reshape(test.shape).astype(np.float32)


def weighted_conformal_p_values(
    calibration_scores: np.ndarray,
    test_scores: np.ndarray,
    calibration_weights: np.ndarray,
    test_weights: np.ndarray | float = 1.0,
) -> np.ndarray:
    calibration = np.asarray(calibration_scores, dtype=np.float64).reshape(-1)
    test = np.asarray(test_scores, dtype=np.float64).reshape(-1)
    weights = np.asarray(calibration_weights, dtype=np.float64).reshape(-1)
    weights = np.maximum(weights, 1e-8)
    test_w = np.asarray(test_weights, dtype=np.float64)
    if test_w.ndim == 0:
        test_w = np.full(len(test), float(test_w), dtype=np.float64)
    test_w = np.maximum(test_w.reshape(-1), 1e-8)
    numer = np.empty(len(test), dtype=np.float64)
    chunk = max(1, int(5_000_000 // max(len(calibration), 1)))
    for start in range(0, len(test), chunk):
        end = min(start + chunk, len(test))
        numer[start:end] = ((calibration[:, None] >= test[None, start:end]) * weights[:, None]).sum(axis=0) + test_w[start:end]
    denom = weights.sum() + test_w
    return (numer / denom).astype(np.float32)


def effective_sample_size(weights: np.ndarray) -> float:
    w = np.maximum(np.asarray(weights, dtype=np.float64).reshape(-1), 1e-12)
    return float((w.sum() ** 2) / np.sum(w * w))


def benjamini_hochberg_mask(p_values: np.ndarray, q: float) -> np.ndarray:
    p = np.asarray(p_values, dtype=np.float64).reshape(-1)
    if len(p) == 0:
        return np.zeros_like(p, dtype=bool)
    order = np.argsort(p)
    ranked = p[order]
    thresholds = q * (np.arange(1, len(p) + 1) / len(p))
    valid = ranked <= thresholds
    mask = np.zeros(len(p), dtype=bool)
    if np.any(valid):
        cutoff = ranked[np.where(valid)[0].max()]
        mask = p <= cutoff
    return mask.reshape(np.asarray(p_values).shape)


@dataclass
class ConformalCalibration:
    patch_scores: np.ndarray
    patch_covariates: np.ndarray
    image_scores: np.ndarray
    image_covariates: np.ndarray
    mode: str


def _compressed_covariates(pca: PCASubspace, features: np.ndarray) -> np.ndarray:
    x = features.reshape(-1, features.shape[-1]).astype(np.float32)
    return ((x - pca.mean) @ pca.components.T).astype(np.float32)


def insample_calibration(support_features: np.ndarray, pca_components: int, rho: float = 0.01) -> ConformalCalibration:
    pca = PCASubspace.fit(support_features, pca_components)
    patch = pca.residual_scores(support_features).astype(np.float32)
    image = top_fraction_score(patch, rho=rho)
    cov = _compressed_covariates(pca, support_features)
    image_cov = cov.reshape(support_features.shape[0], support_features.shape[1], -1).mean(axis=1)
    return ConformalCalibration(patch.reshape(-1), cov, image, image_cov.astype(np.float32), "insample_conformal")


def loio_calibration(support_features: np.ndarray, pca_components: int, rho: float = 0.01) -> ConformalCalibration:
    n_images, n_patches, dim = support_features.shape
    patch_scores: list[np.ndarray] = []
    patch_covariates: list[np.ndarray] = []
    image_scores: list[float] = []
    image_covariates: list[np.ndarray] = []
    if n_images >= 2:
        for index in range(n_images):
            train = np.delete(support_features, index, axis=0)
            pca = PCASubspace.fit(train, pca_components)
            held = support_features[index : index + 1]
            patch = pca.residual_scores(held).astype(np.float32)
            cov = _compressed_covariates(pca, held)
            patch_scores.append(patch.reshape(-1))
            patch_covariates.append(cov)
            image_scores.append(float(top_fraction_score(patch, rho=rho)[0]))
            image_covariates.append(cov.mean(axis=0))
    else:
        even = np.arange(n_patches) % 2 == 0
        odd = ~even
        if even.sum() <= pca_components:
            pca_components = max(1, int(even.sum() - 1))
        pca = PCASubspace.fit(support_features[:, even, :], pca_components)
        held = support_features[:, odd, :]
        patch = pca.residual_scores(held).astype(np.float32)
        cov = _compressed_covariates(pca, held)
        patch_scores.append(patch.reshape(-1))
        patch_covariates.append(cov)
        image_scores.append(float(top_fraction_score(patch, rho=rho)[0]))
        image_covariates.append(cov.mean(axis=0))
    return ConformalCalibration(
        np.concatenate(patch_scores).astype(np.float32),
        np.concatenate(patch_covariates).astype(np.float32),
        np.asarray(image_scores, dtype=np.float32),
        np.asarray(image_covariates, dtype=np.float32),
        "loio_conformal",
    )


def pca_patch_covariates(pca: PCASubspace, features: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    cov = _compressed_covariates(pca, features)
    image_cov = cov.reshape(features.shape[0], features.shape[1], -1).mean(axis=1)
    return cov.astype(np.float32), image_cov.astype(np.float32)


@dataclass
class DensityRatioLogistic:
    weights: np.ndarray
    bias: float
    mean: np.ndarray
    std: np.ndarray
    n0: int
    n1: int

    @classmethod
    def fit(cls, source: np.ndarray, target: np.ndarray, steps: int = 1000, lr: float = 0.05, l2: float = 1e-4) -> "DensityRatioLogistic":
        x0 = np.asarray(source, dtype=np.float64)
        x1 = np.asarray(target, dtype=np.float64)
        x = np.concatenate([x0, x1], axis=0)
        y = np.concatenate([np.zeros(len(x0), dtype=np.float64), np.ones(len(x1), dtype=np.float64)])
        mean = x.mean(axis=0, keepdims=True)
        std = np.maximum(x.std(axis=0, keepdims=True), 1.0)
        z = (x - mean) / std
        weights = np.zeros(z.shape[1], dtype=np.float64)
        bias = 0.0
        for _ in range(steps):
            logits = np.clip(z @ weights + bias, -40, 40)
            probs = 1.0 / (1.0 + np.exp(-logits))
            grad = probs - y
            weights -= lr * (z.T @ grad / len(z) + l2 * weights)
            bias -= lr * float(np.mean(grad))
        return cls(weights.astype(np.float32), float(bias), mean.astype(np.float32), std.astype(np.float32), len(x0), len(x1))

    def probabilities(self, x: np.ndarray) -> np.ndarray:
        z = (np.asarray(x, dtype=np.float64) - self.mean) / self.std
        logits = np.clip(z @ self.weights.astype(np.float64) + self.bias, -40, 40)
        return (1.0 / (1.0 + np.exp(-logits))).astype(np.float32)

    def density_ratio(self, x: np.ndarray) -> np.ndarray:
        p = np.clip(self.probabilities(x).astype(np.float64), 1e-5, 1.0 - 1e-5)
        return (p / (1.0 - p) * (self.n0 / max(self.n1, 1))).astype(np.float32)
