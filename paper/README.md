# Paper v1: Conformal Reliability Routing for Low-Storage Few-Shot Industrial Anomaly Detection

This folder contains an IEEE-style internal draft for advisor discussion.

## Main File

- `main.tex`: IEEEtran conference-style LaTeX source.
- `sections/`: paper sections.
- `tables/`: compact tables copied from current experiment evidence.
- `figures/`: small paper-ready figures copied from `outputs/figures`.
- `references.bib`: current bibliography entries.

## Current Main Claim

A low-storage decoupled DINOv2 subspace detector can preserve PCA/subspace residual ranking while adding LOIO conformal reliability views that substantially improve calibration under VisA corruption shifts.

This draft intentionally does **not** claim:

- MVTec AUROC SOTA.
- Adversarial robustness.
- First DINOv2 PCA/subspace residual method.
- First conformal anomaly detection method.
- First calibration benchmark.

## Compile

On a machine with LaTeX installed:

```bash
cd /home/crl/AD/paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

The current Codex environment does not have `pdflatex`, so PDF build was not run here.

## Important Evidence Included

- Clean accuracy/storage table for MVTec and VisA.
- Full VisA conformal reliability table, 56,000 image rows.
- ECE by corruption comparing Vector Platt, Shift-Aware Platt, LOIO conformal, and weighted conformal.
- Protocol-locked routing table.
- Pixel/robustness diagnostic table.
- Prior-work positioning table to avoid novelty collision.

## Suggested Next Edits Before Submission

1. Add real author affiliation.
2. Replace placeholder anonymous block if not double-blind.
3. Add exact venue template if targeting a specific IEEE journal/conference.
4. Add full MVTec conformal routing if completed later.
5. Tighten references with final BibTeX from official sources.
