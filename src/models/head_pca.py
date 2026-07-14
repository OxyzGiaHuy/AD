from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .pca import PCASubspace


def _sigmoid(x: np.ndarray) -> np.ndarray:
    return 1.0 / (1.0 + np.exp(-np.clip(x, -40, 40)))


def make_synthetic_feature_batch(normal_features: np.ndarray, seed: int = 0, ratio: float = 1.0) -> np.ndarray:
    """Synthetic-anomaly feature batch shared by every label-free calibrator.

    Replaces 25% of the patches of a sampled support image with resampled
    support patches plus Gaussian noise and a sign shift. Keeping this at
    module level lets scalar calibration baselines train on exactly the same
    synthetic protocol as the vector calibrators.
    """
    rng = np.random.default_rng(seed)
    x = normal_features.reshape(-1, normal_features.shape[-1]).astype(np.float32)
    n_images, n_patches, dim = normal_features.shape
    n_synth = max(1, int(n_images * ratio))
    synth = np.empty((n_synth, n_patches, dim), dtype=np.float32)
    for i in range(n_synth):
        source = normal_features[rng.integers(0, n_images)].copy()
        n_bad = max(1, n_patches // 4)
        idx = rng.choice(n_patches, size=n_bad, replace=False)
        sampled = x[rng.integers(0, len(x), size=n_bad)]
        noise = rng.normal(0.0, 0.75, size=sampled.shape).astype(np.float32)
        source[idx] = sampled + noise + 0.25 * np.sign(sampled).astype(np.float32)
        synth[i] = source
    return synth


@dataclass
class LinearHead:
    weight: np.ndarray
    bias: float

    @classmethod
    def fit_synthetic(cls, normal_features: np.ndarray, seed: int = 0, ratio: float = 1.0) -> "LinearHead":
        rng = np.random.default_rng(seed)
        x_normal = normal_features.reshape(-1, normal_features.shape[-1]).astype(np.float32)
        n_anom = max(1, int(len(x_normal) * ratio))
        sampled = x_normal[rng.integers(0, len(x_normal), size=n_anom)]
        noise = rng.normal(0.0, 0.75, size=sampled.shape).astype(np.float32)
        x_anom = sampled + noise + 0.25 * np.sign(sampled)
        mu_n = x_normal.mean(axis=0)
        mu_a = x_anom.mean(axis=0)
        weight = mu_a - mu_n
        norm = np.linalg.norm(weight) + 1e-8
        weight = weight / norm
        bias = -0.5 * float((mu_a + mu_n) @ weight)
        return cls(weight=weight.astype(np.float32), bias=bias)

    def patch_scores(self, features: np.ndarray) -> np.ndarray:
        logits = features @ self.weight + self.bias
        return _sigmoid(logits)

    def storage_bytes(self) -> int:
        return int(self.weight.nbytes + np.asarray(self.bias, dtype=np.float32).nbytes)




class TorchMLPHead:
    def __init__(self, model, device: str = "cpu") -> None:
        self.model = model
        self.device = device

    @classmethod
    def fit_synthetic(
        cls,
        normal_features: np.ndarray,
        seed: int = 0,
        ratio: float = 1.0,
        hidden_dim: int = 256,
        steps: int = 500,
        lr: float = 1e-3,
        weight_decay: float = 1e-4,
        batch_size: int = 4096,
        device: str = "cpu",
    ) -> "TorchMLPHead":
        try:
            import torch
            import torch.nn as nn
        except ImportError as exc:
            raise RuntimeError("PyTorch is required for TorchMLPHead.") from exc

        rng = np.random.default_rng(seed)
        x_normal = normal_features.reshape(-1, normal_features.shape[-1]).astype(np.float32)
        n_anom = max(1, int(len(x_normal) * ratio))
        sampled = x_normal[rng.integers(0, len(x_normal), size=n_anom)]
        noise = rng.normal(0.0, 0.75, size=sampled.shape).astype(np.float32)
        sign_shift = 0.25 * np.sign(sampled).astype(np.float32)
        x_anom = sampled + noise + sign_shift
        x = np.concatenate([x_normal, x_anom], axis=0)
        y = np.concatenate([np.zeros(len(x_normal), dtype=np.float32), np.ones(len(x_anom), dtype=np.float32)])
        order = rng.permutation(len(x))
        x = x[order]
        y = y[order]

        torch.manual_seed(seed)
        if torch.cuda.is_available():
            torch.cuda.manual_seed_all(seed)
        use_device = device if device == "cuda" and torch.cuda.is_available() else "cpu"
        model = nn.Sequential(
            nn.Linear(x.shape[1], hidden_dim),
            nn.ReLU(inplace=True),
            nn.Dropout(p=0.1),
            nn.Linear(hidden_dim, 1),
        ).to(use_device)
        opt = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=weight_decay)
        loss_fn = nn.BCEWithLogitsLoss()
        x_t = torch.from_numpy(x).to(use_device)
        y_t = torch.from_numpy(y).to(use_device)
        model.train()
        for _ in range(max(1, steps)):
            idx = torch.randint(0, len(x_t), (min(batch_size, len(x_t)),), device=use_device)
            logits = model(x_t[idx]).squeeze(1)
            loss = loss_fn(logits, y_t[idx])
            opt.zero_grad(set_to_none=True)
            loss.backward()
            opt.step()
        model.eval()
        return cls(model=model, device=use_device)

    def patch_scores(self, features: np.ndarray) -> np.ndarray:
        import torch

        original_shape = features.shape[:-1]
        x = features.reshape(-1, features.shape[-1]).astype(np.float32)
        with torch.no_grad():
            tensor = torch.from_numpy(x).to(self.device)
            probs = torch.sigmoid(self.model(tensor).squeeze(1)).detach().cpu().numpy()
        return probs.reshape(original_shape).astype(np.float32)

    def storage_bytes(self) -> int:
        return sum(param.numel() * param.element_size() for param in self.model.parameters())


