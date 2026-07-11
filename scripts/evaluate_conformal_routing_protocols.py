from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.evaluation.metrics import average_precision_np, brier_score, ece_binary, nll_binary, roc_auc_score_np

PROB_COLS = [
    "vector_platt",
    "shift_aware_vector_platt",
    "weighted_platt",
    "anchored_structured_gate",
    "conformal_prob_loio",
    "conformal_prob_weighted",
]


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    return [r for r in rows if str(r.get("label", "")).strip() in {"0", "1"}]


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    fields = list(rows[0].keys())
    for row in rows[1:]:
        for key in row:
            if key not in fields:
                fields.append(key)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def f(row: dict, key: str, default: float = 0.0) -> float:
    try:
        value = float(row.get(key, default))
        if np.isnan(value):
            return default
        return value
    except Exception:
        return default


def labels_raw(rows: list[dict]) -> tuple[np.ndarray, np.ndarray]:
    labels = np.asarray([int(r["label"]) for r in rows], dtype=np.int64)
    raw = np.asarray([f(r, "raw_score") for r in rows], dtype=np.float64)
    return labels, raw


def summarize(rows: list[dict], probs: np.ndarray) -> dict[str, float]:
    labels, raw = labels_raw(rows)
    return {
        "auroc": roc_auc_score_np(labels, raw),
        "ap": average_precision_np(labels, raw),
        "ece": ece_binary(labels, probs),
        "brier": brier_score(labels, probs),
        "nll": nll_binary(labels, probs),
    }


def prob_array(rows: list[dict], col: str) -> np.ndarray:
    return np.asarray([np.clip(f(r, col), 0.0, 1.0) for r in rows], dtype=np.float64)


def entropy(p: np.ndarray) -> np.ndarray:
    p = np.clip(p, 1e-8, 1.0 - 1e-8)
    return -(p * np.log(p) + (1.0 - p) * np.log(1.0 - p))


def no_label_rule_probs(rows: list[dict], rule: str) -> np.ndarray:
    vector = prob_array(rows, "vector_platt")
    conformal = prob_array(rows, "conformal_prob_loio")
    weighted = prob_array(rows, "conformal_prob_weighted")
    anchored = prob_array(rows, "anchored_structured_gate")
    if rule == "fixed_vector":
        return vector
    if rule == "fixed_conformal_loio":
        return conformal
    if rule == "fixed_conformal_weighted":
        return weighted
    if rule == "fixed_vector_conformal_mix_50_50":
        return 0.5 * vector + 0.5 * conformal
    if rule == "no_label_shift_or_neff_gate":
        out = vector.copy()
        shift = np.asarray([f(r, "domain_shift_strength") for r in rows])
        neff = np.asarray([f(r, "n_eff_ratio", 1.0) for r in rows])
        patch_neff = np.asarray([f(r, "n_eff_patch", 1.0) for r in rows])
        # Fixed, label-free thresholds. These are intentionally conservative:
        # use conformal only when shift is visibly high or effective sample size is low.
        use_conf = (shift >= 0.45) | (neff <= 0.75) | (patch_neff <= 1000.0)
        out[use_conf] = conformal[use_conf]
        return out
    if rule == "no_label_entropy_agreement_gate":
        out = vector.copy()
        ent_vec = entropy(vector)
        ent_conf = entropy(conformal)
        disagreement = np.abs(vector - anchored)
        use_conf = (ent_conf <= ent_vec) & (disagreement >= 0.10)
        out[use_conf] = conformal[use_conf]
        return out
    raise ValueError(f"Unknown no-label rule: {rule}")


