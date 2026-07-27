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
OUT = ROOT / "els-cas-templates" / "figures"

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

# Committed fallback for the four Q--Q panels.  These are the exact plotted
# coordinates recovered from the previous vector figure; they keep the paper
# figure reproducible when the large experiment-output directory is absent.
UNIFORMITY_QQ_FALLBACK = {
    ("VisA", 4): {
        "blur": [0.155302, 0.315017, 0.540598, 0.781179, 1.0],
        "brightness_contrast": [0.154715, 0.320017, 0.546491, 0.800898, 1.0],
        "gaussian_noise": [0.142063, 0.303232, 0.561491, 0.821484, 1.0],
        "jpeg": [0.157368, 0.324430, 0.562077, 0.802939, 1.0],
    },
    ("VisA", 8): {
        "blur": [0.109130, 0.212954, 0.360297, 0.464427, 0.560011, 0.657662, 0.789419, 0.899135, 1.0],
        "brightness_contrast": [0.110303, 0.214714, 0.367057, 0.482360, 0.579705, 0.681182, 0.802658, 0.907655, 1.0],
        "gaussian_noise": [0.103237, 0.210581, 0.376776, 0.486187, 0.612076, 0.717660, 0.841764, 0.925308, 1.0],
        "jpeg": [0.122956, 0.236193, 0.390602, 0.498253, 0.609117, 0.709115, 0.832657, 0.922961, 1.0],
    },
    ("MVTec", 4): {
        "blur": [0.306217, 0.493941, 0.693809, 0.844417, 1.0],
        "brightness_contrast": [0.313359, 0.493941, 0.699497, 0.852249, 1.0],
        "gaussian_noise": [0.463253, 0.628836, 0.834417, 0.943624, 1.0],
        "jpeg": [0.409709, 0.589577, 0.774445, 0.909365, 1.0],
    },
    ("MVTec", 8): {
        "blur": [0.194153, 0.325476, 0.420423, 0.543200, 0.615290, 0.740899, 0.853677, 0.925767, 1.0],
        "brightness_contrast": [0.188439, 0.326191, 0.418994, 0.536772, 0.627407, 0.736614, 0.854391, 0.926481, 1.0],
        "gaussian_noise": [0.355476, 0.521772, 0.617433, 0.741614, 0.806587, 0.894365, 0.955052, 0.980026, 1.0],
        "jpeg": [0.306931, 0.443968, 0.545343, 0.673809, 0.736614, 0.827275, 0.910793, 0.955766, 1.0],
    },
}

