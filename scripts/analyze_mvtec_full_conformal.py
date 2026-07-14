from __future__ import annotations

import argparse
from collections import defaultdict
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.analyze_visa_full_conformal import (
    fl,
    group_key,
    markdown_table,
    metrics,
    read_csv,
    reliability_bins,
    selective_rows,
    write_csv,
)


def baseline_rows(delta_path: Path) -> list[dict]:
    if not delta_path.exists():
        return []
    out = []
    seen = set()
    for r in read_csv(delta_path):
        entries = [(r.get("method", "gated"), "method")]
        vector_key = (r["k_shot"], r["corruption"], "vector_platt")
        if vector_key not in seen:
            seen.add(vector_key)
            entries.append(("vector_platt", "vector"))
        for prob_col, prefix in entries:
            out.append({
                "group_type": "k_corruption",
                "key0": r["k_shot"],
                "key1": r["corruption"],
                "key2": "all",
                "prob_col": prob_col,
                "n_images": int(float(r["n"])),
                "auroc": fl(r.get(f"{prefix}_auroc")),
                "ap": fl(r.get(f"{prefix}_ap")),
                "ece": fl(r.get(f"{prefix}_ece")),
                "brier": fl(r.get(f"{prefix}_brier")),
                "nll": fl(r.get(f"{prefix}_nll")),
                "normal_mean_prob": float("nan"),
                "anomaly_mean_prob": float("nan"),
                "separation": float("nan"),
            })
    return out


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="outputs/paper_tables/sw_cad_image_views_mvtec_full15_k4k8_s0s2.csv")
    parser.add_argument("--baseline-delta", default="outputs/paper_tables/gated_shift_aware_anchored_adaptive_mvtec_full_k4k8_s0s2_delta.csv")
    parser.add_argument("--out-dir", default="outputs/paper_tables")
    parser.add_argument("--prefix", default="mvtec_full15")
    args = parser.parse_args()
    rows = [r for r in read_csv(Path(args.input)) if r.get("label") in {"0", "1"}]
    if not rows:
        raise SystemExit("No valid rows found")
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
    write_csv(out_dir / f"{args.prefix}_conformal_extended_summary.csv", summary)
    write_csv(out_dir / f"{args.prefix}_conformal_vs_baselines_k_corruption.csv", baseline + [r for r in summary if r["group_type"] == "k_corruption"])

    bins = []
    for prob_col in prob_cols:
        bins.extend(reliability_bins(rows, prob_col))
        for k in ["4", "8"]:
            bins.extend([{**b, "k_shot": k} for b in reliability_bins([r for r in rows if r["k_shot"] == k], prob_col)])
    write_csv(out_dir / f"{args.prefix}_conformal_reliability_bins.csv", bins)

    selective = []
    for prob_col in prob_cols:
        selective.extend(selective_rows(rows, prob_col, "all"))
        for k in ["4", "8"]:
            selective.extend(selective_rows([r for r in rows if r["k_shot"] == k], prob_col, f"k={k}"))
    write_csv(out_dir / f"{args.prefix}_conformal_selective_reliability.csv", selective)

    main_rows = [r for r in summary if r["group_type"] in {"all", "k"}]
    main_rows = sorted(main_rows, key=lambda r: (r["group_type"], r["key0"], r["prob_col"]))
    kc_rows = [r for r in summary if r["group_type"] == "k_corruption" and r["prob_col"] == "conformal_prob_loio"]
    kc_rows = sorted(kc_rows, key=lambda r: (r["key0"], r["key1"]))
    class_rows = [r for r in summary if r["group_type"] == "class_k" and r["prob_col"] == "conformal_prob_loio"]
    class_rows = sorted(class_rows, key=lambda r: float(r["ece"]), reverse=True)
    md = [
        "# Full MVTec Conformal Reliability Tables",
        "",
        f"Source: `{Path(args.input).name}` ({len(rows)} images).",
        "",
        markdown_table(main_rows, "Main Full MVTec Metrics", ["group_type", "key0", "prob_col", "n_images", "auroc", "ap", "ece", "brier", "nll", "normal_mean_prob", "anomaly_mean_prob", "separation"]),
        "",
        markdown_table(kc_rows, "LOIO By k And Corruption", ["key0", "key1", "n_images", "auroc", "ap", "ece", "brier", "nll", "normal_mean_prob", "anomaly_mean_prob", "separation"]),
        "",
        markdown_table(class_rows[:20], "Worst Class-k ECE Cases For LOIO", ["key0", "key1", "n_images", "auroc", "ap", "ece", "brier", "nll", "normal_mean_prob", "anomaly_mean_prob", "separation"]),
    ]
    (out_dir / f"{args.prefix}_conformal_main_table.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"wrote {args.prefix} conformal analysis artifacts for {len(rows)} images")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
