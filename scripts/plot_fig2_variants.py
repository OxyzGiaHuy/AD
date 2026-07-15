"""Color-tone variants of Figure 2 (ECE by corruption) for side-by-side choice.

Renders latex/figures/variants/fig_ece_by_corruption_v{1..5}.pdf (+ .png
previews and a contact sheet). All palettes are CVD-checked; v5 is a
deliberate accent design (Platt baselines in neutral grays separated by
lightness, conformal routes carrying color).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

import plot_paper_v2_figures as base

VARIANTS = {
    "v1_okabe_ito": {
        "vector_platt": "#0072B2", "shift_aware_vector_platt": "#56B4E9",
        "conformal_prob_loio": "#D55E00", "conformal_prob_weighted": "#E69F00",
    },
    "v2_green_blue": {
        "vector_platt": "#009E73", "shift_aware_vector_platt": "#0072B2",
        "conformal_prob_loio": "#D55E00", "conformal_prob_weighted": "#CC79A7",
    },
    "v3_dark2": {
        "vector_platt": "#1B9E77", "shift_aware_vector_platt": "#7570B3",
        "conformal_prob_loio": "#D95F02", "conformal_prob_weighted": "#E7298A",
    },
    "v4_cool_warm": {
        "vector_platt": "#3E6FB0", "shift_aware_vector_platt": "#2E9E4F",
        "conformal_prob_loio": "#E0567B", "conformal_prob_weighted": "#A8922E",
    },
    "v5_accent_loio": {
        "vector_platt": "#8F8F8F", "shift_aware_vector_platt": "#C4C4C4",
        "conformal_prob_loio": "#D55E00", "conformal_prob_weighted": "#0072B2",
    },
    # Nature tones: Platt pair in greens, LOIO in terracotta, weighted in ochre.
    "v6_nature_forest": {
        "vector_platt": "#1F7A53", "shift_aware_vector_platt": "#7FB25E",
        "conformal_prob_loio": "#C75D63", "conformal_prob_weighted": "#CE9426",
    },
    "v7_nature_moss": {
        "vector_platt": "#35854A", "shift_aware_vector_platt": "#8FA842",
        "conformal_prob_loio": "#B85042", "conformal_prob_weighted": "#C9A227",
    },
    # Deliberately muted (true earthy chroma); identity is also carried by the
    # legend, fixed ordering, and bar gaps, so the low-chroma greens stay legal.
    "v8_nature_muted": {
        "vector_platt": "#2D6A4F", "shift_aware_vector_platt": "#7FA96B",
        "conformal_prob_loio": "#C1666B", "conformal_prob_weighted": "#C99733",
    },
    # Nature-journal (npg) palette: navy/cyan for the Platt pair, Nature red
    # for LOIO, teal for weighted. Navy sits just under the chroma floor
    # (0.09); legal here because the legend and bar gaps carry identity.
    "v9_npg": {
        "vector_platt": "#3C5488", "shift_aware_vector_platt": "#4DBBD5",
        "conformal_prob_loio": "#E64B35", "conformal_prob_weighted": "#00A087",
    },
}

OUT = Path(__file__).resolve().parents[1] / "latex" / "figures" / "variants"


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    original_out = base.OUT
    pdfs = []
    for name, palette in VARIANTS.items():
        base.METHOD_COLORS.clear()
        base.METHOD_COLORS.update(palette)
        base.OUT = OUT
        base.fig_ece_by_corruption()
        src = OUT / "fig_ece_by_corruption.pdf"
        dst = OUT / f"fig_ece_by_corruption_{name}.pdf"
        src.rename(dst)
        pdfs.append(dst)
        print("wrote", dst.name)
    base.OUT = original_out

    import subprocess
    pngs = []
    for pdf in pdfs:
        png = pdf.with_suffix("")
        subprocess.run(["pdftoppm", "-png", "-r", "110", "-singlefile", str(pdf), str(png)], check=True)
        pngs.append(png.with_suffix(".png"))

    import matplotlib.image as mpimg
    fig, axes = plt.subplots(4, 2, figsize=(14, 24))
    for ax in axes.ravel():
        ax.axis("off")
    for ax, png in zip(axes.ravel(), pngs):
        ax.imshow(mpimg.imread(png))
        ax.set_title(png.stem.replace("fig_ece_by_corruption_", ""), fontsize=14)
    fig.tight_layout()
    fig.savefig(OUT / "contact_sheet.png", dpi=90)
    print("wrote", OUT / "contact_sheet.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
