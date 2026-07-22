from __future__ import annotations

from dataclasses import dataclass
import hashlib
from typing import Hashable, Sequence

import numpy as np
from scipy.stats import beta


@dataclass(frozen=True)
class CandidateCertificate:
    threshold: float
    empirical_loss: float
    upper_bound: float
    n_units: int
    passes: bool


@dataclass(frozen=True)
class ThresholdCertificate:
    selected_threshold: float
    alpha: float
    delta: float
    unit: str
    bound_method: str
    candidates: tuple[CandidateCertificate, ...]


def partition_source_classes(
    classes: Sequence[str],
    target_class: str,
    seed: int,
    allocation: Sequence[float] = (0.5, 0.25, 0.25),
) -> dict[str, tuple[str, ...]]:
    """Deterministically split non-target classes into reference/proposal/certification."""

    available = sorted(set(classes) - {target_class})
    if len(available) < 6:
        raise ValueError("Nested SC3R requires at least six non-target source classes.")
    fractions = np.asarray(allocation, dtype=np.float64)
    if fractions.shape != (3,) or np.any(fractions <= 0.0) or not np.isclose(fractions.sum(), 1.0):
        raise ValueError("allocation must contain three positive fractions summing to one")
    digest = hashlib.sha256(f"sc3r-partition|{target_class}|{seed}".encode("utf-8")).digest()
    rng = np.random.default_rng(int.from_bytes(digest[:8], "little"))
    shuffled = [available[int(index)] for index in rng.permutation(len(available))]
    raw_counts = fractions * len(shuffled)
    counts = np.floor(raw_counts).astype(int)
    while counts.sum() < len(shuffled):
        remainders = raw_counts - counts
        # Break equal remainders toward certification, matching the original
        # 50/25/25 implementation for six and fourteen source classes.
        index = max(range(3), key=lambda item: (remainders[item], item))
        counts[index] += 1
    if np.any(counts < 1):
        raise ValueError("allocation leaves an empty nested source partition")
    n_reference, n_proposal, _ = (int(value) for value in counts)
    return {
        "reference": tuple(sorted(shuffled[:n_reference])),
        "proposal": tuple(sorted(shuffled[n_reference : n_reference + n_proposal])),
        "certification": tuple(sorted(shuffled[n_reference + n_proposal :])),
    }


def proposal_candidates(p_values: np.ndarray, max_candidates: int = 20) -> np.ndarray:
    """Propose a finite positive threshold grid without certification data."""

    values = np.asarray(p_values, dtype=np.float64).reshape(-1)
    if values.size == 0 or not np.all(np.isfinite(values)):
        raise ValueError("Proposal p-values must be a non-empty finite array.")
    if np.any((values <= 0.0) | (values > 1.0)):
        raise ValueError("Conformal p-values must lie in (0, 1].")
    if max_candidates < 1:
        raise ValueError("max_candidates must be positive.")
    unique = np.unique(values)
    if len(unique) <= max_candidates:
        return unique
    indices = np.unique(np.linspace(0, len(unique) - 1, max_candidates, dtype=int))
    return unique[indices]


def hoeffding_upper_bound(losses: np.ndarray, delta: float) -> float:
    """One-sided Hoeffding bound for independent losses in [0, 1]."""

    values = np.asarray(losses, dtype=np.float64).reshape(-1)
    if values.size == 0:
        raise ValueError("At least one certification unit is required.")
    if not np.all(np.isfinite(values)) or np.any((values < 0.0) | (values > 1.0)):
        raise ValueError("Losses must be finite and lie in [0, 1].")
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie strictly between 0 and 1.")
    radius = np.sqrt(np.log(1.0 / delta) / (2.0 * len(values)))
    return float(min(1.0, values.mean() + radius))


def clopper_pearson_upper_bound(losses: np.ndarray, delta: float) -> float:
    """One-sided exact binomial upper bound for independent Bernoulli losses."""
    values = np.asarray(losses, dtype=np.float64).reshape(-1)
    if values.size == 0:
        raise ValueError("At least one certification unit is required.")
    if not np.all(np.isin(values, [0.0, 1.0])):
        raise ValueError("Clopper-Pearson requires Bernoulli losses in {0, 1}.")
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie strictly between 0 and 1.")
    successes = int(values.sum())
    if successes == len(values):
        return 1.0
    return float(beta.ppf(1.0 - delta, successes + 1, len(values) - successes))


def _unit_losses(alarms: np.ndarray, unit_ids: Sequence[Hashable] | None) -> np.ndarray:
    if unit_ids is None:
        return alarms.astype(np.float64)
    if len(unit_ids) != len(alarms):
        raise ValueError("unit_ids must have one entry per p-value.")
    grouped: dict[Hashable, list[float]] = {}
    for unit_id, alarm in zip(unit_ids, alarms):
        grouped.setdefault(unit_id, []).append(float(alarm))
    return np.asarray([np.mean(grouped[key]) for key in sorted(grouped, key=str)], dtype=np.float64)


def certify_thresholds(
    certification_p_values: np.ndarray,
    candidates: np.ndarray,
    alpha: float,
    delta: float,
    unit_ids: Sequence[Hashable] | None = None,
    bound_method: str = "hoeffding",
) -> ThresholdCertificate:
    """Select the largest simultaneously certified candidate.

    Candidate thresholds must have been fixed without looking at
    ``certification_p_values``. The Bonferroni allocation makes post-certification
    selection across this finite set valid under the assumptions of the chosen
    one-sided bound.
    """

    p_values = np.asarray(certification_p_values, dtype=np.float64).reshape(-1)
    thresholds = np.unique(np.asarray(candidates, dtype=np.float64).reshape(-1))
    if p_values.size == 0 or not np.all(np.isfinite(p_values)):
        raise ValueError("Certification p-values must be a non-empty finite array.")
    if np.any((p_values <= 0.0) | (p_values > 1.0)):
        raise ValueError("Conformal p-values must lie in (0, 1].")
    if thresholds.size == 0 or np.any((thresholds <= 0.0) | (thresholds > 1.0)):
        raise ValueError("Candidate thresholds must be a non-empty subset of (0, 1].")
    if not 0.0 <= alpha <= 1.0:
        raise ValueError("alpha must lie in [0, 1].")
    if not 0.0 < delta < 1.0:
        raise ValueError("delta must lie strictly between 0 and 1.")

    per_candidate_delta = delta / len(thresholds)
    if bound_method not in {"hoeffding", "clopper_pearson"}:
        raise ValueError("bound_method must be hoeffding or clopper_pearson")
    certificates: list[CandidateCertificate] = []
    for threshold in thresholds:
        losses = _unit_losses(p_values <= threshold, unit_ids)
        upper = (
            clopper_pearson_upper_bound(losses, per_candidate_delta)
            if bound_method == "clopper_pearson"
            else hoeffding_upper_bound(losses, per_candidate_delta)
        )
        certificates.append(
            CandidateCertificate(
                threshold=float(threshold),
                empirical_loss=float(losses.mean()),
                upper_bound=upper,
                n_units=len(losses),
                passes=upper <= alpha,
            )
        )
    passing = [certificate.threshold for certificate in certificates if certificate.passes]
    return ThresholdCertificate(
        selected_threshold=max(passing, default=0.0),
        alpha=float(alpha),
        delta=float(delta),
        unit="image" if unit_ids is None else "cluster",
        bound_method=bound_method,
        candidates=tuple(certificates),
    )
