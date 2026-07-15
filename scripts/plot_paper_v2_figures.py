"""Vector figures for the NCAA submission, generated from committed CSVs.

Outputs (into latex/figures/):
- fig_uniformity_cdf.pdf: discrete Q-Q (empirical vs nominal CDF at the p-value
  grid) per dataset/k, one series per corruption.
- fig_risk_coverage.pdf: selective-risk curves (ECE vs coverage, entropy
  abstention) for LOIO conformal on both full benchmarks.
- fig_reliability.pdf: pooled reliability diagrams for LOIO conformal by k.
- fig_ece_by_corruption.pdf: ECE by corruption and reliability view (k=4/8,
  both datasets).

Style: Okabe-Ito colorblind-safe palette, direct axis labels, thin marks,
fonts sized for single-column print.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "outputs" / "paper_tables"
OUT = ROOT / "latex" / "figures"

OKABE_ITO = {
    "blue": "#0072B2",
    "vermillion": "#D55E00",
    "green": "#009E73",
    "orange": "#E69F00",
    "purple": "#CC79A7",
    "skyblue": "#56B4E9",
    "black": "#000000",
}
CORRUPTION_COLORS = {
    "blur": OKABE_ITO["blue"],
    "brightness_contrast": OKABE_ITO["orange"],
    "gaussian_noise": OKABE_ITO["vermillion"],
    "jpeg": OKABE_ITO["green"],
    "clean": OKABE_ITO["black"],
}
CORRUPTION_LABELS = {
    "blur": "blur",
    "brightness_contrast": "bright/contr.",
    "gaussian_noise": "Gauss. noise",
    "jpeg": "JPEG",
    "clean": "clean",
}
METHOD_COLORS = {
    "vector_platt": OKABE_ITO["blue"],
    "shift_aware_vector_platt": OKABE_ITO["skyblue"],
    "conformal_prob_loio": OKABE_ITO["vermillion"],
    "conformal_prob_weighted": OKABE_ITO["orange"],
}
METHOD_LABELS = {
    "vector_platt": "Vector Platt",
    "shift_aware_vector_platt": "Shift-Aware Platt",
    "conformal_prob_loio": "LOIO conformal",
    "conformal_prob_weighted": "Weighted conformal",
}

plt.rcParams.update({
    "font.size": 8,
    "axes.titlesize": 8,
    "axes.labelsize": 8,
    "legend.fontsize": 7,
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
    "axes.linewidth": 0.6,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "grid.linewidth": 0.4,
    "grid.alpha": 0.35,
    "lines.linewidth": 1.4,
    "pdf.fonttype": 42,
})


def fig_uniformity_cdf() -> None:
    frames = []
    for tag, name in [("visa_full", "VisA"), ("mvtec_full15", "MVTec")]:
        df = pd.read_csv(TABLES / f"pvalue_uniformity_{tag}_qq.csv")
        df["dataset_name"] = name
        frames.append(df)
    qq = pd.concat(frames, ignore_index=True)
    qq = qq[qq.pvalue_col == "image_p_loio"]

    fig, axes = plt.subplots(2, 2, figsize=(5.6, 5.2), sharex=True, sharey=True, constrained_layout=True)
    panels = [("VisA", 4), ("VisA", 8), ("MVTec", 4), ("MVTec", 8)]
    for ax, (name, k) in zip(axes.ravel(), panels):
        sub = qq[(qq.dataset_name == name) & (qq.k_shot == k)]
        ax.plot([0, 1], [0, 1], color="#999999", linestyle="--", linewidth=0.8, zorder=1)
        for corruption, g in sub.groupby("corruption"):
            g = g.sort_values("nominal_cdf")
            ax.plot(
                g.nominal_cdf, g.empirical_cdf,
                marker="o", markersize=3.2, linewidth=1.2,
                color=CORRUPTION_COLORS.get(corruption, "#666666"),
                label=CORRUPTION_LABELS.get(corruption, corruption),
                zorder=2,
            )
        ax.set_title(f"{name}, $k={k}$")
        ax.grid(True)
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        # Tight zoom inset around the first attainable grid point, where the
        # corruption curves overlap most: y-limits hug the interpolated curve
        # values inside the window so the four series separate visually.
        p1 = 1.0 / (k + 1)
        if name == "VisA" and k == 4:
            # blur and brightness/contrast coincide at the first grid point
            # (gap 0.0006); the curves separate at the 0.4 grid point, which is
            # also where the paper reports the worst conservative gap.
            center = 2 * p1
            x0, x1 = center - 0.012, center + 0.028
            y_margin = 0.004
        else:
            x0, x1 = p1 - 0.02, p1 + 0.05
            y_margin = 0.008
        axins = ax.inset_axes([0.52, 0.07, 0.44, 0.42])
        axins.plot([0, 1], [0, 1], color="#999999", linestyle="--", linewidth=0.7, zorder=1)
        y_vals = []
        for corruption, g in sub.groupby("corruption"):
            g = g.sort_values("nominal_cdf")
            axins.plot(g.nominal_cdf, g.empirical_cdf, marker="o", markersize=3.0,
                       linewidth=1.1, color=CORRUPTION_COLORS.get(corruption, "#666666"), zorder=2)
            xs = np.concatenate([[0.0], g.nominal_cdf.to_numpy()])
            ys = np.concatenate([[0.0], g.empirical_cdf.to_numpy()])
            probe = np.concatenate([[x0, x1], xs[(xs >= x0) & (xs <= x1)]])
            y_vals.extend(np.interp(probe, xs, ys).tolist())
        lo, hi = min(y_vals) - y_margin, max(y_vals) + y_margin
        axins.set_xlim(x0, x1)
        axins.set_ylim(lo, hi)
        axins.set_xticks([])
        axins.set_yticks([])
        for spine in axins.spines.values():
            spine.set_visible(True)
            spine.set_color("#555555")
            spine.set_linewidth(0.7)
        ax.indicate_inset_zoom(axins, edgecolor="#555555", linewidth=0.7)
    axes[1, 0].set_xlabel("nominal CDF $j/(k{+}1)$")
    axes[1, 1].set_xlabel("nominal CDF $j/(k{+}1)$")
    axes[0, 0].set_ylabel("empirical CDF of normal $p$")
    axes[1, 0].set_ylabel("empirical CDF of normal $p$")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    axes[0, 0].legend(handles, labels, loc="upper left", frameon=False)
    fig.savefig(OUT / "fig_uniformity_cdf.pdf")
    plt.close(fig)


def fig_risk_coverage() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(5.6, 2.4), sharey=False, constrained_layout=True)
    for ax, (tag, name, color) in zip(
        axes,
        [("mvtec_full15_conformal_selective_reliability.csv", "MVTec (full 15)", OKABE_ITO["vermillion"]),
         ("visa_full_conformal_selective_reliability.csv", "VisA (full 12)", OKABE_ITO["blue"])],
    ):
        df = pd.read_csv(TABLES / tag)
        sub = df[(df.group == "all") & (df.prob_col == "conformal_prob_loio") & (df.risk_score == "entropy")]
        sub = sub.sort_values("coverage")
        ax.plot(sub.coverage, sub.selective_ece, marker="o", markersize=3.5, color=color)
        for _, r in sub.iterrows():
            if r.coverage in (1.0, 0.8, 0.7):
                ax.annotate(f"{r.selective_ece:.3f}", (r.coverage, r.selective_ece),
                            textcoords="offset points", xytext=(0, 5), ha="center", fontsize=6.5, color="#444444")
        ax.set_title(name)
        ax.set_xlabel("coverage (fraction not abstained)")
        ax.grid(True)
        ax.invert_xaxis()
    axes[0].set_ylabel("selective ECE (LOIO)")
    fig.savefig(OUT / "fig_risk_coverage.pdf")
    plt.close(fig)


def fig_reliability() -> None:
    fig, axes = plt.subplots(1, 2, figsize=(5.6, 2.6), sharey=True, constrained_layout=True)
    for ax, (tag, name) in zip(
        axes,
        [("mvtec_full15_conformal_reliability_bins.csv", "MVTec (full 15)"),
         ("visa_full_conformal_reliability_bins.csv", "VisA (full 12)")],
    ):
        df = pd.read_csv(TABLES / tag)
        df = df[df.prob_col == "conformal_prob_loio"]
        ax.plot([0, 1], [0, 1], color="#999999", linestyle="--", linewidth=0.8, zorder=1)
        series = []
        for k, color in [(4, OKABE_ITO["vermillion"]), (8, OKABE_ITO["blue"])]:
            sub = df[df.k_shot == k].dropna(subset=["confidence", "accuracy"])
            sub = sub[sub.n > 0].sort_values("confidence")
            series.append(sub)
            ax.plot(sub.confidence, sub.accuracy, marker="o", markersize=3.2, linewidth=1.2,
                    color=color, label=f"$k={k}$", zorder=2)
        ax.set_title(name)
        ax.set_xlabel("confidence $1-p_{\\mathrm{LOIO}}$")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.grid(True)
        del series  # k=4/k=8 curves are already visually separated; no inset here.
    axes[0].set_ylabel("empirical anomaly frequency")
    axes[0].legend(loc="lower right", frameon=False)
    fig.savefig(OUT / "fig_reliability.pdf")
    plt.close(fig)


def fig_ece_by_corruption() -> None:
    frames = []
    for tag, name in [("visa_full", "VisA"), ("mvtec_full15", "MVTec")]:
        df = pd.read_csv(TABLES / f"{tag}_conformal_vs_baselines_k_corruption.csv")
        df["dataset_name"] = name
        frames.append(df)
    data = pd.concat(frames, ignore_index=True)
    data = data[(data.group_type == "k_corruption") & (data.prob_col.isin(METHOD_COLORS))]

    corruptions = ["blur", "brightness_contrast", "gaussian_noise", "jpeg"]
    methods = list(METHOD_COLORS)
    fig, axes = plt.subplots(2, 2, figsize=(5.8, 4.6), sharey="row", constrained_layout=True)
    for row, name in enumerate(["VisA", "MVTec"]):
        for col, k in enumerate([4, 8]):
            ax = axes[row, col]
            sub = data[(data.dataset_name == name) & (data.key0.astype(int) == k)]
            x = np.arange(len(corruptions))
            width = 0.19
            for mi, method in enumerate(methods):
                vals = []
                for corruption in corruptions:
                    cell = sub[(sub.key1 == corruption) & (sub.prob_col == method)]
                    vals.append(float(cell.ece.iloc[0]) if len(cell) else np.nan)
                ax.bar(x + (mi - 1.5) * width, vals, width=width * 0.92,
                       color=METHOD_COLORS[method], label=METHOD_LABELS[method])
            ax.set_title(f"{name}, $k={k}$")
            ax.set_xticks(x)
            ax.set_xticklabels([CORRUPTION_LABELS[c] for c in corruptions], rotation=15)
            ax.grid(True, axis="y")
        axes[row, 0].set_ylabel("ECE (15 equal-width bins)")
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", ncol=4, frameon=False, bbox_to_anchor=(0.5, 1.06))
    fig.savefig(OUT / "fig_ece_by_corruption.pdf", bbox_inches="tight")
    plt.close(fig)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    fig_uniformity_cdf()
    fig_risk_coverage()
    fig_reliability()
    fig_ece_by_corruption()
    for f in sorted(OUT.glob("fig_*.pdf")):
        print(f, f.stat().st_size)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
