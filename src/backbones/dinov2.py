from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np


@dataclass
class FeatureBatch:
    patch_features: np.ndarray
    grid_size: tuple[int, int]


class IdentityPatchBackbone:
    """Deterministic lightweight fallback for smoke tests and offline work."""

    def __init__(self, feature_dim: int = 32, patches: int = 16) -> None:
        self.feature_dim = feature_dim
        self.patches = patches

    def encode_records(self, records: list[Any], seed: int = 0) -> FeatureBatch:
        feats = []
        for rec in records:
            digest = hashlib.sha256(f"{rec.path}|{seed}".encode("utf-8")).digest()
            value = int.from_bytes(digest[:4], byteorder="little", signed=False)
            rng = np.random.default_rng(value)
            base = rng.normal(size=(self.patches, self.feature_dim)).astype(np.float32)
            if getattr(rec, "label", 0) == 1:
                base[: max(1, self.patches // 4)] += 2.0
            feats.append(base)
        return FeatureBatch(np.stack(feats, axis=0), (int(self.patches**0.5), int(self.patches**0.5)))


class DINOv2Backbone:
    def __init__(self, name: str = "dinov2_vits14", device: str = "cuda", image_size: int = 518, batch_size: int = 8) -> None:
        try:
            import torch
        except ImportError as exc:
            raise RuntimeError("PyTorch is required for DINOv2Backbone.") from exc
        self.torch = torch
        self.name = name
        self.device = device if torch.cuda.is_available() and device == "cuda" else "cpu"
        self.image_size = image_size
        self.batch_size = batch_size
        local_repo = Path.home() / ".cache" / "torch" / "hub" / "facebookresearch_dinov2_main"
        if local_repo.exists():
            self.model = torch.hub.load(str(local_repo), name, source="local")
        else:
            self.model = torch.hub.load("facebookresearch/dinov2", name)
        self.model.eval().to(self.device)
        for param in self.model.parameters():
            param.requires_grad_(False)

    def encode_records(self, records: list[Any], seed: int = 0) -> FeatureBatch:
        # Full image preprocessing is intentionally centralized here so all
        # methods share identical frozen features. Dataset-specific transforms
        # can be added without touching model code.
        from PIL import Image
        import torchvision.transforms as T

        transform = T.Compose(
            [
                T.Resize((self.image_size, self.image_size), antialias=True),
                T.ToTensor(),
                T.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
            ]
        )
        patches = []
        batch = []
        with self.torch.no_grad():
            for rec in records:
                image = Image.open(rec.path).convert("RGB")
                batch.append(transform(image))
                if len(batch) == self.batch_size:
                    tensor = self.torch.stack(batch, dim=0).to(self.device)
                    out = self.model.forward_features(tensor)
                    patches.extend(out["x_norm_patchtokens"].detach().cpu().numpy().astype(np.float32))
                    batch = []
            if batch:
                tensor = self.torch.stack(batch, dim=0).to(self.device)
                out = self.model.forward_features(tensor)
                patches.extend(out["x_norm_patchtokens"].detach().cpu().numpy().astype(np.float32))
        n_patches = patches[0].shape[0] if patches else 0
        grid = int(n_patches**0.5)
        return FeatureBatch(np.stack(patches, axis=0), (grid, grid))


def build_backbone(name: str, device: str = "cuda", image_size: int = 518, batch_size: int = 8) -> Any:
    if name == "identity_patch":
        return IdentityPatchBackbone()
    if name == "dinov2_vits14":
        return DINOv2Backbone(name=name, device=device, image_size=image_size, batch_size=batch_size)
    raise ValueError(f"Unsupported backbone: {name}")


def cache_path(cache_dir: str | Path, dataset: str, category: str, backbone: str, k: int, seed: int) -> Path:
    safe = f"{dataset}_{category}_{backbone}_k{k}_seed{seed}.npz"
    return Path(cache_dir) / safe

