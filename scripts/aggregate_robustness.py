from __future__ import annotations

import argparse
import csv
import json
import math
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev


RUN_RE = re.compile(
    r"^calib_subspace_head_mvtec_(?P<class>.+?)_k(?P<k>\d+)_seed(?P<seed>\d+)_calib_subspace_head_k\d+_seed\d+_(?P<tag>.+)$"
)


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def read_entropy_means(run_dir: Path) -> tuple[float, float, float]:
    pred_path = run_dir / "predictions.parquet"
    if not pred_path.exists():
        return math.nan, math.nan, math.nan
    try:
        import pandas as pd

        df = pd.read_parquet(pred_path, columns=["label", "entropy"])
        entropy = df["entropy"].astype(float)
        labels = df["label"].astype(int)
        normal = entropy[labels == 0]
        anomaly = entropy[labels == 1]
        return (
            float(entropy.mean()) if len(entropy) else math.nan,
            float(normal.mean()) if len(normal) else math.nan,
            float(anomaly.mean()) if len(anomaly) else math.nan,
        )
    except Exception:
        return math.nan, math.nan, math.nan


def fmt(value: float) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "nan"
    return f"{value:.4f}"


def mean_std(values: list[float]) -> tuple[float, float]:
    clean = [float(v) for v in values if v is not None and not math.isnan(float(v))]
    if not clean:
        return math.nan, math.nan
    if len(clean) == 1:
        return clean[0], 0.0
    return mean(clean), stdev(clean)