@dataclass
class HeadPCA:
    head: LinearHead
    pca: PCASubspace
    alpha: float = 0.5

    @classmethod
    def fit(
        cls,
        normal_features: np.ndarray,
        pca_components: int = 64,
        alpha: float = 0.5,
        seed: int = 0,
        synthetic_anomaly_ratio: float = 1.0,
        head_type: str = "linear",
        head_hidden_dim: int = 256,
        train_steps: int = 500,
        learning_rate: float = 1e-3,
        weight_decay: float = 1e-4,
        batch_size: int = 4096,
        device: str = "cpu",
    ) -> "HeadPCA":
        pca = PCASubspace.fit(normal_features, pca_components)
        if head_type == "mlp":
            try:
                head = TorchMLPHead.fit_synthetic(
                    normal_features,
                    seed=seed,
                    ratio=synthetic_anomaly_ratio,
                    hidden_dim=head_hidden_dim,
                    steps=train_steps,
                    lr=learning_rate,
                    weight_decay=weight_decay,
                    batch_size=batch_size,
                    device=device,
                )
            except RuntimeError:
                head = LinearHead.fit_synthetic(normal_features, seed=seed, ratio=synthetic_anomaly_ratio)
        else:
            head = LinearHead.fit_synthetic(normal_features, seed=seed, ratio=synthetic_anomaly_ratio)
        return cls(head=head, pca=pca, alpha=alpha)

    def score_patches(self, features: np.ndarray) -> np.ndarray:
        head_scores = self.head.patch_scores(features)
        residual = self.pca.residual_scores(features)
        residual = residual / (np.percentile(residual, 95) + 1e-8)
        residual = np.clip(residual, 0.0, 5.0) / 5.0
        return self.alpha * head_scores + (1.0 - self.alpha) * residual

    def score_images(self, features: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        patch_scores = self.score_patches(features)
        image_scores = patch_scores.max(axis=1)
        return image_scores.astype(np.float32), patch_scores.astype(np.float32)

    def storage_bytes(self) -> int:
        head_bytes = self.head.storage_bytes() if hasattr(self.head, "storage_bytes") else 0
        return int(head_bytes + self.pca.mean.nbytes + self.pca.components.nbytes)


class LoRAHeadPCA(HeadPCA):
    """Interface placeholder for the LoRA variant.

    The class preserves the experiment API while the concrete LoRA injection is
    implemented inside the DINOv2 torch path. Offline smoke tests use the same
    scoring behavior as HeadPCA.
    """



@dataclass
class CalibSubspaceHead:
    head: LinearHead
    pca: PCASubspace
    feature_mean: np.ndarray
    feature_std: np.ndarray

    @classmethod
    def fit(
        cls,
        normal_features: np.ndarray,
        pca_components: int = 64,
        seed: int = 0,
        synthetic_anomaly_ratio: float = 1.0,
        head_type: str = "mlp",
        head_hidden_dim: int = 256,
        train_steps: int = 500,
        learning_rate: float = 1e-3,
        weight_decay: float = 1e-4,
        batch_size: int = 4096,
        device: str = "cpu",
    ) -> "CalibSubspaceHead":
        pca = PCASubspace.fit(normal_features, pca_components)
        if head_type == "mlp":
            try:
                head = TorchMLPHead.fit_synthetic(
                    normal_features,
                    seed=seed,
                    ratio=synthetic_anomaly_ratio,
                    hidden_dim=head_hidden_dim,
                    steps=train_steps,
                    lr=learning_rate,
                    weight_decay=weight_decay,
                    batch_size=batch_size,
                    device=device,
                )
            except RuntimeError:
                head = LinearHead.fit_synthetic(normal_features, seed=seed, ratio=synthetic_anomaly_ratio)
        else:
            head = LinearHead.fit_synthetic(normal_features, seed=seed, ratio=synthetic_anomaly_ratio)
        temp = cls(head=head, pca=pca, feature_mean=np.zeros((1, 2), dtype=np.float32), feature_std=np.ones((1, 2), dtype=np.float32))
        synth_features = temp._make_synthetic_feature_batch(normal_features, seed=seed, ratio=synthetic_anomaly_ratio)
        base = np.concatenate([temp._base_calibration_features(normal_features), temp._base_calibration_features(synth_features)], axis=0)
        temp.feature_mean = base.mean(axis=0, keepdims=True).astype(np.float32)
        temp.feature_std = (base.std(axis=0, keepdims=True) + 1e-6).astype(np.float32)
        return temp

    def _base_calibration_features(self, features: np.ndarray) -> np.ndarray:
        pca_patch = self.pca.residual_scores(features).astype(np.float32)
        pca_image = pca_patch.max(axis=1)
        head_patch = self.head.patch_scores(features).astype(np.float32)
        head_image = head_patch.max(axis=1)
        return np.stack([pca_image, head_image], axis=1).astype(np.float32)

    def calibration_features(self, features: np.ndarray) -> np.ndarray:
        base = self._base_calibration_features(features)
        z = (base - self.feature_mean) / self.feature_std
        disagreement = np.abs(z[:, 0] - z[:, 1])[:, None]
        return np.concatenate([base, disagreement.astype(np.float32)], axis=1).astype(np.float32)

    def _make_synthetic_feature_batch(self, normal_features: np.ndarray, seed: int = 0, ratio: float = 1.0) -> np.ndarray:
        return make_synthetic_feature_batch(normal_features, seed=seed, ratio=ratio)

    def synthetic_calibration_features(self, normal_features: np.ndarray, seed: int = 0, ratio: float = 1.0) -> np.ndarray:
        return self.calibration_features(self._make_synthetic_feature_batch(normal_features, seed=seed, ratio=ratio))

    def score_images(self, features: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
        patch_scores = self.pca.residual_scores(features).astype(np.float32)
        image_scores = patch_scores.max(axis=1)
        return image_scores.astype(np.float32), patch_scores.astype(np.float32)

    def storage_bytes(self) -> int:
        head_bytes = self.head.storage_bytes() if hasattr(self.head, "storage_bytes") else 0
        return int(head_bytes + self.pca.mean.nbytes + self.pca.components.nbytes + self.feature_mean.nbytes + self.feature_std.nbytes)


@dataclass
class ShiftAwareCalibSubspaceHead(CalibSubspaceHead):
    """Subspace ranking with extra shift descriptors for calibration only.

    Raw anomaly ranking remains max PCA residual, identical to CalibSubspaceHead.
    The added features are used by VectorPlattScaler to improve probability
    reliability under dataset/corruption shift without changing AUROC/AP.
    """

    shift_center: np.ndarray
    shift_norm_scale: float

    @classmethod
    def fit(
        cls,
        normal_features: np.ndarray,
        pca_components: int = 64,
        seed: int = 0,
        synthetic_anomaly_ratio: float = 1.0,
        head_type: str = "mlp",
        head_hidden_dim: int = 256,
        train_steps: int = 500,
        learning_rate: float = 1e-3,
        weight_decay: float = 1e-4,
        batch_size: int = 4096,
        device: str = "cpu",
    ) -> "ShiftAwareCalibSubspaceHead":
        base = CalibSubspaceHead.fit(
            normal_features,
            pca_components=pca_components,
            seed=seed,
            synthetic_anomaly_ratio=synthetic_anomaly_ratio,
            head_type=head_type,
            head_hidden_dim=head_hidden_dim,
            train_steps=train_steps,
            learning_rate=learning_rate,
            weight_decay=weight_decay,
            batch_size=batch_size,
            device=device,
        )
        support_flat = normal_features.reshape(-1, normal_features.shape[-1]).astype(np.float32)
        center = support_flat.mean(axis=0, keepdims=True).astype(np.float32)
        support_norm = np.linalg.norm(support_flat - center, axis=1)
        norm_scale = float(np.percentile(support_norm, 95) + 1e-6)
        return cls(
            head=base.head,
            pca=base.pca,
            feature_mean=base.feature_mean,
            feature_std=base.feature_std,
            shift_center=center,
            shift_norm_scale=norm_scale,
        )

    def _shift_features(self, features: np.ndarray) -> np.ndarray:
        centered = features - self.shift_center.reshape(1, 1, -1)
        norms = np.linalg.norm(centered, axis=2)
        norm_max = (norms.max(axis=1) / self.shift_norm_scale)[:, None]
        norm_mean = (norms.mean(axis=1) / self.shift_norm_scale)[:, None]
        pca_patch = self.pca.residual_scores(features)
        pca_mean = pca_patch.mean(axis=1, keepdims=True)
        pca_std = pca_patch.std(axis=1, keepdims=True)
        pca_max = pca_patch.max(axis=1, keepdims=True)
        pca_concentration = pca_max / (pca_mean + 1e-6)
        return np.concatenate([norm_max, norm_mean, pca_mean, pca_std, pca_concentration], axis=1).astype(np.float32)

    def calibration_features(self, features: np.ndarray) -> np.ndarray:
        base = super().calibration_features(features)
        return np.concatenate([base, self._shift_features(features)], axis=1).astype(np.float32)

    def storage_bytes(self) -> int:
        return int(super().storage_bytes() + self.shift_center.nbytes + np.asarray(self.shift_norm_scale, dtype=np.float32).nbytes)

