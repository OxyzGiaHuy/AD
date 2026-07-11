# Novelty And Current Claims

This note tracks the current paper claims and what should not be overclaimed.
For an onboarding-friendly explanation in Vietnamese, see
[`novelty_claims_explained.md`](novelty_claims_explained.md).
For the latest post-P0/P1 status, see
[`novelty_claim_explained_2.md`](novelty_claim_explained_2.md).

## Current Claim

The main method should be framed as a **Decoupled Calibrated Subspace Head** for
few-shot industrial anomaly detection with frozen DINOv2 features.

Recommended claim:

> A decoupled calibrated subspace head approaches memory-bank AUROC on MVTec,
> improves VisA AUROC over PatchCore/AnomalyDINO in the current benchmark,
> greatly reduces storage, improves calibration, and exposes robustness limits
> under corruption and FGSM-style adversarial evaluation.

## What Not To Claim

- Do not claim SOTA AUROC on all MVTec settings.
- Do not claim DINOv2 few-shot memory-bank anomaly detection is new.
- Do not claim frozen DINOv2 + PCA residual scoring is new.
- Do not claim first calibration/adversarial benchmark for DINOv2 few-shot AD.
- Do not claim adversarial robustness; current FGSM results show severe
  fragility.

## Novelty Verification

- **AnomalyDINO** already covers frozen DINOv2 patch similarity/memory-bank
  style few-shot anomaly detection, including image-level and pixel-level
  anomaly outputs. Link: https://arxiv.org/abs/2405.14529
- **SubspaceAD** already covers frozen DINOv2 patch features with PCA/subspace
  residual scoring, training-free and without memory banks. Link:
  https://arxiv.org/abs/2602.23013
- **Khan & Krawczyk 2025** already covers DINOv2-based few-shot AD calibration,
  ECE, Platt scaling, uncertainty, and FGSM-style adversarial evaluation. Link:
  https://arxiv.org/abs/2510.13643

## Remaining Defensible Novelty

- Decoupled design: use PCA/subspace residual for ranking, and use a calibrated
  head for posterior probability and uncertainty.
- Vector Platt calibration over `[subspace_score, head_score, disagreement]`.
- Unified empirical story across AUROC/AP, calibration, storage/latency,
  corruption, FGSM fragility, and ablations on MVTec and VisA.
- Stronger novelty after additional P0/P1 work: qualitative heatmaps,
  pixel metrics, calibration ablation, and MVTec to VisA transfer calibration.


## 2026-07-02 Final P1 Update

- Extended transfer calibration ablation is complete: `720/720` runs.
- MVTec-transfer calibration on VisA: AUROC k1 `0.8226`, k8 `0.8824`; ECE k1 `0.4319`, k8 `0.2324`.
- VisA normal-synthetic calibration improves high-k ECE to `0.2066` at k8 without changing ranking.
- Upper-bound VisA anomaly-val improves low-shot ECE to `0.3787` at k1 but must be reported as an upper-bound.
- Official SubspaceAD representative remains a key novelty guardrail: average image AUROC `0.9518`, pixel AUROC `0.9710` on bottle/cable/hazelnut k1.
- Current main claim: calibrated low-storage subspace detection with transfer/calibration-shift diagnostics, not pure AUROC SOTA.
