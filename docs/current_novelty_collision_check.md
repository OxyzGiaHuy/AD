# Current Novelty Collision Check

Date: 2026-07-03

## Claim Being Checked

Current claim:

> Shift-aware vector calibration improves probability reliability under structured corruption/domain shift for low-storage frozen-DINOv2 subspace few-shot industrial anomaly detection, while preserving PCA/subspace anomaly ranking.

This claim intentionally does not say:

- first DINOv2 few-shot anomaly detection;
- first DINOv2 PCA/subspace anomaly detector;
- first calibration benchmark;
- first calibration-under-shift method;
- adversarially robust;
- SOTA MVTec AUROC.

## Closest Prior Work And Collision Risk

| Prior Work | What It Covers | Collision With Our Current Claim |
| --- | --- | --- |
| AnomalyDINO, arXiv:2405.14529 | Frozen DINOv2 patch similarity/memory-bank few-shot industrial AD. | Covers DINOv2 few-shot memory-bank AD, not low-storage subspace + shift-aware vector calibration. |
| SubspaceAD, arXiv:2602.23013 | Frozen DINOv2 + PCA/subspace residual, training-free, strong MVTec/VisA results. | Covers DINOv2 PCA/subspace ranking. We must not claim subspace residual novelty. It does not appear to focus on calibrated probabilities or structured corruption calibration. |
| Khan & Krawczyk 2025, arXiv:2510.13643 | DINOv2 few-shot AD calibration/ECE/Platt scaling/entropy and FGSM fragility, based on AnomalyDINO. | Very close on calibration/FGSM. We must not claim first calibration or Platt scaling. Difference: our claim is decoupled subspace ranking + vector/disagreement/shift-aware calibration under structured corruption shift. |
| AD under Distribution Shift, arXiv:2303.13845 | General anomaly detection under distribution shift. | Covers distribution-shift AD broadly, not the specific few-shot DINOv2 subspace calibrated probability setting. |
| Calibration under covariate/dataset shift, e.g. arXiv:2006.16405, arXiv:2206.02757 | Calibration under shift, robust/multi-domain calibration. | Covers the broad calibration-under-shift problem. Our novelty must be task-specific and empirical/methodological, not general calibration theory. |

## Current Assessment

No direct collision found for the exact combination:

- few-shot industrial AD;
- frozen DINOv2 patch features;
- low-storage PCA/subspace detector;
- ranking/calibration decoupling;
- vector Platt using subspace score, head score, disagreement, and shift descriptors;
- full VisA structured-corruption calibration evidence;
- claim limited to probability reliability, not AUROC improvement.

However, the novelty is **incremental and combinatorial**, not a wholly new primitive. The paper must position itself carefully as a reliability-centered extension/benchmark for subspace few-shot AD.

## Safest Novelty Wording

Use:

> We study a decoupled, low-storage DINOv2 subspace detector whose raw PCA residuals provide anomaly ranking, while vector and shift-aware Platt calibration improve probability reliability under dataset and structured corruption shifts.

Avoid:

- We introduce the first DINOv2 PCA anomaly detector.
- We introduce the first calibration benchmark for DINOv2 anomaly detection.
- We solve adversarial robustness.
- We are SOTA on MVTec.
- Shift-aware calibration improves all shifts.

## Paper Positioning

The defensible contribution is:

1. A low-storage calibrated subspace detector built on frozen DINOv2.
2. A decoupled ranking-vs-calibration design.
3. A shift-aware vector calibrator for structured corruptions.
4. A unified empirical benchmark over clean accuracy, storage, calibration, transfer, pixel metrics, corruption shift, and adversarial diagnostics.

The strongest evidence is the full VisA corruption result: Shift-Aware improves ECE under blur, brightness/contrast, and JPEG while preserving AUROC/AP; Gaussian noise remains a limitation.
