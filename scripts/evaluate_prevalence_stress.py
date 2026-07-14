from __future__ import annotations

import argparse
import csv
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, roc_auc_score


DEFAULT_PROB_COLS = [
    "vector_platt",
    "shift_aware_vector_platt",
    "weighted_platt",
    "anchored_structured_gate",
    "conformal_prob_loio",
    "conformal_prob_weighted",
]


def expected_calibration_error(labels: np.ndarray, probs: np.ndarray, bins: int) -> float:
    edges = np.linspace(0.0, 1.0, bins + 1)
    total = len(labels)
    error = 0.0
    for index in range(bins):
        upper_inclusive = index == bins - 1
        mask = (probs >= edges[index]) & (
            probs <= edges[index + 1] if upper_inclusive else probs < edges[index + 1]
        )
        if np.any(mask):
            error += mask.mean() * abs(float(labels[mask].mean()) - float(probs[mask].mean()))
    return float(error)


def metrics(labels: np.ndarray, probs: np.ndarray, bins: int) -> dict[str, float]:
    clipped = np.clip(probs.astype(np.float64), 1e-7, 1.0 - 1e-7)
    return {
        "ece": expected_calibration_error(labels, clipped, bins),
        "brier": float(np.mean((clipped - labels) ** 2)),
        "nll": float(-np.mean(labels * np.log(clipped) + (1 - labels) * np.log(1 - clipped))),
        "auroc": float(roc_auc_score(labels, clipped)),
        "ap": float(average_precision_score(labels, clipped)),
        "mean_probability": float(clipped.mean()),
    }


def prevalence_sample(
    frame: pd.DataFrame,
    prevalence: float,
    rng: np.random.Generator,
) -> pd.DataFrame:
    normal = frame[frame["label"] == 0]
    anomaly = frame[frame["label"] == 1]
    if normal.empty or anomaly.empty:
        raise ValueError("Each group needs both normal and anomalous images")
    n_normal = len(normal)
    n_anomaly = max(1, int(round(prevalence / (1.0 - prevalence) * n_normal)))
    sampled_anomaly = anomaly.iloc[rng.choice(len(anomaly), size=n_anomaly, replace=n_anomaly > len(anomaly))]
    return pd.concat([normal, sampled_anomaly], ignore_index=True)


def evaluate(
    frame: pd.DataFrame,
    prob_cols: list[str],
    prevalences: list[float],
    repeats: int,
    bins: int,
    seed: int,
) -> pd.DataFrame:
    group_cols = ["dataset", "class", "k_shot", "seed", "corruption"]
    available_groups = [column for column in group_cols if column in frame.columns]
    rows: list[dict] = []
    for group_key, group in frame.groupby(available_groups, dropna=False):
        if not isinstance(group_key, tuple):
            group_key = (group_key,)
        group_info = dict(zip(available_groups, group_key))
        if group["label"].nunique() < 2:
            continue
        for prevalence in prevalences:
            for repeat in range(repeats):
                key_seed = seed + repeat + int(prevalence * 10000)
                rng = np.random.default_rng(key_seed)
                sampled = prevalence_sample(group, prevalence, rng)
                labels = sampled["label"].to_numpy(dtype=np.int64)
                realized = float(labels.mean())
                for column in prob_cols:
                    if column not in sampled.columns:
                        continue
                    probs = pd.to_numeric(sampled[column], errors="coerce").to_numpy(dtype=np.float64)
                    valid = np.isfinite(probs)
                    if valid.sum() < 2 or np.unique(labels[valid]).size < 2:
                        continue
                    row = {
                        **group_info,
                        "method": column,
                        "target_prevalence": prevalence,
                        "realized_prevalence": realized,
                        "repeat": repeat,
                        "n_images": int(valid.sum()),
                    }
                    row.update(metrics(labels[valid], probs[valid], bins))
                    rows.append(row)
    return pd.DataFrame(rows)


def summarize(detailed: pd.DataFrame) -> pd.DataFrame:
    metrics_cols = ["ece", "brier", "nll", "auroc", "ap", "mean_probability"]
    group_cols = ["dataset", "method", "target_prevalence"]
    aggregate = detailed.groupby(group_cols)[metrics_cols].agg(["mean", "std"]).reset_index()
    aggregate.columns = [
        "_".join(str(part) for part in column if part)
        if isinstance(column, tuple)
        else str(column)
        for column in aggregate.columns
    ]
    return aggregate


def write_csv(path: Path, frame: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False, quoting=csv.QUOTE_MINIMAL)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", required=True)
    parser.add_argument("--prob-cols", nargs="*", default=DEFAULT_PROB_COLS)
    parser.add_argument("--prevalences", nargs="*", type=float, default=[0.01, 0.05, 0.10, 0.25, 0.50])
    parser.add_argument("--repeats", type=int, default=20)
    parser.add_argument("--bins", type=int, default=15)
    parser.add_argument("--seed", type=int, default=2026)
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="representative")
    args = parser.parse_args()

    frame = pd.read_csv(args.predictions)
    detailed = evaluate(
        frame,
        args.prob_cols,
        args.prevalences,
        args.repeats,
        args.bins,
        args.seed,
    )
    summary = summarize(detailed)
    out_dir = Path(args.out_dir)
    write_csv(out_dir / f"prevalence_stress_{args.run_tag}_detailed.csv", detailed)
    write_csv(out_dir / f"prevalence_stress_{args.run_tag}_summary.csv", summary)
    print(f"wrote {len(detailed)} detailed rows and {len(summary)} summary rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
