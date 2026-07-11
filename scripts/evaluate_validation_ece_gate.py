from __future__ import annotations

import argparse
import csv
from collections import Counter, defaultdict
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.evaluation.reliability_routing import (
    choose_best_expert_by_ece,
    choose_best_mixture_by_ece,
    mixture_probs,
    risk_ece_weights,
    sage_hier_ece_weights,
    summarize_probs,
)

DEFAULT_EXPERTS = ["vector_platt", "shift_aware_vector_platt", "weighted_platt", "anchored_structured_gate"]


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fieldnames = list(rows[0].keys())
    for row in rows[1:]:
        for key in row:
            if key not in fieldnames:
                fieldnames.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def arrays(rows: list[dict], experts: list[str]) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    labels = np.asarray([int(r["label"]) for r in rows], dtype=np.int64)
    raw = np.asarray([float(r["raw_score"]) for r in rows], dtype=np.float64)
    probs = np.asarray([[float(r[e]) for e in experts] for r in rows], dtype=np.float64)
    return labels, raw, probs, np.arange(len(rows))


def row_filter(rows: list[dict], dataset: str | None = None, cls: str | None = None) -> list[int]:
    out = []
    for i, row in enumerate(rows):
        if dataset is not None and row["dataset"] != dataset:
            continue
        if cls is not None and row["class"] != cls:
            continue
        out.append(i)
    return out


def split_validation_classes(classes: list[str], test_cls: str) -> list[str]:
    candidates = [c for c in classes if c != test_cls]
    if not candidates:
        return []
    return [candidates[0]]


def eval_with_weights(name: str, split: str, rows: list[dict], test_idx: list[int], val_idx: list[int], experts: list[str], weights: np.ndarray, validation_ece: float | None = None) -> dict:
    test = [rows[i] for i in test_idx]
    labels, raw, probs, _ = arrays(test, experts)
    pred = mixture_probs(probs, weights)
    metrics = summarize_probs(labels, raw, pred)
    vector = probs[:, experts.index("vector_platt")]
    vector_metrics = summarize_probs(labels, raw, vector)
    selected = int(np.argmax(weights))
    usage = Counter()
    if np.max(weights) >= 0.999:
        usage[experts[selected]] = len(test)
    else:
        usage["soft_mix"] = len(test)
    return {
        "gate": name,
        "split": split,
        "dataset": "+".join(sorted({r["dataset"] for r in test})),
        "n_images": len(test),
        "validation_n_images": len(val_idx),
        "validation_ece": float(validation_ece) if validation_ece is not None else float("nan"),
        "test_ece": metrics["ece"],
        "vector_ece": vector_metrics["ece"],
        "delta_ece_vs_vector": metrics["ece"] - vector_metrics["ece"],
        "test_brier": metrics["brier"],
        "test_nll": metrics["nll"],
        "test_auroc": metrics["auroc"],
        "test_ap": metrics["ap"],
        "no_harm_ece_vs_vector": float(metrics["ece"] <= vector_metrics["ece"] + 0.01),
        "weights": ";".join(f"{e}:{weights[i]:.4f}" for i, e in enumerate(experts)),
        "usage": ";".join(f"{k}:{v}" for k, v in usage.items()),
    }


def tune_rows(rows: list[dict], val_idx: list[int], experts: list[str], margin: float, grid_step: float) -> dict[str, tuple[np.ndarray, float]]:
    val = [rows[i] for i in val_idx]
    labels, _raw, probs, _ = arrays(val, experts)
    anchor_idx = experts.index("vector_platt")
    out: dict[str, tuple[np.ndarray, float]] = {}
    best = choose_best_expert_by_ece(labels, probs)
    w = np.zeros(len(experts), dtype=np.float64); w[best] = 1.0
    out["ece_grid_gate"] = (w, float(__import__('src.evaluation.metrics', fromlist=['ece_binary']).ece_binary(labels, probs[:, best])))
    out["risk_ece_gate"] = (risk_ece_weights(labels, probs, anchor_index=anchor_idx, margin=margin), float("nan"))
    out["sage_hier_ece_gate"] = sage_hier_ece_weights(labels, probs, anchor_index=anchor_idx)
    out["soft_mix_ece_gate"] = choose_best_mixture_by_ece(labels, probs, step=grid_step)
    return out


