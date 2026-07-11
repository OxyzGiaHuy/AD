from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def dataframe_to_markdown(df: pd.DataFrame) -> str:
    cols = [str(c) for c in df.columns]
    lines = [
        "| " + " | ".join(cols) + " |",
        "| " + " | ".join(["---"] * len(cols)) + " |",
    ]
    for _, row in df.iterrows():
        vals = [str(row[c]) for c in df.columns]
        vals = [v.replace("\n", " ").replace("|", "/") for v in vals]
        lines.append("| " + " | ".join(vals) + " |")
    return "\n".join(lines)


def section_from_csv(title: str, path: Path, limit: int | None = None) -> str:
    if not path.exists() or path.stat().st_size == 0:
        return f"## {title}\n\nMissing: `{path}`\n"
    df = pd.read_csv(path)
    if limit is not None:
        df = df.head(limit)
    return f"## {title}\n\n" + dataframe_to_markdown(df) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tables-dir", default="outputs/paper_tables")
    parser.add_argument("--out", default="outputs/paper_tables/paper_ready_tables.md")
    args = parser.parse_args()
    root = Path(args.tables_dir)
    sections = [
        ("MVTec Clean AUROC/AP/ECE/Cost", root / "mvtec_full_clean_summary.csv", None),
        ("VisA Clean AUROC/AP/ECE", root / "visa_full_clean_summary.csv", None),
        ("Calibration Ablation", root / "calibration_ablation_summary.csv", None),
        ("Pixel Metrics", root / "pixel_metrics_summary.csv", None),
        ("MVTec To VisA Transfer", root / "mvtec_to_visa_transfer_summary.csv", None),
        ("Transfer Calibration Ablation", root / "transfer_calibration_ablation_summary.csv", None),
        ("Official SubspaceAD Representative", root / "official_subspacead_representative.csv", None),
        ("Official SubspaceAD Representative k-Trend", root / "official_subspacead_representative_k_trend.csv", None),
        ("VisA PCA128 Representative", root / "visa_pca128_representative_summary.csv", None),
        ("VisA PCA64 vs PCA128 Representative Delta", root / "visa_pca64_vs_pca128_representative_delta.csv", None),
        ("VisA PCA128 Full", root / "visa_pca128_full_visa_summary.csv", None),
        ("VisA PCA64 vs PCA128 Full Delta", root / "visa_pca64_vs_pca128_full_visa_delta.csv", None),
        ("Shift-Aware Calibration Representative", root / "shift_aware_calibration_representative_summary.csv", None),
        ("Shift-Aware Calibration Full VisA", root / "shift_aware_calibration_full_visa_summary.csv", None),
        ("Shift-Aware Calibration Full VisA Delta", root / "shift_aware_calibration_full_visa_delta.csv", None),
        ("Shift-Aware Corruption Calibration VisA k4/k8", root / "shift_aware_corruption_calibration_visa_k4k8_full_corruptions_summary.csv", None),
        ("Shift-Aware Corruption Calibration VisA k4/k8 Delta", root / "shift_aware_corruption_calibration_visa_k4k8_full_corruptions_delta.csv", None),
        ("No-Cache Runtime Representative", root / "runtime_no_cache_representative_summary.csv", None),
        ("Claim-Relevant Ablation Findings", root / "parallel_findings_for_claims.csv", None),
        ("MVTec Robustness", root / "mvtec_robustness_all_summary.csv", 40),
        ("VisA Robustness", root / "visa_robustness_all_summary.csv", 40),
        ("MVTec FGSM Sweep", root / "mvtec_fgsm_sweep_summary.csv", None),
        ("Selective Risk", root / "selective_risk_summary.csv", 60),
        ("Runtime Audit", root / "runtime_audit_summary.csv", 40),
    ]
    body = [
        "# Paper-Ready Benchmark Tables",
        "",
        "Generated from current CSV artifacts. Use these tables as a drafting bundle; final paper tables should still be manually pruned for readability.",
        "",
    ]
    for title, path, limit in sections:
        body.append(section_from_csv(title, path, limit))
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(body), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
