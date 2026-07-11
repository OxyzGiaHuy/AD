# Paper Draft

This folder contains a first LaTeX draft for the conformal reliability routing paper.

Main file:

```bash
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

Key generated tables are in `paper/tables/`. Figures are referenced from `outputs/figures/` to avoid duplicating artifacts.

Current framing: reliability/calibration/efficiency, not MVTec AUROC SOTA or adversarial robustness.
