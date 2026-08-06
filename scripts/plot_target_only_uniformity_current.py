"""Plot the current target-only CDF audit from an explicit coordinates CSV."""
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


COLORS = {
    "blur": "#0072B2",
    "brightness_contrast": "#E69F00",
    "gaussian_noise": "#D55E00",
    "jpeg": "#009E73",
}
LABELS = {
    "blur": "blur",
    "brightness_contrast": "bright/contr.",
    "gaussian_noise": "Gaussian noise",
    "jpeg": "JPEG",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    data = pd.read_csv(args.input)
    required = {"dataset", "k_shot", "corruption", "nominal_cdf", "empirical_cdf"}
    missing = sorted(required - set(data.columns))
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    plt.rcParams.update(
        {
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
            "lines.linewidth": 1.3,
            "pdf.fonttype": 42,
        }
    )

    fig, grid = plt.subplots(2, 2, figsize=(5.6, 4.7), constrained_layout=True)
    panels = [("visa", "VisA", 4), ("visa", "VisA", 8), ("mvtec", "MVTec", 4), ("mvtec", "MVTec", 8)]
    for ax, (dataset, title, k_shot) in zip(grid.ravel(), panels):
        panel = data[(data.dataset == dataset) & (data.k_shot == k_shot)]
        ax.plot([0, 1], [0, 1], color="#999999", linestyle="--", linewidth=0.8, zorder=1)
        for corruption in COLORS:
            series = panel[panel.corruption == corruption].sort_values("nominal_cdf")
            ax.plot(
                series.nominal_cdf,
                series.empirical_cdf,
                marker="o",
                markersize=3.2,
                color=COLORS[corruption],
                label=LABELS[corruption],
                zorder=2,
            )
        ax.set_title(f"{title}, $k={k_shot}$")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.grid(True)

        # The inset stays inside the lower-right white region.  Tick labels are
        # placed on its right so the connector rays cannot cross them.
        p_min = 1.0 / (k_shot + 1.0)
        x0, x1 = p_min - 0.018, p_min + 0.045
        inset = ax.inset_axes([0.54, 0.08, 0.36, 0.28])
        inset.plot([0, 1], [0, 1], color="#999999", linestyle="--", linewidth=0.7, zorder=1)
        local_y: list[float] = []
        for corruption in COLORS:
            series = panel[panel.corruption == corruption].sort_values("nominal_cdf")
            inset.plot(
                series.nominal_cdf,
                series.empirical_cdf,
                marker="o",
                markersize=3.0,
                color=COLORS[corruption],
                zorder=2,
            )
            xs = np.concatenate([[0.0], series.nominal_cdf.to_numpy()])
            ys = np.concatenate([[0.0], series.empirical_cdf.to_numpy()])
            local_y.extend(np.interp([x0, p_min, x1], xs, ys).tolist())
        margin = 0.007 if title == "VisA" else 0.012
        inset.set_xlim(x0, x1)
        inset.set_ylim(min(local_y) - margin, max(local_y) + margin)
        inset.yaxis.tick_right()
        inset.tick_params(axis="both", labelsize=6, length=2, pad=1)
        inset.tick_params(axis="y", labelleft=False, labelright=True)
        inset.grid(True)
        inset.set_facecolor("white")
        for spine in inset.spines.values():
            spine.set_visible(True)
            spine.set_color("#555555")
            spine.set_linewidth(0.7)
        indicator = ax.indicate_inset_zoom(
            inset, edgecolor="#666666", alpha=0.85, linewidth=0.65, zorder=3
        )
        for connector in indicator.connectors or ():
            connector.set_linewidth(0.65)
            connector.set_color("#666666")
            connector.set_alpha(0.85)

    grid[1, 0].set_xlabel("attainable rank value $j/(k{+}1)$")
    grid[1, 1].set_xlabel("attainable rank value $j/(k{+}1)$")
    grid[0, 0].set_ylabel(r"empirical CDF $\widehat{F}(t)$")
    grid[1, 0].set_ylabel(r"empirical CDF $\widehat{F}(t)$")
    handles, labels = grid[0, 0].get_legend_handles_labels()
    grid[0, 0].legend(handles, labels, loc="upper left", frameon=False)

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(output, bbox_inches="tight")
    plt.close(fig)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
