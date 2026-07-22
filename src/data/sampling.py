from __future__ import annotations

import math
from collections import defaultdict
from collections.abc import Sequence

import numpy as np

from .datasets import ImageRecord


def _sample_without_replacement(records: Sequence[ImageRecord], count: int, rng: np.random.Generator) -> list[ImageRecord]:
    ordered = sorted(records, key=lambda rec: rec.path)
    indices = np.sort(rng.choice(len(ordered), size=count, replace=False))
    return [ordered[int(index)] for index in indices]


def few_shot_support(records: Sequence[ImageRecord], k: int, seed: int) -> list[ImageRecord]:
    """Take a deterministic nested prefix of train-normal images per category.

    For a fixed category and seed, support(k=1) is a subset of support(k=2),
    and so on. This makes k-shot comparisons paired instead of silently changing
    every support image when k changes.
    """

    if k < 1:
        raise ValueError("k must be positive.")
    by_category: dict[str, list[ImageRecord]] = defaultdict(list)
    for record in records:
        if record.split == "train" and record.label == 0:
            by_category[record.category].append(record)
    if not by_category:
        raise ValueError("No train-normal records are available for few-shot support.")
    rng = np.random.default_rng(seed)
    support: list[ImageRecord] = []
    for category in sorted(by_category):
        candidates = by_category[category]
        if len(candidates) < k:
            raise ValueError(f"Category {category!r} has {len(candidates)} train-normal images, fewer than k={k}.")
        ordered = sorted(candidates, key=lambda record: record.path)
        permutation = rng.permutation(len(ordered))
        selected = sorted(int(index) for index in permutation[:k])
        support.extend(ordered[index] for index in selected)
    return support


def evaluation_records(records: Sequence[ImageRecord]) -> list[ImageRecord]:
    """Return only test records in a deterministic order."""

    return sorted((record for record in records if record.split == "test"), key=lambda rec: (rec.category, rec.label, rec.defect_type, rec.path))


def split_calibration(
    records: Sequence[ImageRecord],
    seed: int,
    anomaly_fraction: float = 0.2,
) -> tuple[list[ImageRecord], list[ImageRecord]]:
    """Hold out labeled test anomalies for the explicitly upper-bound protocol.

    Sampling is stratified by category and always leaves at least one anomaly
    per category in evaluation. It must not be used by the label-free main
    protocol.
    """

    if not 0.0 < anomaly_fraction < 1.0:
        raise ValueError("anomaly_fraction must lie strictly between 0 and 1.")
    anomalies: dict[str, list[ImageRecord]] = defaultdict(list)
    evaluation = evaluation_records(records)
    for record in evaluation:
        if record.label == 1:
            anomalies[record.category].append(record)
    if not anomalies:
        raise ValueError("No test anomalies are available for calibration holdout.")
    rng = np.random.default_rng(seed)
    calibration: list[ImageRecord] = []
    for category in sorted(anomalies):
        candidates = anomalies[category]
        if len(candidates) < 2:
            raise ValueError(f"Category {category!r} needs at least two anomalies to keep evaluation non-empty.")
        count = min(len(candidates) - 1, max(1, int(math.floor(len(candidates) * anomaly_fraction))))
        calibration.extend(_sample_without_replacement(candidates, count, rng))
    held_out = set(calibration)
    remaining = [record for record in evaluation if record not in held_out]
    return calibration, remaining
