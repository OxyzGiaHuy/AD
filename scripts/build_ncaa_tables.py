"""Generate NCAA-submission tables that are new relative to paper V2.

Reads committed CSVs and writes LaTeX tables into latex/tables/:
- tab_scalar_calibrators.tex: per-cell ECE of LOIO vs Platt-family and
  standard scalar calibrators with paired Wilcoxon p-values, both benchmarks.
- tab_agg_ablation.tex: AUROC sensitivity to the patch aggregation choice.
- tab_sc3r_k8.tex: SC3R k=8 source-validated thresholding per condition
  (written only if the k=8 summary CSV exists).

The three V2 tables owned by build_paper_v2_tables.py are not touched here.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "paper_tables"
OUT = ROOT / "latex" / "tables"

BASELINE_LABELS = {
    "vector_platt": "Vector Platt",
    "shift_aware_vector_platt": "Shift-Aware Platt",
    "scalar_platt": "Scalar Platt",
    "temperature": "Temperature scaling",
    "isotonic": "Isotonic regression",
    "histogram_binning": "Histogram binning",
}
CORRUPTION_LABELS = {
    "blur": "blur",
    "brightness_contrast": "bright/contr.",
    "gaussian_noise": "Gauss. noise",
    "jpeg": "JPEG",
    "clean": "clean",
}
AGG_LABELS = {
    "max": "max",
    "top_0.005": "top-0.5\\%",
    "top_0.01": "top-1\\%",
    "top_0.02": "top-2\\%",
    "top_0.05": "top-5\\%",
}


def fmt_p(p: float) -> str:
    if pd.isna(p):
        return "--"
    if p < 1e-3:
        mantissa, exponent = f"{p:.0e}".split("e")
        return f"${mantissa}{{\\times}}10^{{{int(exponent)}}}$"
    return f"{p:.2f}"


def build_scalar_calibrators() -> None:
    frames = []
    for tag, name in [("mvtec_full15", "MVTec"), ("visa_full", "VisA")]:
        df = pd.read_csv(TABLES / f"calibrator_significance_{tag}.csv")
        df["dataset_name"] = name
        frames.append(df)
    sig = pd.concat(frames, ignore_index=True)
    sig = sig[sig.corruption == "all"]

    lines = [
        "\\begin{table}[t]",
        "\\centering",
        "\\caption{LOIO conformal reliability versus Platt-family and standard scalar calibrators on the full corruption benchmarks. All calibrators are label-free and fit on the identical calibration set ($k$ support normals plus $k$ synthetic anomalies). Cells are class$\\times$seed$\\times$corruption ECE values (15 equal-width bins); $\\Delta$ is LOIO minus baseline (negative favors LOIO), $p$ is a paired two-sided Wilcoxon signed-rank test, and the last column is the fraction of cells where LOIO is better. The only comparison that is not significant is Shift-Aware Platt at VisA $k{=}8$.}",
        "\\label{tab:scalar-calibrators}",
        "\\footnotesize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\begin{tabular}{llrrrrr}",
        "\\toprule",
        "dataset / $k$ & baseline & base ECE & LOIO ECE & $\\Delta$ & Wilcoxon $p$ & LOIO better \\\\",
        "\\midrule",
    ]
    order = ["vector_platt", "shift_aware_vector_platt", "temperature", "isotonic", "histogram_binning", "scalar_platt"]
    for name in ["MVTec", "VisA"]:
        for k in [4, 8]:
            block = sig[(sig.dataset_name == name) & (sig.k_shot == k)]
            first = True
            for baseline in order:
                row = block[block.baseline == baseline]
                if row.empty:
                    continue
                r = row.iloc[0]
                base_mean = r[f"{baseline}_mean"]
                base_std = r[f"{baseline}_std"]
                loio_mean = r["conformal_prob_loio_mean"]
                loio_std = r["conformal_prob_loio_std"]
                label = f"{name} $k{{=}}{k}$" if first else ""
                first = False
                lines.append(
                    f"{label} & {BASELINE_LABELS[baseline]} & "
                    f"{base_mean:.3f}$\\pm${base_std:.3f} & {loio_mean:.3f}$\\pm${loio_std:.3f} & "
                    f"{r.delta_mean:+.3f} & {fmt_p(r.wilcoxon_p)} & {r.candidate_better_frac * 100:.0f}\\% \\\\"
                )
            lines.append("\\addlinespace[2pt]")
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    (OUT / "tab_scalar_calibrators.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_agg_ablation() -> None:
    df = pd.read_csv(TABLES / "agg_ablation_summary.csv")
    aggs = ["max", "top_0.005", "top_0.01", "top_0.02", "top_0.05"]
    lines = [
        "\\begin{table}[t]",
        "\\centering",
        "\\caption{Aggregation-sensitivity ablation: clean image AUROC (mean over representative classes, seeds 0--2) when patch residuals are pooled by max versus top-$\\rho$ mean. Bold marks the best aggregator per row; the max/top-1\\% choices used in the paper are within 0.01--0.02 AUROC of the per-row optimum.}",
        "\\label{tab:agg-ablation}",
        "\\footnotesize",
        "\\setlength{\\tabcolsep}{4pt}",
        "\\begin{tabular}{llrrrrr}",
        "\\toprule",
        "dataset & $k$ & " + " & ".join(AGG_LABELS[a] for a in aggs) + " \\\\",
        "\\midrule",
    ]
    for (dataset, k), g in df.groupby(["dataset", "k_shot"]):
        vals = {a: float(g[g.aggregator == a].auroc_mean.iloc[0]) for a in aggs}
        best = max(vals.values())
        cells = [f"\\textbf{{{v:.4f}}}" if abs(v - best) < 5e-5 else f"{v:.4f}" for v in (vals[a] for a in aggs)]
        name = "MVTec" if dataset == "mvtec" else "VisA"
        lines.append(f"{name} & {k} & " + " & ".join(cells) + " \\\\")
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    (OUT / "tab_agg_ablation.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_sc3r_k8() -> None:
    path = TABLES / "source_validated_threshold_sc3r_mvtec_full15_k8_stratified_summary.csv"
    if not path.exists():
        print("sc3r k8 summary missing; skipping tab_sc3r_k8")
        return
    s = pd.read_csv(path)
    pool = s[(s.source_mode == "matched_condition") & (s.method == "source_validated_pool")]
    anchor = s[(s.source_mode == "matched_condition") & (s.method == "target_only")]
    lines = [
        "\\begin{table}[t]",
        "\\centering",
        "\\caption{SC3R at $k{=}8$ (matched-condition source mode) versus the target-only LOIO anchor on all 15 label-stratified MVTec classes (seeds 0--2). The target-only floor is $1/9\\approx0.111$, so $\\alpha\\in\\{0.05,0.10\\}$ are below the anchor's resolution. Bold marks cells satisfying $\\mathrm{FAR}\\le\\alpha{+}0.02$ with nonzero power.}",
        "\\label{tab:sc3r-k8}",
        "\\footnotesize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\begin{tabular}{llrrrrrr}",
        "\\toprule",
        " & & \\multicolumn{3}{c}{SC3R (source-validated)} & \\multicolumn{3}{c}{Target-only anchor} \\\\",
        "\\cmidrule(lr){3-5}\\cmidrule(lr){6-8}",
        "corruption & $\\alpha$ & FAR & power & prec. & FAR & power & prec. \\\\",
        "\\midrule",
    ]
    for corruption in ["clean", "blur", "brightness_contrast", "gaussian_noise", "jpeg"]:
        first = True
        for alpha in [0.05, 0.10, 0.20]:
            p = pool[(pool.corruption == corruption) & (pool.alpha == alpha)]
            if p.empty:
                continue
            p = p.iloc[0]
            a = anchor[(anchor.corruption == corruption) & (anchor.alpha == alpha)]
            a = a.iloc[0] if len(a) else None

            def cell(far, power, prec):
                ok = far <= alpha + 0.02 and power > 0
                far_s = f"\\textbf{{{far:.3f}}}" if ok else f"{far:.3f}"
                power_s = f"\\textbf{{{power:.3f}}}" if ok else f"{power:.3f}"
                prec_s = f"{prec:.3f}" if pd.notna(prec) else "--"
                return f"{far_s} & {power_s} & {prec_s}"

            left = CORRUPTION_LABELS[corruption] if first else ""
            first = False
            pool_cells = cell(p.false_alarm_rate_mean, p.power_mean, p.alarm_precision_mean)
            if a is not None:
                anchor_cells = cell(a.false_alarm_rate_mean, a.power_mean, a.alarm_precision_mean)
            else:
                anchor_cells = "-- & -- & --"
            lines.append(f"{left} & {alpha:.2f} & {pool_cells} & {anchor_cells} \\\\")
        lines.append("\\addlinespace[2pt]")
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    (OUT / "tab_sc3r_k8.tex").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    build_scalar_calibrators()
    build_agg_ablation()
    build_sc3r_k8()
    for f in sorted(OUT.glob("tab_*.tex")):
        print(f.name)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
