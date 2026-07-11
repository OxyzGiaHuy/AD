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
from src.evaluation.reliability_routing import coverage_mask, risk_coverage_auc


def read_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


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


def fl(value: object, default: float = float("nan")) -> float:
    try:
        out = float(value)
        return out if np.isfinite(out) else default
    except Exception:
        return default


def metrics(rows: list[dict], prob_col: str) -> dict[str, float]:
    y = np.asarray([int(r["label"]) for r in rows], dtype=np.int64)
    raw = np.asarray([fl(r["raw_score"]) for r in rows], dtype=np.float64)
    p = np.clip(np.asarray([fl(r[prob_col]) for r in rows], dtype=np.float64), 0.0, 1.0)
    normal = y == 0
    anomaly = y == 1
    return {
        "n_images": len(rows),
        "auroc": roc_auc_score_np(y, raw),
        "ap": average_precision_np(y, raw),
        "ece": ece_binary(y, p),
        "brier": brier_score(y, p),
        "nll": nll_binary(y, p),
        "normal_mean_prob": float(np.mean(p[normal])) if np.any(normal) else float("nan"),
        "anomaly_mean_prob": float(np.mean(p[anomaly])) if np.any(anomaly) else float("nan"),
        "separation": float(np.mean(p[anomaly]) - np.mean(p[normal])) if np.any(normal) and np.any(anomaly) else float("nan"),
    }


def group_key(row: dict, group: str) -> tuple[str, str, str]:
    if group == "all":
        return ("all", "all", "all")
    if group == "k":
        return (row["k_shot"], "all", "all")
    if group == "k_corruption":
        return (row["k_shot"], row["corruption"], "all")
    if group == "class_k":
        return (row["class"], row["k_shot"], "all")
    if group == "class_k_corruption":
        return (row["class"], row["k_shot"], row["corruption"])
    raise ValueError(group)


def reliability_bins(rows: list[dict], prob_col: str, bins: int = 15) -> list[dict]:
    y = np.asarray([int(r["label"]) for r in rows], dtype=np.float64)
    p = np.clip(np.asarray([fl(r[prob_col]) for r in rows], dtype=np.float64), 0.0, 1.0)
    edges = np.linspace(0.0, 1.0, bins + 1)
    out = []
    for idx, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
        mask = (p >= lo) & (p < hi if hi < 1.0 else p <= hi)
        if not np.any(mask):
            out.append({"prob_col": prob_col, "bin": idx, "lo": lo, "hi": hi, "n": 0, "confidence": float("nan"), "accuracy": float("nan"), "gap": float("nan")})
            continue
        conf = float(np.mean(p[mask]))
        acc = float(np.mean(y[mask]))
        out.append({"prob_col": prob_col, "bin": idx, "lo": lo, "hi": hi, "n": int(mask.sum()), "confidence": conf, "accuracy": acc, "gap": abs(conf - acc)})
    return out


def entropy(prob: np.ndarray) -> np.ndarray:
    p = np.clip(prob, 1e-8, 1.0 - 1e-8)
    return -(p * np.log(p) + (1.0 - p) * np.log(1.0 - p))


def selective_rows(rows: list[dict], prob_col: str, group_name: str) -> list[dict]:
    y = np.asarray([int(r["label"]) for r in rows], dtype=np.int64)
    raw = np.asarray([fl(r["raw_score"]) for r in rows], dtype=np.float64)
    p = np.clip(np.asarray([fl(r[prob_col]) for r in rows], dtype=np.float64), 0.0, 1.0)
    risk_scores = {
        "entropy": entropy(p),
        "low_conformal_confidence": 1.0 - p,
        "raw_score_confidence_inverse": -raw,
    }
    if "n_eff_patch" in rows[0]:
        neff = np.asarray([fl(r.get("n_eff_patch", 0.0), 0.0) for r in rows], dtype=np.float64)
        risk_scores["low_n_eff_patch"] = -neff
    out = []
    coverages = [1.0, 0.95, 0.90, 0.80, 0.70]
    for risk_name, risk in risk_scores.items():
        curve_cov = []
        curve_ece = []
        full_ece = ece_binary(y, p)
        for cov in coverages:
            mask = coverage_mask(risk, cov)
            ece = ece_binary(y[mask], p[mask])
            out.append({
                "group": group_name,
                "prob_col": prob_col,
                "risk_score": risk_name,
                "coverage": cov,
                "n_total": len(rows),
                "n_kept": int(mask.sum()),
                "full_ece": full_ece,
                "selective_ece": ece,
                "relative_ece_reduction": (full_ece - ece) / full_ece if full_ece > 0 else float("nan"),
                "selective_brier": brier_score(y[mask], p[mask]),
                "selective_nll": nll_binary(y[mask], p[mask]),
                "selective_auroc": roc_auc_score_np(y[mask], raw[mask]),
                "selective_ap": average_precision_np(y[mask], raw[mask]),
            })
            curve_cov.append(cov)
            curve_ece.append(ece)
        out.append({
            "group": group_name,
            "prob_col": prob_col,
            "risk_score": risk_name,
            "coverage": "AURC",
            "n_total": len(rows),
            "n_kept": "",
            "full_ece": full_ece,
            "selective_ece": risk_coverage_auc(np.asarray(curve_cov), np.asarray(curve_ece)),
            "relative_ece_reduction": max((full_ece - np.asarray(curve_ece)) / full_ece) if full_ece > 0 else float("nan"),
            "selective_brier": "",
            "selective_nll": "",
            "selective_auroc": "",
            "selective_ap": "",
        })
    return out