def class_splits(rows: list[dict]) -> list[tuple[str, list[dict], list[dict]]]:
    out = []
    datasets = sorted({r["dataset"] for r in rows})
    for dataset in datasets:
        drows = [r for r in rows if r["dataset"] == dataset]
        classes = sorted({r["class"] for r in drows})
        for cls in classes:
            test = [r for r in drows if r["class"] == cls]
            val = [r for r in drows if r["class"] != cls]
            if val and test:
                out.append((f"loco:{dataset}:{cls}", val, test))
        if len(classes) >= 4:
            pivot = max(1, len(classes) // 2)
            val_classes = set(classes[:pivot])
            test_classes = set(classes[pivot:])
            val = [r for r in drows if r["class"] in val_classes]
            test = [r for r in drows if r["class"] in test_classes]
            out.append((f"within:{dataset}:class_split", val, test))
    for source, target in [("mvtec", "visa"), ("visa", "mvtec")]:
        val = [r for r in rows if r["dataset"] == source]
        test = [r for r in rows if r["dataset"] == target]
        if val and test:
            out.append((f"cross:{source}_to_{target}", val, test))
    return out


def best_col_by_ece(rows: list[dict], cols: list[str]) -> tuple[str, float]:
    labels, _raw = labels_raw(rows)
    best_col = cols[0]
    best_ece = float("inf")
    for col in cols:
        p = prob_array(rows, col)
        ece = ece_binary(labels, p)
        if ece < best_ece:
            best_col = col
            best_ece = ece
    return best_col, best_ece


def eval_protocol(split: str, test_rows: list[dict], method: str, probs: np.ndarray, validation_choice: str = "none", validation_ece: float = float("nan")) -> dict:
    metrics = summarize(test_rows, probs)
    vector_metrics = summarize(test_rows, prob_array(test_rows, "vector_platt"))
    return {
        "split": split,
        "split_group": split if split.startswith("cross:") else split.split(":")[0],
        "method": method,
        "validation_choice": validation_choice,
        "n_images": len(test_rows),
        "validation_ece": validation_ece,
        "ece": metrics["ece"],
        "vector_ece": vector_metrics["ece"],
        "delta_ece_vs_vector": metrics["ece"] - vector_metrics["ece"],
        "brier": metrics["brier"],
        "nll": metrics["nll"],
        "auroc": metrics["auroc"],
        "ap": metrics["ap"],
        "no_harm_vs_vector": float(metrics["ece"] <= vector_metrics["ece"] + 0.01),
    }


def aggregate(rows: list[dict]) -> list[dict]:
    groups: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for row in rows:
        groups[(row["split_group"], row["method"])].append(row)
    out = []
    for (split_group, method), group in sorted(groups.items()):
        n = sum(int(r["n_images"]) for r in group)
        def wavg(key: str) -> float:
            return sum(float(r[key]) * int(r["n_images"]) for r in group) / max(n, 1)
        out.append({
            "split_group": split_group,
            "method": method,
            "n_images": n,
            "mean_ece": wavg("ece"),
            "mean_vector_ece": wavg("vector_ece"),
            "mean_delta_ece_vs_vector": wavg("delta_ece_vs_vector"),
            "mean_brier": wavg("brier"),
            "mean_nll": wavg("nll"),
            "no_harm_rate": sum(float(r["no_harm_vs_vector"]) * int(r["n_images"]) for r in group) / max(n, 1),
            "worst_split_ece": max(float(r["ece"]) for r in group),
        })
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", default="outputs/paper_tables/sage_sample_gate_representative_with_conformal_full.csv")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="conformal_routing_protocols")
    args = parser.parse_args()
    rows = read_csv(Path(args.predictions))
    rows = [r for r in rows if all(str(r.get(c, "")).strip() for c in ["vector_platt", "conformal_prob_loio"])]
    detail = []
    no_label_rules = [
        "fixed_vector",
        "fixed_conformal_loio",
        "fixed_conformal_weighted",
        "fixed_vector_conformal_mix_50_50",
        "no_label_shift_or_neff_gate",
        "no_label_entropy_agreement_gate",
    ]
    validation_cols = ["vector_platt", "shift_aware_vector_platt", "weighted_platt", "anchored_structured_gate", "conformal_prob_loio", "conformal_prob_weighted"]
    for split, val_rows, test_rows in class_splits(rows):
        for rule in no_label_rules:
            detail.append(eval_protocol(split, test_rows, rule, no_label_rule_probs(test_rows, rule)))
        best_col, val_ece = best_col_by_ece(val_rows, validation_cols)
        detail.append(eval_protocol(split, test_rows, "validation_best_expert_all", prob_array(test_rows, best_col), best_col, val_ece))
        best_safe, safe_ece = best_col_by_ece(val_rows, ["vector_platt", "conformal_prob_loio"])
        detail.append(eval_protocol(split, test_rows, "validation_best_vector_or_conformal", prob_array(test_rows, best_safe), best_safe, safe_ece))
    out_dir = Path(args.out_dir)
    write_csv(out_dir / f"{args.run_tag}_detailed.csv", detail)
    write_csv(out_dir / f"{args.run_tag}_summary.csv", aggregate(detail))
    print(f"wrote {len(detail)} detailed rows from {len(rows)} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
