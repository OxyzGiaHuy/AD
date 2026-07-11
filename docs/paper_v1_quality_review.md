# Paper V1 Quality Review

Date: 2026-07-10

## What Was Improved

This pass rewrote the IEEE draft from a result dump into a more submission-like research story.

Main improvements:

- The paper now uses the name **Conformal Reliability Routing (CRR)**.
- Motivation is framed around the deployment gap between anomaly ranking and reliable alarm probability.
- The novelty boundary is explicit: CRR does not claim DINOv2, PCA residuals, Platt scaling, conformal prediction, or gated experts as individually new.
- Method now defines:
  - few-shot normal-only setup;
  - frozen DINOv2 patch features;
  - PCA/subspace residual ranking;
  - Vector/Shift-Aware Platt calibration;
  - LOIO conformal reliability;
  - reliability routing and selective diagnostics.
- Experiments now separate:
  - clean accuracy/storage;
  - accuracy-storage PCA64 vs PCA128;
  - full VisA corruption reliability;
  - representative routing protocols;
  - pixel and adversarial fragility diagnostics.
- Results now emphasize the strongest defensible claim: LOIO conformal reliability lowers ECE on full VisA corruptions while preserving raw PCA/subspace ranking.

## Current Main Claim

A low-storage decoupled DINOv2 subspace detector can preserve PCA/subspace residual ranking while adding LOIO conformal reliability views that substantially improve calibration under VisA corruption shifts.

## Evidence Currently In Paper

- MVTec clean AUROC is competitive but not SOTA; storage is much lower than memory-bank rows.
- VisA PCA128 improves AUROC over PCA64 by about 0.011--0.017 while storage remains below 0.6 MB.
- Full VisA corruption benchmark:
  - 12 classes;
  - k = 4 and 8;
  - 5 seeds;
  - 4 corruptions;
  - 56,000 image rows.
- LOIO conformal ECE:
  - overall: 0.0766;
  - k4: 0.0391;
  - k8: 0.1140.
- LOIO conformal improves over Vector Platt and Shift-Aware Platt in every tested k/corruption cell.

## Claims To Avoid

- Do not claim MVTec AUROC SOTA.
- Do not claim adversarial robustness.
- Do not claim first DINOv2 PCA/subspace method.
- Do not claim first conformal anomaly detection.
- Do not claim SAGE architecture is used directly; cite SAGE only as routing inspiration.

## Experiments Still Recommended Before Submission

Priority 1:

- Full MVTec conformal routing, matching the full VisA protocol.
- Stronger no-label routing/gating ablation: can shift descriptors and effective sample size choose the safe reliability route without anomaly validation labels?
- False-alarm control table at fixed conformal thresholds, not only ECE.

Priority 2:

- More official baseline alignment with SubspaceAD and AnomalyDINO under the same preprocessing/splits.
- Risk-coverage curves using conformal confidence, entropy, and effective sample size.
- End-to-end runtime audit including feature extraction, not only cached-feature scoring.

Priority 3:

- Expand transfer calibration experiments beyond representative splits.
- Improve qualitative heatmap figures and add failure cases.

## Build Notes

The current environment does not have `pdflatex`, `latexmk`, `xelatex`, or `tectonic`, so PDF compilation could not be run here. Static checks passed for citation keys and included section/table files.
