from __future__ import annotations

import argparse
import csv
import json
import math
import re
from collections import defaultdict
from pathlib import Path
from statistics import mean, stdev


ALPHA_RE = re.compile(
    r"^ablation_alpha_(?P<value>.+?)_mvtec_(?P<class>.+?)_k(?P<k>\d+)_seed(?P<seed>\d+)_head_pca_k\d+_seed\d+_(?P<calibration_mode>.+)$"
)
PCA_RE = re.compile(
    r"^ablation_pca(?P<value>\d+)_mvtec_(?P<class>.+?)_k(?P<k>\d+)_seed(?P<seed>\d+)_calib_subspace_head_k\d+_seed\d+_(?P<calibration_mode>.+)$"
)
CALIB_RE = re.compile(
    r"^ablation_calib_upper_mvtec_(?P<class>.+?)_k(?P<k>\d+)_seed(?P<seed>\d+)_calib_subspace_head_k\d+_seed\d+_(?P<calibration_mode>.+)$"
)

METRICS = [
    "auroc",
    "ap",
    "max_f1",
    "ece",
    "brier",
    "nll",
    "latency_sec_per_image",
    "model_storage_mb",
    "calibration_anomaly_val_count",
]


def parse_run_id(run_id: str) -> dict | None:
    match = ALPHA_RE.match(run_id)
    if match:
        value = match.group("value").replace("p", ".")
        return {
            "ablation": "alpha_decoupling",
            "value": value,
            "variant": "head_pca",
            "class": match.group("class"),
            "k_shot": int(match.group("k")),
            "seed": int(match.group("seed")),
            "calibration_mode": match.group("calibration_mode"),
        }
    match = PCA_RE.match(run_id)
    if match:
        return {
            "ablation": "pca_components",
            "value": match.group("value"),
            "variant": "calib_subspace_head",
            "class": match.group("class"),
            "k_shot": int(match.group("k")),
            "seed": int(match.group("seed")),
            "calibration_mode": match.group("calibration_mode"),
        }
    match = CALIB_RE.match(run_id)
    if match:
        return {
            "ablation": "calibration_mode",
            "value": "normal_plus_anomaly_val",
            "variant": "calib_subspace_head",
            "class": match.group("class"),
            "k_shot": int(match.group("k")),
            "seed": int(match.group("seed")),
            "calibration_mode": match.group("calibration_mode"),
        }
    return None


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def mean_std(values: list[float]) -> tuple[float, float]:
    clean = [float(v) for v in values if v is not None and not math.isnan(float(v))]
    if not clean:
        return math.nan, math.nan
    if len(clean) == 1:
        return clean[0], 0.0
    return mean(clean), stdev(clean)


def fmt_pair(mean_value: float, std_value: float) -> str:
    if math.isnan(mean_value):
        return ""
    return f"{mean_value:.4f}+-{std_value:.4f}"


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def write_markdown(path: Path, rows: list[dict]) -> None:
    fields = ["ablation", "value", "variant", "k_shot", "n", "auroc", "ap", "ece", "brier", "nll"]
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join(["---"] * len(fields)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def detailed_rows(outputs_dir: Path) -> list[dict]:
    rows = []
    for metrics_path in sorted(outputs_dir.glob("ablation_*/metrics.json")):
        info = parse_run_id(metrics_path.parent.name)
        if info is None:
            continue
        data = read_json(metrics_path)
        row = {"dataset": "mvtec", **info, "run_id": metrics_path.parent.name}
        for metric in METRICS:
            value = data.get(metric)
            row[metric] = float(value) if isinstance(value, (int, float)) else math.nan
        rows.append(row)
    return rows


def summarize(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    grouped = defaultdict(list)
    for row in rows:
        key = (row["ablation"], row["value"], row["variant"], row["k_shot"], row["calibration_mode"])
        grouped[key].append(row)

    numeric_rows = []
    compact_rows = []
    for (ablation, value, variant, k_shot, calibration_mode), group_rows in sorted(grouped.items()):
        base = {
            "dataset": "mvtec",
            "ablation": ablation,
            "value": value,
            "variant": variant,
            "k_shot": k_shot,
            "calibration_mode": calibration_mode,
            "n": len(group_rows),
        }
        numeric = dict(base)
        compact = dict(base)
        for metric in METRICS:
            m, s = mean_std([row[metric] for row in group_rows])
            numeric[f"{metric}_mean"] = m
            numeric[f"{metric}_std"] = s
            compact[metric] = fmt_pair(m, s)
        numeric_rows.append(numeric)
        compact_rows.append(compact)
    return numeric_rows, compact_rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    args = parser.parse_args()

    rows = detailed_rows(Path(args.outputs_dir))
    if not rows:
        print("No ablation runs found")
        return 1

    out_dir = Path(args.out_dir)
    summary, compact = summarize(rows)
    write_csv(out_dir / "mvtec_ablation_detailed.csv", rows)
    write_csv(out_dir / "mvtec_ablation_summary.csv", summary)
    write_csv(out_dir / "mvtec_ablation_summary_compact.csv", compact)
    write_markdown(out_dir / "mvtec_ablation_summary.md", compact)
    print(f"runs={len(rows)}")
    print(out_dir / "mvtec_ablation_summary.csv")
    print(out_dir / "mvtec_ablation_summary.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