def baseline_rows(delta_path: Path) -> list[dict]:
    if not delta_path.exists():
        return []
    out = []
    for r in read_csv(delta_path):
        for method, prefix in [("vector_platt", "vector"), ("shift_aware_vector_platt", "shift_aware")]:
            out.append({
                "group_type": "k_corruption",
                "key0": r["k_shot"],
                "key1": r["corruption"],
                "key2": "all",
                "prob_col": method,
                "n_images": int(r["n"]),
                "auroc": fl(r[f"{prefix}_auroc"]),
                "ap": fl(r[f"{prefix}_ap"]),
                "ece": fl(r[f"{prefix}_ece"]),
                "brier": fl(r[f"{prefix}_brier"]),
                "nll": fl(r[f"{prefix}_nll"]),
                "normal_mean_prob": float("nan"),
                "anomaly_mean_prob": float("nan"),
                "separation": float("nan"),
            })
    return out


def markdown_table(rows: list[dict], title: str, columns: list[str]) -> str:
    lines = [f"## {title}", "", "| " + " | ".join(columns) + " |", "|" + "|".join(["---"] * len(columns)) + "|"]
    for r in rows:
        vals = []
        for c in columns:
            v = r.get(c, "")
            if isinstance(v, float):
                vals.append(f"{v:.4f}")
            else:
                try:
                    fv = float(v)
                    vals.append(f"{fv:.4f}") if c not in {"n_images"} else vals.append(str(int(fv)))
                except Exception:
                    vals.append(str(v))
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/paper_tables/sw_cad_image_views_visa_full_k4k8_s0s4_combined.csv")
    parser.add_argument("--baseline-delta", default="outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_delta.csv")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    args = parser.parse_args()
    rows = [r for r in read_csv(Path(args.input)) if r.get("label") in {"0", "1"}]
    out_dir = Path(args.out_dir)
    prob_cols = ["conformal_prob_loio", "conformal_prob_weighted"]

    summary = []
    for group in ["all", "k", "k_corruption", "class_k", "class_k_corruption"]:
        groups: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
        for r in rows:
            groups[group_key(r, group)].append(r)
        for key, gr in sorted(groups.items()):
            for prob_col in prob_cols:
                summary.append({"group_type": group, "key0": key[0], "key1": key[1], "key2": key[2], "prob_col": prob_col, **metrics(gr, prob_col)})
    baseline = baseline_rows(Path(args.baseline_delta))
    write_csv(out_dir / "visa_full_conformal_extended_summary.csv", summary)
    write_csv(out_dir / "visa_full_conformal_vs_baselines_k_corruption.csv", baseline + [r for r in summary if r["group_type"] == "k_corruption"])

    bins = []
    for prob_col in prob_cols:
        bins.extend(reliability_bins(rows, prob_col))
        for k in ["4", "8"]:
            bins.extend([{**b, "k_shot": k} for b in reliability_bins([r for r in rows if r["k_shot"] == k], prob_col)])
    write_csv(out_dir / "visa_full_conformal_reliability_bins.csv", bins)

    selective = []
    for prob_col in prob_cols:
        selective.extend(selective_rows(rows, prob_col, "all"))
        for k in ["4", "8"]:
            selective.extend(selective_rows([r for r in rows if r["k_shot"] == k], prob_col, f"k={k}"))
    write_csv(out_dir / "visa_full_conformal_selective_reliability.csv", selective)

    main_rows = [r for r in summary if r["group_type"] in {"all", "k"}]
    main_rows = sorted(main_rows, key=lambda r: (r["group_type"], r["key0"], r["prob_col"]))
    kc_rows = [r for r in summary if r["group_type"] == "k_corruption" and r["prob_col"] == "conformal_prob_loio"]
    kc_rows = sorted(kc_rows, key=lambda r: (r["key0"], r["key1"]))
    class_rows = [r for r in summary if r["group_type"] == "class_k" and r["prob_col"] == "conformal_prob_loio"]
    class_rows = sorted(class_rows, key=lambda r: float(r["ece"]), reverse=True)
    md = [
        "# Full VisA Conformal Reliability Tables",
        "",
        "Source: `sw_cad_image_views_visa_full_k4k8_s0s4_combined.csv` (`480/480` cases, `56,000` images).",
        "",
        markdown_table(main_rows, "Main Full VisA Metrics", ["group_type", "key0", "prob_col", "n_images", "auroc", "ap", "ece", "brier", "nll", "normal_mean_prob", "anomaly_mean_prob", "separation"]),
        "",
        markdown_table(kc_rows, "LOIO By k And Corruption", ["key0", "key1", "n_images", "auroc", "ap", "ece", "brier", "nll", "normal_mean_prob", "anomaly_mean_prob", "separation"]),
        "",
        markdown_table(class_rows[:20], "Worst Class-k ECE Cases For LOIO", ["key0", "key1", "n_images", "auroc", "ap", "ece", "brier", "nll", "normal_mean_prob", "anomaly_mean_prob", "separation"]),
    ]
    (out_dir / "visa_full_conformal_main_table.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print("wrote full VisA conformal analysis artifacts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
