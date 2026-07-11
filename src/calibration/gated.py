from __future__ import annotations

from dataclasses import dataclass

import numpy as np


def normalize_gate_weights(weights: np.ndarray) -> np.ndarray:
    w = np.asarray(weights, dtype=np.float64)
    if w.ndim == 1:
        w = w[None, :]
    w = np.maximum(w, 0.0)
    denom = w.sum(axis=1, keepdims=True)
    fallback = np.full_like(w, 1.0 / max(w.shape[1], 1))
    return np.where(denom > 0.0, w / np.maximum(denom, 1e-12), fallback).astype(np.float32)


def gated_probabilities(expert_probs: np.ndarray, gate_weights: np.ndarray) -> np.ndarray:
    probs = np.asarray(expert_probs, dtype=np.float64)
    weights = normalize_gate_weights(gate_weights).astype(np.float64)
    if probs.ndim != 2:
        raise ValueError("expert_probs must have shape [num_samples, num_experts].")
    if weights.shape[0] == 1 and probs.shape[0] > 1:
        weights = np.repeat(weights, probs.shape[0], axis=0)
    if weights.shape != probs.shape:
        raise ValueError(f"gate_weights shape {weights.shape} does not match expert_probs shape {probs.shape}.")
    return np.clip((probs * weights).sum(axis=1), 0.0, 1.0).astype(np.float32)


def anchored_gated_probabilities(anchor_probs: np.ndarray, expert_probs: np.ndarray, gate_weights: np.ndarray, strength: float) -> np.ndarray:
    """Interpolate from a safe anchor toward a gated expert mixture.

    The base Vector Platt calibrator is used as the anchor in the experiments.
    This makes shift-aware calibration a no-harm correction: when the gate is
    uncertain, `strength` should be close to zero and the output stays near the
    safe baseline.
    """

    anchor = np.asarray(anchor_probs, dtype=np.float64).reshape(-1)
    mixed = gated_probabilities(expert_probs, gate_weights).astype(np.float64)
    lam = float(np.clip(strength, 0.0, 1.0))
    return np.clip(anchor + lam * (mixed - anchor), 0.0, 1.0).astype(np.float32)


@dataclass
class ShiftGateSummary:
    domain_confidence: float
    n_eff_ratio: float
    pca_concentration: float
    residual_std: float


def structured_shift_gate(corruption: str, expert_names: list[str]) -> np.ndarray:
    weights = np.zeros(len(expert_names), dtype=np.float32)
    preferred = "shift_aware_vector_platt"
    if corruption == "gaussian_noise":
        preferred = "vector_platt"
    elif corruption in {"blur", "brightness_contrast", "jpeg"}:
        preferred = "shift_aware_vector_platt"
    if preferred not in expert_names:
        preferred = expert_names[0]
    weights[expert_names.index(preferred)] = 1.0
    return weights


def noise_safe_soft_gate(summary: ShiftGateSummary, expert_names: list[str]) -> np.ndarray:
    """Oracle-free heuristic gate.

    Low effective sample size and high residual concentration often indicate
    unstable density-ratio estimates, so the gate falls back toward the base
    vector Platt expert. Structured shifts with usable n_eff receive more mass
    on the shift-aware and weighted experts.
    """

    weights = {name: 0.0 for name in expert_names}
    base = "vector_platt" if "vector_platt" in weights else expert_names[0]
    shift = "shift_aware_vector_platt" if "shift_aware_vector_platt" in weights else base
    weighted = "weighted_platt" if "weighted_platt" in weights else shift
    stable_ratio = float(np.clip(summary.n_eff_ratio, 0.0, 1.0))
    domain_signal = float(np.clip(2.0 * abs(summary.domain_confidence - 0.5), 0.0, 1.0))
    noisy_signal = float(np.clip((summary.pca_concentration - 4.0) / 4.0, 0.0, 1.0))
    structured_mass = stable_ratio * domain_signal * (1.0 - 0.6 * noisy_signal)
    weights[base] += 1.0 - structured_mass
    weights[shift] += 0.65 * structured_mass
    weights[weighted] += 0.35 * structured_mass
    return normalize_gate_weights(np.asarray([weights[name] for name in expert_names], dtype=np.float32))[0]


def no_harm_gate_strength(summary: ShiftGateSummary, conservative: bool = True) -> float:
    stable_ratio = float(np.clip(summary.n_eff_ratio, 0.0, 1.0))
    domain_signal = float(np.clip(2.0 * abs(summary.domain_confidence - 0.5), 0.0, 1.0))
    noisy_signal = float(np.clip((summary.pca_concentration - 4.0) / 4.0, 0.0, 1.0))
    raw = stable_ratio * domain_signal * (1.0 - 0.75 * noisy_signal)
    raw = float(np.clip(raw, 0.0, 1.0))
    return 0.35 * raw if conservative else raw
