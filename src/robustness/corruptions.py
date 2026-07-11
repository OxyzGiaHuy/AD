from __future__ import annotations

import io

import numpy as np


def gaussian_noise(image: np.ndarray, severity: float = 0.05, seed: int = 0) -> np.ndarray:
    rng = np.random.default_rng(seed)
    return np.clip(image + rng.normal(0.0, severity, size=image.shape), 0.0, 1.0).astype(np.float32)


def brightness_contrast(image: np.ndarray, brightness: float = 0.05, contrast: float = 1.15) -> np.ndarray:
    return np.clip((image - 0.5) * contrast + 0.5 + brightness, 0.0, 1.0).astype(np.float32)


def blur(image: np.ndarray, kernel: int = 3) -> np.ndarray:
    try:
        from PIL import Image, ImageFilter
    except ImportError:
        return image.astype(np.float32)
    radius = max(float(kernel - 1) / 2.0, 0.0)
    pil = Image.fromarray((np.clip(image, 0, 1) * 255).astype(np.uint8))
    out = pil.filter(ImageFilter.BoxBlur(radius))
    return (np.asarray(out).astype(np.float32) / 255.0).clip(0, 1)


def jpeg(image: np.ndarray, quality: int = 60) -> np.ndarray:
    try:
        from PIL import Image
    except ImportError:
        return image
    pil = Image.fromarray((np.clip(image, 0, 1) * 255).astype(np.uint8))
    buffer = io.BytesIO()
    pil.save(buffer, format="JPEG", quality=quality)
    buffer.seek(0)
    return (np.asarray(Image.open(buffer)).astype(np.float32) / 255.0).clip(0, 1)

