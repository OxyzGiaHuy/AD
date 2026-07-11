# Paper Draft Status

Date: 2026-07-10

## Draft Created

Created a first LaTeX manuscript scaffold in `paper/`:

- `paper/main.tex`
- `paper/references.bib`
- `paper/sections/abstract.tex`
- `paper/sections/introduction.tex`
- `paper/sections/related_work.tex`
- `paper/sections/method.tex`
- `paper/sections/experiments.tex`
- `paper/sections/results.tex`
- `paper/sections/limitations.tex`
- `paper/sections/conclusion.tex`
- `paper/tables/tab_visa_full_conformal.tex`
- `paper/tables/tab_visa_ece_by_corruption.tex`
- `paper/tables/tab_protocol_routing.tex`

## Main Story In Draft

Working title:

> Conformal Reliability Routing for Low-Storage Few-Shot Industrial Anomaly Detection

Main claim:

> Preserve DINOv2 PCA/subspace residual ranking, add LOIO conformal p-value views as a reliability layer, and show full VisA calibration improvement under corruptions.

This draft explicitly avoids overclaiming:

- no MVTec AUROC SOTA claim;
- no adversarial robustness claim;
- no first conformal AD claim;
- no first DINOv2 PCA/subspace residual claim.

## Key Evidence Included

Full VisA k4/k8 corruption benchmark:

- `480/480` cases.
- `56,000` images.
- LOIO conformal overall ECE: `0.0766`.
- LOIO k4 ECE: `0.0391`.
- LOIO k8 ECE: `0.1140`.
- LOIO beats Vector Platt and Shift-Aware Platt in every tested k/corruption ECE cell.

Figures referenced:

- `outputs/figures/visa_full_loio_reliability_all.png`
- `outputs/figures/visa_full_loio_reliability_k4.png`
- `outputs/figures/visa_full_loio_reliability_k8.png`
- `outputs/figures/visa_full_ece_by_corruption_k4.png`
- `outputs/figures/visa_full_ece_by_corruption_k8.png`

## Compile Note

`pdflatex` is not available in the current environment PATH, so PDF compilation was not run here. The draft is structured for standard LaTeX compilation:

```bash
cd paper
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Next Paper Tasks

1. Add full MVTec or stronger representative MVTec conformal table if compute allows.
2. Add a clean method diagram for decoupled ranking/reliability.
3. Add more precise citations once final venue format is chosen.
4. Add appendix with protocol details and failure cases.
5. Decide whether to include SAGE in main related work or only as inspiration in appendix.
