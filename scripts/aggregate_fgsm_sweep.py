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
EPS_RE = re.compile(r"^fgsm_eps(?P<num>\d+)_(?P<den>\d+)$")


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def mean_std(values: list[float]) -> tuple[float, float]:
    clean = [float(v) for v in values if v is not None and not math.isnan(float(v))]
    if not clean:
        return math.nan, math.nan
    if len(clean) == 1:
        return clean[0], 0.0
    return mean(clean), stdev(clean)


def write_csv(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def fmt(value: float) -> str:
    if value is None or (isinstance(value, float) and math.isnan(value)):
        return "nan"
    return f"{value:.4f}"


def write_markdown(path: Path, rows: list[dict]) -> None:
    fields = [
        "epsilon",
        "k_shot",
        "n",
        "clean_auroc",
        "fgsm_auroc",
        "auroc_drop_abs",
        "auroc_drop_rel_pct",
        "clean_ece",
        "fgsm_ece",
        "ece_delta",
    ]
    lines = ["| " + " | ".join(fields) + " |", "| " + " | ".join(["---"] * len(fields)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(str(row.get(field, "")) for field in fields) + " |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def detailed_rows(outputs_dir: Path, robustness_dir: Path) -> list[dict]:
    clean = {}
    for metrics_path in outputs_dir.glob("calib_subspace_head_mvtec_*_normal_synthetic/metrics.json"):
        match = RUN_RE.match(metrics_path.parent.name)
        if not match:
            continue
        clean[(match.group("class"), int(match.group("k")), int(match.group("seed")))] = read_json(metrics_path)

    rows = []
    for metrics_path in robustness_dir.glob("calib_subspace_head_mvtec_*_fgsm_eps*_*/metrics.json"):
        match = RUN_RE.match(metrics_path.parent.name)
        if not match:
            continue
        eps_match = EPS_RE.match(match.group("tag"))
        if not eps_match:
            continue
        cls = match.group("class")
        k = int(match.group("k"))
        seed = int(match.group("seed"))
        clean_metrics = clean.get((cls, k, seed))
        if clean_metrics is None:
            continue
        attack_metrics = read_json(metrics_path)
        clean_auroc = float(clean_metrics.get("auroc", math.nan))
        attack_auroc = float(attack_metrics.get("auroc", math.nan))
        clean_ap = float(clean_metrics.get("ap", math.nan))
        attack_ap = float(attack_metrics.get("ap", math.nan))
        clean_ece = float(clean_metrics.get("ece", math.nan))
        attack_ece = float(attack_metrics.get("ece", math.nan))
        epsilon = f"{eps_match.group('num')}/{eps_match.group('den')}"
        rows.append(
            {
                "dataset": "mvtec",
                "variant": "calib_subspace_head",
                "class": cls,
                "k_shot": k,
                "seed": seed,
                "attack": "fgsm_image_pca_surrogate",
                "epsilon": epsilon,
                "epsilon_value": int(eps_match.group("num")) / int(eps_match.group("den")),
                "num_images": attack_metrics.get("num_images"),
                "clean_auroc": clean_auroc,
                "fgsm_auroc": attack_auroc,
                "auroc_drop_abs": clean_auroc - attack_auroc,
                "auroc_drop_rel_pct": 100.0 * (clean_auroc - attack_auroc) / clean_auroc if clean_auroc else math.nan,
                "clean_ap": clean_ap,
                "fgsm_ap": attack_ap,
                "ap_drop_abs": clean_ap - attack_ap,
                "clean_ece": clean_ece,
                "fgsm_ece": attack_ece,
                "ece_delta": attack_ece - clean_ece,
                "clean_brier": float(clean_metrics.get("brier", math.nan)),
                "fgsm_brier": float(attack_metrics.get("brier", math.nan)),
                "clean_nll": float(clean_metrics.get("nll", math.nan)),
                "fgsm_nll": float(attack_metrics.get("nll", math.nan)),
            }
        )
    return sorted(rows, key=lambda r: (r["epsilon_value"], r["k_shot"], r["class"], r["seed"]))


def summarize(rows: list[dict]) -> list[dict]:
    grouped = defaultdict(list)
    for row in rows:
        grouped[(row["epsilon_value"], row["epsilon"], row["k_shot"])].append(row)
    out = []
    for (_, epsilon, k), group_rows in sorted(grouped.items()):
        row = {"epsilon": epsilon, "k_shot": k, "n": len(group_rows)}
        for metric in [
            "clean_auroc",
            "fgsm_auroc",
            "auroc_drop_abs",
            "auroc_drop_rel_pct",
            "clean_ap",
            "fgsm_ap",
            "ap_drop_abs",
            "clean_ece",
            "fgsm_ece",
            "ece_delta",
        ]:
            m, s = mean_std([r[metric] for r in group_rows])
            row[f"{metric}_mean"] = m
            row[f"{metric}_std"] = s
        out.append(row)
    return out


def compact(rows: list[dict]) -> list[dict]:
    out = []
    for row in rows:
        out.append(
            {
                "epsilon": row["epsilon"],
                "k_shot": row["k_shot"],
                "n": row["n"],
                "clean_auroc": f"{fmt(row['clean_auroc_mean'])} +/- {fmt(row['clean_auroc_std'])}",
                "fgsm_auroc": f"{fmt(row['fgsm_auroc_mean'])} +/- {fmt(row['fgsm_auroc_std'])}",
                "auroc_drop_abs": f"{fmt(row['auroc_drop_abs_mean'])} +/- {fmt(row['auroc_drop_abs_std'])}",
                "auroc_drop_rel_pct": f"{fmt(row['auroc_drop_rel_pct_mean'])} +/- {fmt(row['auroc_drop_rel_pct_std'])}",
                "clean_ece": f"{fmt(row['clean_ece_mean'])} +/- {fmt(row['clean_ece_std'])}",
                "fgsm_ece": f"{fmt(row['fgsm_ece_mean'])} +/- {fmt(row['fgsm_ece_std'])}",
                "ece_delta": f"{fmt(row['ece_delta_mean'])} +/- {fmt(row['ece_delta_std'])}",
            }
        )
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--outputs-dir", default="outputs")
    parser.add_argument("--robustness-dir", default="outputs/robustness")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    args = parser.parse_args()

    rows = detailed_rows(Path(args.outputs_dir), Path(args.robustness_dir))
    if not rows:
        print("No FGSM sweep runs found")
        return 1
    out_dir = Path(args.out_dir)
    summary = summarize(rows)
    write_csv(out_dir / "mvtec_fgsm_sweep_detailed.csv", rows)
    write_csv(out_dir / "mvtec_fgsm_sweep_summary.csv", summary)
    write_markdown(out_dir / "mvtec_fgsm_sweep_summary.md", compact(summary))
    print(f"runs={len(rows)}")
    print(out_dir / "mvtec_fgsm_sweep_summary.csv")
    print(out_dir / "mvtec_fgsm_sweep_summary.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
