# Paper Outline: Conformal Reliability Routing for Few-Shot Industrial AD

## Title Working Draft

Conformal Reliability Routing for Low-Storage Few-Shot Industrial Anomaly Detection

## 1. Introduction

Core problem: few-shot industrial AD has strong DINOv2 ranking methods, but reliability under low-shot, class shift, dataset shift, and corruption remains underdeveloped.

Positioning:

- AnomalyDINO: strong DINOv2 memory-bank ranking.
- SubspaceAD: strong DINOv2 PCA/subspace residual ranking.
- Khan & Krawczyk: calibration/adversarial fragility analysis with Platt scaling.
- Our angle: decouple ranking from reliability and add conformal reliability routing for low-storage subspace AD.

## 2. Method

- Frozen DINOv2 patch features.
- PCA/subspace residual ranking.
- Calibration baselines: Vector Platt, Shift-Aware Platt, Weighted Platt.
- LOIO conformal p-values from few-shot normal support.
- Reliability routing:
  - fixed conformal view;
  - validation ECE route;
  - no-label shift/effective-sample-size gate.
- Selective reliability: entropy, disagreement, conformal p-values, `n_eff`.

## 3. Benchmark Protocol

- MVTec and VisA.
- Few-shot k `{1,2,4,8}` for main clean tables where available.
- Representative conformal routing: MVTec/VisA transfer, LOCO, within split, corruptions.
- Full VisA conformal scale-up: k `{4,8}`, seeds `{0..4}`, 12 classes, 4 corruptions.
- Metrics: AUROC/AP for ranking, ECE/Brier/NLL for reliability, risk-coverage/selective ECE for diagnostic utility, storage/latency for efficiency.

## 4. Results

Main tables:

1. Clean ranking and efficiency: show low storage and competitive AUROC.
2. Calibration: Vector/Shift-Aware/Weighted/Conformal.
3. Protocol-locked conformal routing: fixed/no-label/validation protocols.
4. Selective reliability: ECE vs coverage.
5. Robustness/corruption diagnostic.

Expected main message:

- We do not beat all memory-bank/subspace methods on AUROC.
- We improve reliability strongly with conformal views while preserving ranking.
- We provide practical risk flagging under shift.

## 5. Ablation

- Vector Platt only.
- Shift-Aware Platt.
- Weighted Platt.
- Fixed LOIO conformal view.
- Vector/conformal mixture.
- No-label shift/neff gate.
- Validation-ECE vector-or-conformal gate.
- Selective abstention signals.

## 6. Limitations

- Not SOTA AUROC on MVTec.
- Not adversarially robust.
- Conformal validity depends on calibration assumptions; distribution shift still needs diagnostics.
- Full-scale confirmation is still needed for the new conformal routing claim.
- SAGE is architectural inspiration for routing, not the implemented segmentation architecture.

## 7. Claim Statement

A paper-safe claim:

> We introduce a low-storage, decoupled DINOv2 subspace AD pipeline that preserves PCA residual ranking while using LOIO conformal p-value views for reliability routing. On representative MVTec/VisA transfer and class-held-out protocols, the fixed conformal reliability view substantially reduces ECE over Vector Platt and enables selective risk flagging under shift.
