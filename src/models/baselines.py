from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .pca import PCASubspace


@dataclass
class PatchCoreNN:
    memory: np.ndarray

    @classmethod
    def fit(cls, normal_features: np.ndarray, max_memory: int = 4096, seed: int = 0) -> "PatchCoreNN":
        rng = np.random.default_rng(seed)
        x = normal_features.reshape(-1, normal_features.shape[-1]).astype(np.float32)
        if len(x) > max_memory:
            x = x[rng.choice(len(x), size=max_memory, replace=False)]
        return cls(memory=x)

    def score_images(self, features: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        x = features.reshape(-1, features.shape[-1]).astype(np.float32)
        memory = self.memory.astype(np.float32)
        memory_norm = np.sum(memory * memory, axis=1, keepdims=True).T
        mins = np.empty(len(x), dtype=np.float32)
        chunk_size = 2048
        for start in range(0, len(x), chunk_size):
            chunk = x[start : start + chunk_size]
            chunk_norm = np.sum(chunk * chunk, axis=1, keepdims=True)
            distances = chunk_norm + memory_norm - 2.0 * (chunk @ memory.T)
            np.maximum(distances, 0.0, out=distances)
            mins[start : start + len(chunk)] = distances.min(axis=1)
        patch_scores = np.sqrt(mins).reshape(features.shape[:-1])
        return patch_scores.max(axis=1), patch_scores

    def storage_bytes(self) -> int:
        return int(self.memory.nbytes)


class AnomalyDINO(PatchCoreNN):
    """DINOv2 memory-bank baseline using the shared frozen features."""


@dataclass
class SubspaceAD:
    pca: PCASubspace

    @classmethod
    def fit(cls, normal_features: np.ndarray, pca_components: int = 64) -> "SubspaceAD":
        return cls(PCASubspace.fit(normal_features, pca_components))

    def score_images(self, features: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        patch_scores = self.pca.residual_scores(features)
        return patch_scores.max(axis=1), patch_scores

    def storage_bytes(self) -> int:
        return int(self.pca.mean.nbytes + self.pca.components.nbytes)


def build_model(variant: str, normal_features: np.ndarray, config: dict, seed: int):
    from .head_pca import CalibSubspaceHead, HeadPCA, LoRAHeadPCA, ShiftAwareCalibSubspaceHead

    pca_components = int(config.get("pca_components", 64))
    if variant == "head_pca":
        return HeadPCA.fit(
            normal_features,
            pca_components=pca_components,
            alpha=float(config.get("alpha", 0.5)),
            seed=seed,
            synthetic_anomaly_ratio=float(config.get("synthetic_anomaly_ratio", 1.0)),
            head_type=str(config.get("head_type", "linear")),
            head_hidden_dim=int(config.get("head_hidden_dim", 256)),
            train_steps=int(config.get("train_steps", 500)),
            learning_rate=float(config.get("learning_rate", 1e-3)),
            weight_decay=float(config.get("weight_decay", 1e-4)),
            batch_size=int(config.get("batch_size", 4096)),
            device=str(config.get("device", "cpu")),
        )
    if variant == "lora_head_pca":
        return LoRAHeadPCA.fit(
            normal_features,
            pca_components=pca_components,
            alpha=float(config.get("alpha", 0.5)),
            seed=seed,
            synthetic_anomaly_ratio=float(config.get("synthetic_anomaly_ratio", 1.0)),
            head_type=str(config.get("head_type", "mlp")),
            head_hidden_dim=int(config.get("head_hidden_dim", 256)),
            train_steps=int(config.get("train_steps", 500)),
            learning_rate=float(config.get("learning_rate", 1e-3)),
            weight_decay=float(config.get("weight_decay", 1e-4)),
            batch_size=int(config.get("batch_size", 4096)),
            device=str(config.get("device", "cpu")),
        )
    if variant == "calib_subspace_head":
        return CalibSubspaceHead.fit(
            normal_features,
            pca_components=pca_components,
            seed=seed,
            synthetic_anomaly_ratio=float(config.get("synthetic_anomaly_ratio", 1.0)),
            head_type=str(config.get("head_type", "mlp")),
            head_hidden_dim=int(config.get("head_hidden_dim", 256)),
            train_steps=int(config.get("train_steps", 500)),
            learning_rate=float(config.get("learning_rate", 1e-3)),
            weight_decay=float(config.get("weight_decay", 1e-4)),
            batch_size=int(config.get("batch_size", 4096)),
            device=str(config.get("device", "cpu")),
        )
    if variant == "shift_aware_calib_subspace_head":
        return ShiftAwareCalibSubspaceHead.fit(
            normal_features,
            pca_components=pca_components,
            seed=seed,
            synthetic_anomaly_ratio=float(config.get("synthetic_anomaly_ratio", 1.0)),
            head_type=str(config.get("head_type", "mlp")),
            head_hidden_dim=int(config.get("head_hidden_dim", 256)),
            train_steps=int(config.get("train_steps", 500)),
            learning_rate=float(config.get("learning_rate", 1e-3)),
            weight_decay=float(config.get("weight_decay", 1e-4)),
            batch_size=int(config.get("batch_size", 4096)),
            device=str(config.get("device", "cpu")),
        )
    if variant == "patchcore":
        return PatchCoreNN.fit(normal_features, seed=seed)
    if variant == "anomalydino":
        return AnomalyDINO.fit(normal_features, seed=seed)
    if variant == "subspacead":
        return SubspaceAD.fit(normal_features, pca_components=pca_components)
    raise ValueError(f"Unsupported model variant: {variant}")

