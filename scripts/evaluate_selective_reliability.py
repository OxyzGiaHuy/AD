from __future__ import annotations

import argparse
import csv
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.calibration.platt import entropy_binary
from src.evaluation.reliability_routing import combined_minmax_score, coverage_mask, risk_coverage_auc, summarize_probs

EXPERTS = ["vector_platt", "shift_aware_vector_platt", "weighted_platt", "anchored_structured_gate"]


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


def arrays(rows: list[dict], prob_col: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    labels = np.asarray([int(r["label"]) for r in rows], dtype=np.int64)
    raw = np.asarray([float(r["raw_score"]) for r in rows], dtype=np.float64)
    probs = np.asarray([float(r[prob_col]) for r in rows], dtype=np.float64)
    return labels, raw, probs


def risk_scores(rows: list[dict], prob_col: str) -> dict[str, np.ndarray]:
    probs = np.asarray([float(r[prob_col]) for r in rows], dtype=np.float64)
    expert_probs = np.asarray([[float(r[e]) for e in EXPERTS if e in r] for r in rows], dtype=np.float64)
    entropy = entropy_binary(probs)
    entropies = np.asarray([[float(r.get(f"entropy_{e}", entropy_binary(np.asarray([float(r[e])]))[0])) for e in EXPERTS if e in r] for r in rows], dtype=np.float64)
    disagreement = expert_probs.max(axis=1) - expert_probs.min(axis=1)
    raw = np.asarray([float(r["raw_score"]) for r in rows], dtype=np.float64)
    n_eff_ratio = np.asarray([float(r.get("n_eff_ratio", 1.0)) for r in rows], dtype=np.float64)
    domain_shift = np.asarray([float(r.get("domain_shift_strength", 0.0)) for r in rows], dtype=np.float64)
    base = {
        "entropy_selected": entropy,
        "entropy_mean_experts": entropies.mean(axis=1),
        "entropy_max_experts": entropies.max(axis=1),
        "expert_disagreement": disagreement,
        "low_n_eff": 1.0 - np.clip(n_eff_ratio, 0.0, 1.0),
        "domain_shift_strength": domain_shift,
        "raw_score_confidence_inverse": -np.abs((raw - np.nanmean(raw)) / (np.nanstd(raw) + 1e-8)),
    }
    base["combined_entropy_disagreement_neff"] = combined_minmax_score([base["entropy_selected"], disagreement, base["low_n_eff"]])
    return base


def evaluate_group(rows: list[dict], group_name: str, prob_col: str, coverage_levels: list[float]) -> tuple[list[dict], list[dict]]:
    labels, raw, probs = arrays(rows, prob_col)
    full = summarize_probs(labels, raw, probs)
    score_map = risk_scores(rows, prob_col)
    detailed = []
    auc_rows = []
    for score_name, scores in score_map.items():
        coverages = []
        risks = []
        for coverage in coverage_levels:
            mask = coverage_mask(scores, coverage)
            kept_labels, kept_raw, kept_probs = labels[mask], raw[mask], probs[mask]
            metrics = summarize_probs(kept_labels, kept_raw, kept_probs)
            abstained = ~mask
            detailed.append({
                "group": group_name,
                "prob_col": prob_col,
                "risk_score": score_name,
                "coverage": coverage,
                "n_total": len(rows),
                "n_kept": int(mask.sum()),
                "n_abstained": int(abstained.sum()),
                "abstained_anomaly_rate": float(labels[abstained].mean()) if np.any(abstained) else float("nan"),
                "full_ece": full["ece"],
                "selective_ece": metrics["ece"],
                "relative_ece_reduction": (full["ece"] - metrics["ece"]) / max(full["ece"], 1e-12),
                "selective_brier": metrics["brier"],
                "selective_nll": metrics["nll"],
                "selective_auroc": metrics["auroc"],
                "selective_ap": metrics["ap"],
            })
            coverages.append(coverage)
            risks.append(metrics["ece"])
        auc_rows.append({
            "group": group_name,
            "prob_col": prob_col,
            "risk_score": score_name,
            "aurc_ece": risk_coverage_auc(np.asarray(coverages), np.asarray(risks)),
            "full_ece": full["ece"],
            "best_relative_ece_reduction": max(float(r["relative_ece_reduction"]) for r in detailed if r["group"] == group_name and r["prob_col"] == prob_col and r["risk_score"] == score_name),
        })
    return detailed, auc_rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--predictions", default="outputs/paper_tables/sage_sample_gate_representative_predictions.csv")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="representative")
    parser.add_argument("--prob-cols", nargs="*", default=["vector_platt", "weighted_platt", "shift_aware_vector_platt", "anchored_structured_gate"])
    parser.add_argument("--coverages", nargs="*", type=float, default=[1.0, 0.95, 0.9, 0.8, 0.7])
    args = parser.parse_args()
    rows = read_csv(Path(args.predictions))
    groups: dict[str, list[dict]] = {"all": rows}
    for dataset in sorted({r["dataset"] for r in rows}):
        groups[f"dataset:{dataset}"] = [r for r in rows if r["dataset"] == dataset]
    detailed = []
    aucs = []
    for group_name, group_rows in groups.items():
        for prob_col in args.prob_cols:
            if prob_col not in group_rows[0]:
                continue
            d, a = evaluate_group(group_rows, group_name, prob_col, args.coverages)
            detailed.extend(d)
            aucs.extend(a)
    out_dir = Path(args.out_dir)
    write_csv(out_dir / f"selective_reliability_{args.run_tag}.csv", detailed)
    write_csv(out_dir / f"risk_coverage_curves_{args.run_tag}.csv", aucs)
    print(f"wrote {len(detailed)} selective rows and {len(aucs)} auc rows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
