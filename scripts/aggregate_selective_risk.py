from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd
from src.evaluation.metrics import average_precision_np, roc_auc_score_np


def parse_run_name(name: str) -> dict[str, str | int]:
    dataset = "visa" if "_visa_" in name else "mvtec" if "_mvtec_" in name else "unknown"
    variant = "unknown"
    for candidate in ["calib_subspace_head", "anomalydino", "patchcore", "subspacead", "head_pca"]:
        if name.startswith(candidate + "_") or f"_{candidate}_" in name:
            variant = candidate
            break
    corruption = "clean"
    if "_fgsm_" in name:
        corruption = name[name.index("fgsm_") :]
    for candidate in ["gaussian_noise", "brightness_contrast", "blur", "jpeg"]:
        if name.endswith("_" + candidate):
            corruption = candidate
    k = -1
    seed = -1
    for part in name.split("_"):
        if part.startswith("k") and part[1:].isdigit():
            k = int(part[1:])
        if part.startswith("seed") and part[4:].isdigit():
            seed = int(part[4:])
    return {"dataset": dataset, "variant": variant, "k_shot": k, "seed": seed, "shift": corruption}


def read_predictions(run_dir: Path) -> pd.DataFrame | None:
    parquet = run_dir / "predictions.parquet"
    csv_path = run_dir / "predictions.csv"
    if parquet.exists():
        return pd.read_parquet(parquet)
    if csv_path.exists():
        return pd.read_csv(csv_path)
    return None


def safe_auc(labels: np.ndarray, scores: np.ndarray) -> float:
    if len(np.unique(labels)) < 2:
        return float("nan")
    return float(roc_auc_score_np(labels, scores))


def safe_ap(labels: np.ndarray, scores: np.ndarray) -> float:
    if len(np.unique(labels)) < 2:
        return float("nan")
    return float(average_precision_np(labels, scores))


def evaluate_run(run_dir: Path, coverages: list[float]) -> list[dict]:
    df = read_predictions(run_dir)
    if df is None or "label" not in df or "entropy" not in df:
        return []
    score_col = "calibrated_probability" if "calibrated_probability" in df else "raw_score"
    if score_col not in df:
        return []
    labels = df["label"].to_numpy(dtype=np.int64)
    scores = df[score_col].to_numpy(dtype=np.float64)
    entropy = df["entropy"].to_numpy(dtype=np.float64)
    order = np.argsort(entropy)
    meta = parse_run_name(run_dir.name)
    rows = []
    risks = []
    for coverage in coverages:
        n_keep = max(2, int(round(len(order) * coverage)))
        idx = order[:n_keep]
        auc = safe_auc(labels[idx], scores[idx])
        ap = safe_ap(labels[idx], scores[idx])
        risk = float(1.0 - auc) if np.isfinite(auc) else float("nan")
        risks.append(risk)
        rows.append(
            {
                **meta,
                "run_id": run_dir.name,
                "coverage": coverage,
                "n": n_keep,
                "auroc": auc,
                "ap": ap,
                "risk_1_minus_auroc": risk,
                "entropy_mean_kept": float(np.mean(entropy[idx])),
                "entropy_mean_rejected": float(np.mean(entropy[order[n_keep:]])) if n_keep < len(order) else float("nan"),
            }
        )
    aurc = float(np.nanmean(risks)) if risks else float("nan")
    for row in rows:
        row["aurc_proxy"] = aurc
    return rows


def mean_std(values: list[float]) -> tuple[float, float]:
    arr = np.asarray([v for v in values if np.isfinite(v)], dtype=np.float64)
    if len(arr) == 0:
        return float("nan"), float("nan")
    return float(arr.mean()), float(arr.std(ddof=1)) if len(arr) > 1 else 0.0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--robustness-dir", default="outputs/robustness")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()
    coverages = [0.5, 0.7, 0.9, 1.0]

    run_dirs = [p for p in Path(args.outputs_dir).iterdir() if p.is_dir()]
    robust = Path(args.robustness_dir)
    if robust.exists():
        run_dirs.extend([p for p in robust.iterdir() if p.is_dir()])
    run_dirs = [p for p in run_dirs if "calib_subspace_head" in p.name and not p.name.startswith("ablation_")]
    if args.limit:
        run_dirs = run_dirs[: args.limit]

    rows = []
    for run_dir in run_dirs:
        rows.extend(evaluate_run(run_dir, coverages))

    groups: dict[tuple, list[dict]] = defaultdict(list)
    for row in rows:
        groups[(row["dataset"], row["variant"], row["k_shot"], row["shift"], row["coverage"])].append(row)
    summary = []
    for key, group in sorted(groups.items()):
        dataset, variant, k_shot, shift, coverage = key
        out = {
            "dataset": dataset,
            "variant": variant,
            "k_shot": k_shot,
            "shift": shift,
            "coverage": coverage,
            "n_runs": len(group),
        }
        for metric in ["auroc", "ap", "risk_1_minus_auroc", "aurc_proxy", "entropy_mean_kept", "entropy_mean_rejected"]:
            mean, std = mean_std([float(r[metric]) for r in group])
            out[f"{metric}_mean"] = mean
            out[f"{metric}_std"] = std
        summary.append(out)

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    for path, data in [
        (out_dir / "selective_risk_detailed.csv", rows),
        (out_dir / "selective_risk_summary.csv", summary),
    ]:
        if not data:
            path.write_text("", encoding="utf-8")
            continue
        with path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(data[0].keys()))
            writer.writeheader()
            writer.writerows(data)
    print(f"runs={len({r['run_id'] for r in rows})}")
    print(out_dir / "selective_risk_summary.csv")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