def make_splits(rows: list[dict]) -> list[tuple[str, list[int], list[int]]]:
    splits = []
    datasets = sorted({r["dataset"] for r in rows})
    for dataset in datasets:
        classes = sorted({r["class"] for r in rows if r["dataset"] == dataset})
        for cls in classes:
            test_idx = row_filter(rows, dataset=dataset, cls=cls)
            val_classes = split_validation_classes(classes, cls)
            val_idx = [i for i, r in enumerate(rows) if r["dataset"] == dataset and r["class"] in val_classes]
            if val_idx and test_idx:
                splits.append((f"loco:{dataset}:{cls}", val_idx, test_idx))
        if len(classes) >= 4:
            train_val = classes[: max(1, len(classes) // 2)]
            test = classes[max(1, len(classes) // 2):]
            val_idx = [i for i, r in enumerate(rows) if r["dataset"] == dataset and r["class"] in train_val]
            test_idx = [i for i, r in enumerate(rows) if r["dataset"] == dataset and r["class"] in test]
            if val_idx and test_idx:
                splits.append((f"within:{dataset}:class_split", val_idx, test_idx))
    for source, target in [("visa", "mvtec"), ("mvtec", "visa")]:
        val_idx = [i for i, r in enumerate(rows) if r["dataset"] == source]
        test_idx = [i for i, r in enumerate(rows) if r["dataset"] == target]
        if val_idx and test_idx:
            splits.append((f"cross:{source}_to_{target}", val_idx, test_idx))
    if not splits and rows:
        idx = list(range(len(rows)))
        splits.append(("smoke:all", idx, idx))
    return splits


def aggregate(rows: list[dict]) -> list[dict]:
    groups: dict[tuple, list[dict]] = defaultdict(list)
    for row in rows:
        split_group = row["split"].split(":")[0]
        if row["split"].startswith("cross:"):
            split_group = row["split"]
        groups[(split_group, row["gate"])].append(row)
    out = []
    for (split_group, gate), group in sorted(groups.items()):
        n = sum(int(r["n_images"]) for r in group)
        def wavg(key: str) -> float:
            return sum(float(r[key]) * int(r["n_images"]) for r in group) / max(n, 1)
        no = sum(float(r["no_harm_ece_vs_vector"]) * int(r["n_images"]) for r in group)
        out.append({
            "split_group": split_group,
            "gate": gate,
            "n_images": n,
            "mean_test_ece": wavg("test_ece"),
            "mean_vector_ece": wavg("vector_ece"),
            "mean_delta_ece_vs_vector": wavg("delta_ece_vs_vector"),
            "mean_brier": wavg("test_brier"),
            "mean_nll": wavg("test_nll"),
            "no_harm_rate": no / max(n, 1),
            "worst_split_ece": max(float(r["test_ece"]) for r in group),
        })
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", default="outputs/paper_tables/sage_sample_gate_representative_predictions.csv")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="representative")
    parser.add_argument("--experts", nargs="*", default=DEFAULT_EXPERTS)
    parser.add_argument("--margin", type=float, default=0.005)
    parser.add_argument("--grid-step", type=float, default=0.25)
    args = parser.parse_args()
    rows = read_csv(Path(args.predictions))
    missing = [e for e in args.experts if e not in rows[0]]
    if missing:
        raise ValueError(f"Missing expert columns: {missing}")
    rows = [r for r in rows if all(str(r.get(e, "")).strip() != "" for e in args.experts)]
    if not rows:
        raise ValueError("No rows contain all requested expert columns.")
    detailed = []
    for split, val_idx, test_idx in make_splits(rows):
        tuned = tune_rows(rows, val_idx, args.experts, args.margin, args.grid_step)
        for name, (weights, val_ece) in tuned.items():
            detailed.append(eval_with_weights(name, split, rows, test_idx, val_idx, args.experts, weights, val_ece))
    out_dir = Path(args.out_dir)
    write_csv(out_dir / f"validation_ece_gate_{args.run_tag}_detailed.csv", detailed)
    write_csv(out_dir / f"validation_ece_gate_{args.run_tag}_summary.csv", aggregate(detailed))
    print(f"wrote {len(detailed)} detailed rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