# Exact values recovered from the committed vector figure.  The source CSVs
# also contain an AURC summary row; it is intentionally excluded here because
# AURC is a scalar summary, not an additional coverage operating point.
RISK_COVERAGE_FALLBACK = {
    "MVTec (full 15)": {
        "coverage": [1.0, 0.95, 0.9, 0.8, 0.7],
        "selective_ece": [0.06846, 0.05569, 0.04975, 0.03045, 0.02273],
    },
    "VisA (full 12)": {
        "coverage": [1.0, 0.95, 0.9, 0.8, 0.7],
        "selective_ece": [0.07656, 0.07391, 0.06764, 0.07515, 0.06594],
    },
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
        source = TABLES / f"pvalue_uniformity_{tag}_qq.csv"
        if source.exists():
            df = pd.read_csv(source)
            df["dataset_name"] = name
            frames.append(df)
        else:
            rows = []
            for (dataset_name, k), series in UNIFORMITY_QQ_FALLBACK.items():
                if dataset_name != name:
                    continue
                nominal = np.arange(1, k + 2) / (k + 1)
                for corruption, empirical in series.items():
                    rows.extend({
                        "dataset_name": name,
                        "k_shot": k,
                        "corruption": corruption,
                        "pvalue_col": "image_p_loio",
                        "nominal_cdf": x,
                        "empirical_cdf": y,
                    } for x, y in zip(nominal, empirical))
            frames.append(pd.DataFrame(rows))
    qq = pd.concat(frames, ignore_index=True)
    qq = qq[qq.pvalue_col == "image_p_loio"]

    # Keep each zoom inside its parent panel in the data-free lower-right region.
    # The marked source rectangle and connector rays make the zoom provenance
    # explicit without crossing the main data curves.
    fig, grid = plt.subplots(2, 2, figsize=(5.6, 4.7), constrained_layout=True)
    axes = grid.ravel()
    panels = [("VisA", 4), ("VisA", 8), ("MVTec", 4), ("MVTec", 8)]
    for ax, (name, k) in zip(axes, panels):
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
        axins = ax.inset_axes([0.53, 0.08, 0.37, 0.28])
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
        # Put the inset y labels on the side opposite the connector rays.
        # This prevents the rays entering the left inset corners from crossing
        # numeric tick labels.
        axins.yaxis.tick_right()
        axins.tick_params(axis="x", labelsize=6, length=2, pad=1)
        axins.tick_params(
            axis="y",
            labelsize=6,
            length=2,
            pad=1,
            labelleft=False,
            labelright=True,
        )
        axins.grid(True)
        axins.set_facecolor("white")
        for spine in axins.spines.values():
            spine.set_visible(True)
            spine.set_color("#555555")
            spine.set_linewidth(0.7)
        indicator = ax.indicate_inset_zoom(
            axins,
            edgecolor="#666666",
            alpha=0.85,
            linewidth=0.65,
            zorder=3,
        )
        # Matplotlib chooses the two least-cluttered connectors automatically.
        # Keep them above the grid but below the inset data.
        for connector in indicator.connectors or ():
            connector.set_linewidth(0.65)
            connector.set_color("#666666")
            connector.set_alpha(0.85)
    axes[2].set_xlabel("nominal CDF $j/(k{+}1)$")
    axes[3].set_xlabel("nominal CDF $j/(k{+}1)$")
    axes[0].set_ylabel("empirical CDF of normal $p$")
    axes[2].set_ylabel("empirical CDF of normal $p$")
    handles, labels = axes[0].get_legend_handles_labels()
    axes[0].legend(handles, labels, loc="upper left", frameon=False)
    fig.savefig(OUT / "fig_uniformity_cdf.pdf", bbox_inches="tight")
    plt.close(fig)


def fig_risk_coverage() -> None:
    # Native single-column dimensions: avoid shrinking a double-column canvas
    # after LaTeX placement, which would make labels and annotations too small.
    fig, ax = plt.subplots(figsize=(3.35, 2.45), constrained_layout=True)
    series = [
        ("mvtec_full15_conformal_selective_reliability.csv", "MVTec (15)",
         "MVTec (full 15)", OKABE_ITO["vermillion"], "o"),
        ("visa_full_conformal_selective_reliability.csv", "VisA (12)",
         "VisA (full 12)", OKABE_ITO["blue"], "s"),
    ]
    for tag, name, fallback_name, color, marker in series:
        source = TABLES / tag
        if source.exists():
            df = pd.read_csv(source)
            sub = df[(df.group == "all") & (df.prob_col == "conformal_prob_loio")
                     & (df.risk_score == "entropy")].copy()
            sub["coverage"] = pd.to_numeric(sub.coverage, errors="coerce")
            sub = sub.dropna(subset=["coverage", "selective_ece"])
            sub = sub[sub.coverage.between(0.0, 1.0)].sort_values("coverage", ascending=False)
        else:
            sub = pd.DataFrame(RISK_COVERAGE_FALLBACK[fallback_name])
        ax.plot(sub.coverage, sub.selective_ece, marker=marker, markersize=4.0,
                color=color, label=name)
        for _, r in sub.iterrows():
            if r.coverage in (1.0, 0.8, 0.7):
                ax.annotate(f"{r.selective_ece:.3f}", (r.coverage, r.selective_ece),
                            textcoords="offset points", xytext=(0, 5), ha="center", fontsize=6.5, color="#444444")
    ax.set_xlabel("coverage (fraction not abstained)")
    ax.set_ylabel("selective ECE (LOIO)")
    ax.set_xticks([1.0, 0.95, 0.9, 0.8, 0.7])
    ax.set_xlim(1.015, 0.685)
    ax.grid(True)
    ax.legend(loc="upper center", ncol=2, frameon=False,
              bbox_to_anchor=(0.5, 1.16), columnspacing=0.9)
    fig.savefig(OUT / "fig_risk_coverage.pdf", bbox_inches="tight")
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