def write_csv(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict], fields: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join(["---"] * len(fields)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_runs(outputs_dir: Path, robustness_dir: Path) -> list[dict]:
    clean = {}
    for metrics_path in outputs_dir.glob("calib_subspace_head_mvtec_*_normal_synthetic/metrics.json"):
        match = RUN_RE.match(metrics_path.parent.name)
        if not match:
            continue
        key = (match.group("class"), int(match.group("k")), int(match.group("seed")))
        clean[key] = (metrics_path.parent, read_json(metrics_path))

    rows = []
    for metrics_path in robustness_dir.glob("calib_subspace_head_mvtec_*_calib_subspace_head_k*_seed*_*/metrics.json"):
        match = RUN_RE.match(metrics_path.parent.name)
        if not match:
            continue
        cls = match.group("class")
        k = int(match.group("k"))
        seed = int(match.group("seed"))
        corruption = match.group("tag")
        clean_pair = clean.get((cls, k, seed))
        if clean_pair is None:
            continue
        clean_dir, clean_metrics = clean_pair
        corrupt_metrics = read_json(metrics_path)
        clean_entropy, clean_entropy_normal, clean_entropy_anomaly = read_entropy_means(clean_dir)
        corrupt_entropy, corrupt_entropy_normal, corrupt_entropy_anomaly = read_entropy_means(metrics_path.parent)
        clean_auroc = float(clean_metrics.get("auroc", math.nan))
        corrupt_auroc = float(corrupt_metrics.get("auroc", math.nan))
        clean_ap = float(clean_metrics.get("ap", math.nan))
        corrupt_ap = float(corrupt_metrics.get("ap", math.nan))
        clean_ece = float(clean_metrics.get("ece", math.nan))
        corrupt_ece = float(corrupt_metrics.get("ece", math.nan))
        row = {
            "dataset": "mvtec",
            "model": "calib_subspace_head",
            "class": cls,
            "k_shot": k,
            "seed": seed,
            "corruption": corruption,
            "clean_auroc": clean_auroc,
            "corrupt_auroc": corrupt_auroc,
            "auroc_drop_abs": clean_auroc - corrupt_auroc,
            "auroc_drop_rel_pct": 100.0 * (clean_auroc - corrupt_auroc) / clean_auroc if clean_auroc else math.nan,
            "clean_ap": clean_ap,
            "corrupt_ap": corrupt_ap,
            "ap_drop_abs": clean_ap - corrupt_ap,
            "clean_ece": clean_ece,
            "corrupt_ece": corrupt_ece,
            "ece_delta": corrupt_ece - clean_ece,
            "clean_brier": float(clean_metrics.get("brier", math.nan)),
            "corrupt_brier": float(corrupt_metrics.get("brier", math.nan)),
            "clean_nll": float(clean_metrics.get("nll", math.nan)),
            "corrupt_nll": float(corrupt_metrics.get("nll", math.nan)),
            "clean_entropy_mean": clean_entropy,
            "corrupt_entropy_mean": corrupt_entropy,
            "entropy_shift": corrupt_entropy - clean_entropy,
            "clean_entropy_normal": clean_entropy_normal,
            "corrupt_entropy_normal": corrupt_entropy_normal,
            "clean_entropy_anomaly": clean_entropy_anomaly,
            "corrupt_entropy_anomaly": corrupt_entropy_anomaly,
        }
        rows.append(row)
    return sorted(rows, key=lambda r: (r["k_shot"], r["corruption"], r["class"], r["seed"]))


def summarize(rows: list[dict], keys: list[str]) -> list[dict]:
    groups = defaultdict(list)
    for row in rows:
        groups[tuple(row[key] for key in keys)].append(row)
    metric_names = [
        "clean_auroc",
        "corrupt_auroc",
        "auroc_drop_abs",
        "auroc_drop_rel_pct",
        "clean_ap",
        "corrupt_ap",
        "ap_drop_abs",
        "clean_ece",
        "corrupt_ece",
        "ece_delta",
        "entropy_shift",
    ]
    out = []
    for group_key, group_rows in sorted(groups.items()):
        row = {key: value for key, value in zip(keys, group_key)}
        row["n"] = len(group_rows)
        for metric in metric_names:
            m, s = mean_std([r[metric] for r in group_rows])
            row[f"{metric}_mean"] = m
            row[f"{metric}_std"] = s
        out.append(row)
    return out


def compact_summary_rows(rows: list[dict]) -> list[dict]:
    compact = []
    for row in rows:
        compact.append(
            {
                "k_shot": row["k_shot"],
                "corruption": row["corruption"],
                "n": row["n"],
                "clean_auroc": f"{fmt(row['clean_auroc_mean'])} +/- {fmt(row['clean_auroc_std'])}",
                "corrupt_auroc": f"{fmt(row['corrupt_auroc_mean'])} +/- {fmt(row['corrupt_auroc_std'])}",
                "auroc_drop_abs": f"{fmt(row['auroc_drop_abs_mean'])} +/- {fmt(row['auroc_drop_abs_std'])}",
                "auroc_drop_rel_pct": f"{fmt(row['auroc_drop_rel_pct_mean'])} +/- {fmt(row['auroc_drop_rel_pct_std'])}",
                "clean_ece": f"{fmt(row['clean_ece_mean'])} +/- {fmt(row['clean_ece_std'])}",
                "corrupt_ece": f"{fmt(row['corrupt_ece_mean'])} +/- {fmt(row['corrupt_ece_std'])}",
                "ece_delta": f"{fmt(row['ece_delta_mean'])} +/- {fmt(row['ece_delta_std'])}",
                "entropy_shift": f"{fmt(row['entropy_shift_mean'])} +/- {fmt(row['entropy_shift_std'])}",
            }
        )
    return compact


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--robustness-dir", default="outputs/robustness")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    args = parser.parse_args()

    outputs_dir = Path(args.outputs_dir)
    robustness_dir = Path(args.robustness_dir)
    out_dir = Path(args.out_dir)
    detailed = parse_runs(outputs_dir, robustness_dir)
    if not detailed:
        print("No matched robustness runs found")
        return 1
    detailed_fields = list(detailed[0].keys())
    write_csv(out_dir / "mvtec_calib_subspace_head_robustness_detailed.csv", detailed, detailed_fields)

    summary = summarize(detailed, ["k_shot", "corruption"])
    summary_fields = list(summary[0].keys())
    write_csv(out_dir / "mvtec_calib_subspace_head_robustness_summary.csv", summary, summary_fields)

    compact = compact_summary_rows(summary)
    compact_fields = list(compact[0].keys())
    write_markdown(out_dir / "mvtec_calib_subspace_head_robustness_summary.md", compact, compact_fields)
    print(f"runs={len(detailed)}")
    print(out_dir / "mvtec_calib_subspace_head_robustness_summary.csv")
    print(out_dir / "mvtec_calib_subspace_head_robustness_summary.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
