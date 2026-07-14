"""Build paper V2 LaTeX tables from analysis CSVs.

Regenerates:
- paper/tables/tab_sc3r_source_validated.tex
- paper/tables/tab_attainable_alpha.tex
- paper/tables/tab_false_alarm_control.tex
"""
from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

CORRUPTION_LABELS = {
    "clean": "clean",
    "blur": "blur",
    "brightness_contrast": "bright/contr.",
    "gaussian_noise": "Gauss. noise",
    "jpeg": "JPEG",
}


def fmt(value: float, digits: int = 3, bold: bool = False) -> str:
    if not np.isfinite(value):
        return "--"
    text = f"{value:.{digits}f}"
    return f"\\textbf{{{text}}}" if bold else text


def sc3r_table(detailed_path: Path, out_path: Path) -> None:
    d = pd.read_csv(detailed_path)
    d = d[d.source_mode == "matched_condition"]
    lines = [
        "\\begin{table}[t]",
        "\\centering",
        "\\caption{Source-validated thresholding (SC3R, matched-condition source mode) versus the target-only LOIO anchor on all 15 label-stratified MVTec classes ($k{=}4$, seeds 0--2). Below the target-only attainable-alpha floor $1/(k{+}1){=}0.2$, the anchor cannot raise alarms; source pooling unlocks these operating points with controlled false alarms. Bold marks cells satisfying $\\mathrm{FAR}\\le\\alpha{+}0.02$ with nonzero power.}",
        "\\label{tab:sc3r-source-validated}",
        "\\footnotesize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\begin{tabular}{llrrrrrr}",
        "\\toprule",
        " & & \\multicolumn{3}{c}{SC3R (source-validated)} & \\multicolumn{3}{c}{Target-only anchor} \\\\",
        "\\cmidrule(lr){3-5}\\cmidrule(lr){6-8}",
        "corruption & $\\alpha$ & FAR & power & prec. & FAR & power & prec. \\\\",
        "\\midrule",
    ]
    order = ["clean", "blur", "brightness_contrast", "gaussian_noise", "jpeg"]
    for corruption in order:
        for alpha in [0.05, 0.10, 0.20]:
            cell = d[(d.corruption == corruption) & (d.alpha == alpha)]
            sc = cell[cell.method == "source_validated_pool"]
            to = cell[cell.method == "target_only"]
            far, power, prec = sc.false_alarm_rate.mean(), sc.power.mean(), sc.alarm_precision.mean()
            tfar, tpower, tprec = to.false_alarm_rate.mean(), to.power.mean(), to.alarm_precision.mean()
            ok = far <= alpha + 0.02 and power > 0
            label = CORRUPTION_LABELS[corruption] if alpha == 0.05 else ""
            lines.append(
                f"{label} & {alpha:.2f} & {fmt(far, bold=ok)} & {fmt(power, bold=ok)} & {fmt(prec)} & "
                f"{fmt(tfar)} & {fmt(tpower)} & {fmt(tprec)} \\\\"
            )
        if corruption != order[-1]:
            lines.append("\\addlinespace[2pt]")
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def attainable_alpha_table(summary_paths: dict[str, Path], out_path: Path) -> None:
    lines = [
        "\\begin{table}[t]",
        "\\centering",
        "\\caption{Attainable-alpha structure of few-shot LOIO conformal p-values. With $k$ support scores the smallest attainable p-value is $1/(k{+}1)$, so nominal levels below this floor structurally raise no alarms; empirical false-alarm rates (FAR, mean over classes/seeds/corruptions) then sit at the nearest attainable grid point rather than at the nominal level.}",
        "\\label{tab:attainable-alpha}",
        "\\footnotesize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\begin{tabular}{llrrrrr}",
        "\\toprule",
        "dataset & $k$ & nominal $\\alpha$ & floor & attainable & FAR & detection \\\\",
        "\\midrule",
    ]
    for name, path in summary_paths.items():
        s = pd.read_csv(path)
        agg = s.groupby(["k_shot", "nominal_alpha", "alpha_floor", "nearest_attainable_alpha"])[
            ["false_alarm_rate_mean", "detection_rate_mean"]
        ].mean().reset_index()
        first = True
        for _, r in agg.sort_values(["k_shot", "nominal_alpha"]).iterrows():
            label = name if first else ""
            first = False
            lines.append(
                f"{label} & {int(r.k_shot)} & {r.nominal_alpha:.2f} & {r.alpha_floor:.3f} & "
                f"{r.nearest_attainable_alpha:.3f} & {fmt(r.false_alarm_rate_mean)} & {fmt(r.detection_rate_mean)} \\\\"
            )
        lines.append("\\addlinespace[2pt]")
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def false_alarm_table(summary_paths: dict[str, Path], out_path: Path) -> None:
    lines = [
        "\\begin{table}[t]",
        "\\centering",
        "\\caption{Operational false-alarm behavior of target-only LOIO conformal p-values at the first attainable operating point ($\\alpha{=}0.20$; alarms fire at $p\\le\\alpha$ with a float tolerance). Rates are pooled over classes and seeds. On VisA the rule is conservative (FAR below nominal); on full MVTec it is anti-conservative under corruption, especially at $k{=}4$, motivating source-validated thresholding (Table~\\ref{tab:sc3r-source-validated}).}",
        "\\label{tab:false-alarm-control}",
        "\\footnotesize",
        "\\setlength{\\tabcolsep}{3pt}",
        "\\begin{tabular}{llrrrr}",
        "\\toprule",
        "dataset & corruption & $k$ & FAR & detection & precision \\\\",
        "\\midrule",
    ]
    for name, path in summary_paths.items():
        s = pd.read_csv(path)
        s = s[(s.group_type == "k_corruption") & (s.pvalue_col == "image_p_loio") & (s.alpha == 0.20)]
        first = True
        for corruption in ["blur", "brightness_contrast", "gaussian_noise", "jpeg"]:
            for k in ["4", "8"]:
                r = s[(s.key0.astype(str) == k) & (s.key1 == corruption)]
                if r.empty:
                    continue
                r = r.iloc[0]
                label = name if first else ""
                first = False
                lines.append(
                    f"{label} & {CORRUPTION_LABELS[corruption]} & {k} & {fmt(float(r.false_alarm_rate))} & "
                    f"{fmt(float(r.anomaly_detection_rate))} & {fmt(float(r.alarm_precision))} \\\\"
                )
        lines.append("\\addlinespace[2pt]")
    lines += ["\\bottomrule", "\\end{tabular}", "\\end{table}"]
    out_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tables-dir", default="outputs/paper_tables")
    parser.add_argument("--out-dir", default="paper/tables")
    parser.add_argument("--mvtec-full-tag", default=None, help="If set (e.g. mvtec_full15), include full-MVTec rows.")
    parser.add_argument("--sc3r-detailed", default="source_validated_threshold_sc3r_mvtec_repr_stratified_detailed.csv", help="Detailed SC3R CSV (relative to --tables-dir) for the SC3R table.")
    args = parser.parse_args()
    tables = Path(args.tables_dir)
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)

    sc3r_table(tables / args.sc3r_detailed, out / "tab_sc3r_source_validated.tex")
    attainable = {"VisA (full)": tables / "attainable_alpha_visa_full_summary.csv"}
    false_alarm = {"VisA (full)": tables / "visa_full_conformal_false_alarm_summary.csv"}
    if args.mvtec_full_tag:
        attainable["MVTec (full)"] = tables / f"attainable_alpha_{args.mvtec_full_tag}_summary.csv"
        false_alarm["MVTec (full)"] = tables / f"{args.mvtec_full_tag}_conformal_false_alarm_summary.csv"
    else:
        attainable["MVTec (repr.)"] = tables / "attainable_alpha_mvtec_representative_summary.csv"
        false_alarm["MVTec (repr.)"] = tables / "mvtec_representative_conformal_false_alarm_summary.csv"
    attainable_alpha_table(attainable, out / "tab_attainable_alpha.tex")
    false_alarm_table(false_alarm, out / "tab_false_alarm_control.tex")
    print("wrote paper V2 tables")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
