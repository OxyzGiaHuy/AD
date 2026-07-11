from __future__ import annotations

from collections import deque
import math

import numpy as np

from .metrics import average_precision_np, max_f1_np, roc_auc_score_np


def as_score_grid(score_map: np.ndarray) -> np.ndarray:
    arr = np.asarray(score_map, dtype=np.float32)
    if arr.ndim == 2:
        return arr
    if arr.ndim == 1:
        side = int(round(float(len(arr)) ** 0.5))
        if side * side == len(arr):
            return arr.reshape(side, side)
    raise ValueError(f"score_map must be 2D or square flattened patches, got {arr.shape}")


def resize_score_map(score_map: np.ndarray, size_hw: tuple[int, int]) -> np.ndarray:
    from PIL import Image

    h, w = size_hw
    arr = as_score_grid(score_map)
    lo = float(np.nanmin(arr)) if arr.size else 0.0
    hi = float(np.nanmax(arr)) if arr.size else 1.0
    norm = (arr - lo) / (hi - lo + 1e-8)
    img = Image.fromarray(np.uint8(np.clip(norm, 0.0, 1.0) * 255), mode="L")
    img = img.resize((w, h), resample=Image.Resampling.BILINEAR)
    return np.asarray(img, dtype=np.float32) / 255.0


def normalize_map(score_map: np.ndarray, percentile: float = 99.0) -> np.ndarray:
    arr = np.asarray(score_map, dtype=np.float32)
    lo = float(np.nanmin(arr)) if arr.size else 0.0
    hi = float(np.nanpercentile(arr, percentile)) if arr.size else 1.0
    return np.clip((arr - lo) / (hi - lo + 1e-8), 0.0, 1.0).astype(np.float32)


def connected_components(mask: np.ndarray) -> list[np.ndarray]:
    binary = np.asarray(mask).astype(bool)
    seen = np.zeros(binary.shape, dtype=bool)
    components: list[np.ndarray] = []
    h, w = binary.shape
    for y in range(h):
        for x in range(w):
            if not binary[y, x] or seen[y, x]:
                continue
            comp = np.zeros(binary.shape, dtype=bool)
            q: deque[tuple[int, int]] = deque([(y, x)])
            seen[y, x] = True
            while q:
                cy, cx = q.popleft()
                comp[cy, cx] = True
                for ny, nx in ((cy - 1, cx), (cy + 1, cx), (cy, cx - 1), (cy, cx + 1)):
                    if 0 <= ny < h and 0 <= nx < w and binary[ny, nx] and not seen[ny, nx]:
                        seen[ny, nx] = True
                        q.append((ny, nx))
            components.append(comp)
    return components


def pro_auc_score(masks: list[np.ndarray], scores: list[np.ndarray], max_fpr: float = 0.3, steps: int = 100) -> float:
    if not masks or not scores:
        return float("nan")
    thresholds = np.linspace(1.0, 0.0, steps)
    normal_pixels = np.concatenate([np.ones_like(m, dtype=bool).reshape(-1) for m in masks if not np.any(m)]) if any(not np.any(m) for m in masks) else np.asarray([], dtype=bool)
    normal_scores = np.concatenate([s.reshape(-1) for m, s in zip(masks, scores) if not np.any(m)]) if any(not np.any(m) for m in masks) else np.asarray([], dtype=np.float32)
    components_per_image = [connected_components(m) for m in masks]
    xs: list[float] = []
    ys: list[float] = []
    for threshold in thresholds:
        if len(normal_scores):
            fpr = float(np.mean(normal_scores >= threshold))
        else:
            bg_scores = np.concatenate([s[~m] for m, s in zip(masks, scores) if np.any(~m)])
            fpr = float(np.mean(bg_scores >= threshold)) if len(bg_scores) else 0.0
        if fpr > max_fpr:
            continue
        overlaps = []
        for comps, score in zip(components_per_image, scores):
            pred = score >= threshold
            for comp in comps:
                denom = int(comp.sum())
                if denom:
                    overlaps.append(float(np.logical_and(pred, comp).sum()) / denom)
        if overlaps:
            xs.append(fpr)
            ys.append(float(np.mean(overlaps)))
    if len(xs) < 2:
        return float("nan")
    order = np.argsort(xs)
    x = np.asarray(xs, dtype=np.float64)[order]
    y = np.asarray(ys, dtype=np.float64)[order]
    # Add endpoints for stable normalized AUC in [0, max_fpr].
    if x[0] > 0.0:
        x = np.concatenate([[0.0], x])
        y = np.concatenate([[y[0]], y])
    if x[-1] < max_fpr:
        x = np.concatenate([x, [max_fpr]])
        y = np.concatenate([y, [y[-1]]])
    return float(np.trapz(y, x) / max_fpr)


def summarize_pixel(masks: list[np.ndarray], scores: list[np.ndarray]) -> dict[str, float]:
    if not masks or not scores:
        return {"pixel_auroc": float("nan"), "pixel_ap": float("nan"), "max_pixel_f1": float("nan"), "pro": float("nan"), "pixel_count": 0}
    labels = np.concatenate([m.astype(np.uint8).reshape(-1) for m in masks])
    flat_scores = np.concatenate([s.astype(np.float32).reshape(-1) for s in scores])
    if labels.sum() == 0 or labels.sum() == len(labels):
        auroc = float("nan")
    else:
        auroc = roc_auc_score_np(labels, flat_scores)
    return {
        "pixel_auroc": auroc,
        "pixel_ap": average_precision_np(labels, flat_scores),
        "max_pixel_f1": max_f1_np(labels, flat_scores),
        "pro": pro_auc_score(masks, scores),
        "pixel_count": int(len(labels)),
    }
