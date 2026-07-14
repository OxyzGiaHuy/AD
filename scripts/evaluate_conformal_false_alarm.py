from __future__ import annotations

import argparse
import csv
from collections import defaultdict
from pathlib import Path
from typing import Iterable

import numpy as np


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


def label_array(rows: list[dict]) -> np.ndarray:
    return np.asarray([int(r["label"]) for r in rows], dtype=np.int64)


def pvalue_array(rows: list[dict], pvalue_col: str, prob_col: str | None) -> np.ndarray:
    if pvalue_col in rows[0]:
        p = np.asarray([fl(r.get(pvalue_col)) for r in rows], dtype=np.float64)
    elif prob_col and prob_col in rows[0]:
        p = 1.0 - np.asarray([fl(r.get(prob_col)) for r in rows], dtype=np.float64)
    else:
        raise KeyError(f"Missing p-value column {pvalue_col!r} and probability fallback {prob_col!r}")
    return np.clip(p, 0.0, 1.0)


def group_key(row: dict, group: str) -> tuple[str, str, str]:
    if group == "all":
        return ("all", "all", "all")
    if group == "k":
        return (row.get("k_shot", "all"), "all", "all")
    if group == "corruption":
        return (row.get("corruption", "clean"), "all", "all")
    if group == "k_corruption":
        return (row.get("k_shot", "all"), row.get("corruption", "clean"), "all")
    if group == "class":
        return (row.get("class", "unknown"), "all", "all")
    if group == "class_k":
        return (row.get("class", "unknown"), row.get("k_shot", "all"), "all")
    if group == "class_k_corruption":
        return (row.get("class", "unknown"), row.get("k_shot", "all"), row.get("corruption", "clean"))
    raise ValueError(group)


def summarize(rows: list[dict], alpha: float, pvalue_col: str, prob_col: str | None, group_type: str, key: tuple[str, str, str]) -> dict:
    y = label_array(rows)
    p = pvalue_array(rows, pvalue_col, prob_col)
    # float32-stored p-values can exceed their exact rational value (e.g. 1/5 -> 0.20000000298),
    # so an exact p <= alpha comparison silently drops alarms at attainable alphas
    alarm = p <= alpha + 1e-6
    normal = y == 0
    anomaly = y == 1
    n_normal = int(normal.sum())
    n_anomaly = int(anomaly.sum())
    false_alarm = int(np.logical_and(alarm, normal).sum())
    detected = int(np.logical_and(alarm, anomaly).sum())
    false_alarm_rate = false_alarm / n_normal if n_normal else float("nan")
    detection_rate = detected / n_anomaly if n_anomaly else float("nan")
    precision = detected / int(alarm.sum()) if int(alarm.sum()) else float("nan")
    return {
        "group_type": group_type,
        "key0": key[0],
        "key1": key[1],
        "key2": key[2],
        "pvalue_col": pvalue_col,
        "alpha": alpha,
        "n_images": len(rows),
        "n_normal": n_normal,
        "n_anomaly": n_anomaly,
        "n_alarm": int(alarm.sum()),
        "false_alarms": false_alarm,
        "detected_anomalies": detected,
        "false_alarm_rate": false_alarm_rate,
        "nominal_alpha": alpha,
        "coverage_gap": false_alarm_rate - alpha if np.isfinite(false_alarm_rate) else float("nan"),
        "abs_coverage_gap": abs(false_alarm_rate - alpha) if np.isfinite(false_alarm_rate) else float("nan"),
        "anomaly_detection_rate": detection_rate,
        "alarm_precision": precision,
        "normal_mean_pvalue": float(np.mean(p[normal])) if n_normal else float("nan"),
        "anomaly_mean_pvalue": float(np.mean(p[anomaly])) if n_anomaly else float("nan"),
        "pvalue_separation_normal_minus_anomaly": float(np.mean(p[normal]) - np.mean(p[anomaly])) if n_normal and n_anomaly else float("nan"),
    }


def make_summary(rows: list[dict], alphas: Iterable[float], pvalue_cols: list[tuple[str, str | None]], groups: list[str]) -> list[dict]:
    out: list[dict] = []
    for group in groups:
        buckets: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
        for row in rows:
            buckets[group_key(row, group)].append(row)
        for key, gr in sorted(buckets.items()):
            for pvalue_col, prob_col in pvalue_cols:
                if pvalue_col not in gr[0] and (not prob_col or prob_col not in gr[0]):
                    continue
                for alpha in alphas:
                    out.append(summarize(gr, alpha, pvalue_col, prob_col, group, key))
    return out


def make_histogram(rows: list[dict], pvalue_cols: list[tuple[str, str | None]], bins: int) -> list[dict]:
    edges = np.linspace(0.0, 1.0, bins + 1)
    y = label_array(rows)
    out: list[dict] = []
    for pvalue_col, prob_col in pvalue_cols:
        if pvalue_col not in rows[0] and (not prob_col or prob_col not in rows[0]):
            continue
        p = pvalue_array(rows, pvalue_col, prob_col)
        for label_name, mask in [("normal", y == 0), ("anomaly", y == 1), ("all", np.ones_like(y, dtype=bool))]:
            vals = p[mask]
            for idx, (lo, hi) in enumerate(zip(edges[:-1], edges[1:])):
                bin_mask = (vals >= lo) & (vals < hi if hi < 1.0 else vals <= hi)
                out.append({
                    "pvalue_col": pvalue_col,
                    "label_group": label_name,
                    "bin": idx,
                    "lo": lo,
                    "hi": hi,
                    "n": int(bin_mask.sum()),
                    "fraction": float(bin_mask.mean()) if len(vals) else float("nan"),
                })
    return out


def markdown(rows: list[dict], pvalue_col: str) -> str:
    keep = [r for r in rows if r["group_type"] == "k_corruption" and r["pvalue_col"] == pvalue_col]
    lines = [
        "# Conformal False-Alarm Control Summary",
        "",
        "Alarm rule: raise an anomaly alarm when conformal p-value <= alpha.",
        "",
        "| k | corruption | alpha | false alarm | detection | gap | precision |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for r in keep:
        lines.append(
            f"| {r['key0']} | {r['key1']} | {float(r['alpha']):.2f} | "
            f"{float(r['false_alarm_rate']):.4f} | {float(r['anomaly_detection_rate']):.4f} | "
            f"{float(r['coverage_gap']):+.4f} | {float(r['alarm_precision']):.4f} |"
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--dataset", default="")
    parser.add_argument("--alphas", nargs="*", type=float, default=[0.01, 0.05, 0.10, 0.20])
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--run-tag", default="full")
    parser.add_argument("--bins", type=int, default=20)
    args = parser.parse_args()

    rows = [r for r in read_csv(Path(args.input)) if r.get("label") in {"0", "1"}]
    if args.dataset:
        rows = [r for r in rows if r.get("dataset", args.dataset) == args.dataset]
    if not rows:
        raise SystemExit("No valid rows found")

    pvalue_cols = [("image_p_loio", "conformal_prob_loio"), ("image_p_weighted", "conformal_prob_weighted")]
    groups = ["all", "k", "corruption", "k_corruption", "class", "class_k", "class_k_corruption"]
    summary = make_summary(rows, args.alphas, pvalue_cols, groups)
    hist = make_histogram(rows, pvalue_cols, args.bins)

    out_dir = Path(args.out_dir)
    prefix = f"{args.run_tag}_conformal_false_alarm"
    write_csv(out_dir / f"{prefix}_summary.csv", summary)
    write_csv(out_dir / f"{prefix}_pvalue_histogram.csv", hist)
    (out_dir / f"{prefix}_summary.md").write_text(markdown(summary, "image_p_loio"), encoding="utf-8")
    print(f"wrote {len(summary)} summary rows and {len(hist)} histogram rows for {len(rows)} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
