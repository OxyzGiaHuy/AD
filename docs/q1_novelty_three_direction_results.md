# Q1 Novelty Push: Three Direction Experiment Results

Date: 2026-07-09

## Implemented So Far

Added scripts:

- `scripts/evaluate_validation_ece_gate.py`
- `scripts/evaluate_selective_reliability.py`
- `scripts/export_sw_cad_image_views.py`
- `scripts/merge_conformal_views.py`

Added utilities/tests:

- `src/evaluation/reliability_routing.py`
- `tests/test_reliability_routing.py`

Verification:

```text
36 passed, 1 skipped
```

## P0: Validation-Class ECE Gate

Input: `outputs/paper_tables/sage_sample_gate_representative_predictions.csv`.

Outputs:

- `outputs/paper_tables/validation_ece_gate_representative_detailed.csv`
- `outputs/paper_tables/validation_ece_gate_representative_summary.csv`

Summary:

| Split | Best ECE | Delta vs Vector | No-harm | Interpretation |
|---|---:|---:|---:|---|
| LOCO | 0.2781 | -0.0258 | 0.567 | Improves mean ECE but no-harm weak. |
| Within class split | 0.3045 | -0.0561 | 1.000 | Strong but split is easier/less general. |
| MVTec -> VisA | 0.3014 | 0.0000 | 1.000 | No gain, safe. |
| VisA -> MVTec | 0.3420 | +0.0385 | 0.000 | Fails; over-adapts under this transfer. |

Interpretation:

- Validation-ECE gate gives useful LOCO/within-dataset signal.
- It is not robust enough for universal cross-dataset claim.
- Current claim should be: ECE-aware routing improves selected class-held-out settings, but transfer requires safer target-shift handling.

## P1: Risk-Coverage / Selective Reliability

Input: `outputs/paper_tables/sage_sample_gate_representative_predictions.csv`.

Outputs:

- `outputs/paper_tables/selective_reliability_representative.csv`
- `outputs/paper_tables/risk_coverage_curves_representative.csv`

Best representative findings at 80% coverage:

| Group | Probability | Risk Score | Full ECE | Selective ECE | Relative Reduction |
|---|---|---|---:|---:|---:|
| all | vector_platt | expert_disagreement | 0.3021 | 0.2670 | 11.6% |
| VisA | vector_platt | expert_disagreement | 0.3014 | 0.2526 | 16.2% |
| MVTec | weighted_platt | expert_disagreement | 0.3420 | 0.2721 | 20.5% |
| MVTec | shift_aware_vector_platt | expert_disagreement | 0.3413 | 0.2717 | 20.4% |

Interpretation:

- Selective reliability is currently the strongest new diagnostic signal.
- Expert disagreement is the best risk score so far.
- This supports an industrial reliability claim: uncertain/high-disagreement samples can be flagged/abstained to reduce calibration error.

## P2: SW-CAD Per-Image Conformal Views

Representative export completed.

Outputs:

- `outputs/paper_tables/sw_cad_image_views_representative_visa.csv`: VisA `64/64` cases, `7360` rows.
- `outputs/paper_tables/sw_cad_image_views_representative_mvtec.csv`: MVTec `48/48` cases, `4768` rows.
- `outputs/paper_tables/sw_cad_image_views_representative_full.csv`: combined `12128` rows.
- `outputs/paper_tables/sage_sample_gate_representative_with_conformal_full.csv`: merge with sample-level predictions, `missing_conformal=0`.

Implementation note:

- Full weighted patch conformal was too slow for the representative grid, so the current prototype keeps LOIO patch rejection and image-level weighted conformal.
- `conformal_prob_loio = 1 - image_p_loio` is a statistical reliability view, not a replacement for the raw PCA/subspace ranking.
- The DINOv2 loader was patched to prefer local Torch Hub cache to avoid GitHub timeout during long offline runs.

## P3: Gated + Conformal View

Input: `outputs/paper_tables/sage_sample_gate_representative_with_conformal_full.csv`.

Outputs:

- `outputs/paper_tables/validation_ece_gate_representative_conformal_full_detailed.csv`
- `outputs/paper_tables/validation_ece_gate_representative_conformal_full_summary.csv`
- `outputs/paper_tables/selective_reliability_representative_conformal_full.csv`
- `outputs/paper_tables/risk_coverage_curves_representative_conformal_full.csv`

Validation-ECE gate with conformal experts:

| Split | Gate ECE | Vector ECE | Delta vs Vector | No-harm | Note |
|---|---:|---:|---:|---:|---|
| LOCO | 0.1156 | 0.3039 | -0.1883 | 1.000 | Strong class-held-out gain. |
| Within class split | 0.1537 | 0.3606 | -0.2068 | 1.000 | Strong, but easier split. |
| MVTec -> VisA | 0.0985 | 0.3014 | -0.2028 | 1.000 | Strong transfer gain. |
| VisA -> MVTec | 0.1019 | 0.3035 | -0.2016 | 1.000 | Previous failure fixed by conformal view. |

The selected expert is consistently `conformal_prob_loio`. This is good evidence that conformal p-value views add a useful statistical reliability channel, but it also means the current result is closer to **conformal reliability routing** than to the earlier calibrator-only SAGE gate.

Selective reliability with conformal view at 80% coverage:

| Group | Probability | Risk Score | Full ECE | Selective ECE | Relative Reduction |
|---|---|---|---:|---:|---:|
| MVTec | conformal_prob_loio | entropy_selected | 0.1019 | 0.0361 | 64.6% |
| VisA | conformal_prob_loio | combined_entropy_disagreement_neff | 0.0985 | 0.0495 | 49.7% |
| all | conformal_prob_loio | combined_entropy_disagreement_neff | 0.0998 | 0.0590 | 40.9% |
| all | conformal_prob_loio | expert_disagreement | 0.0998 | 0.0667 | 33.2% |

AURC/ECE also supports the same direction: best AURC values come from `conformal_prob_loio` combined with entropy/disagreement/`n_eff` risk scores.

## Current Claim Implication

Strongest claim after P0-P3:

> A low-storage decoupled DINOv2 subspace detector can be extended with conformal reliability views and SAGE-style validation-ECE routing. On representative MVTec+VisA shifts, the conformal view reduces ECE by about `0.18-0.21` absolute versus Vector Platt with no observed harm across LOCO, within-dataset, and cross-dataset splits.

Strong diagnostic claim:

> Reliability signals such as entropy, expert disagreement, and conformal/effective-sample-size views identify high-risk samples; abstaining on the top 20% risk samples reduces ECE by about `41%` overall, `50%` on VisA, and `65%` on MVTec in the representative conformal-view benchmark.

Claim caveats:

- Do not claim SOTA AUROC on MVTec. Ranking remains the raw PCA/subspace residual.
- Do not claim adversarial robustness. FGSM remains a diagnostic/failure-case direction.
- Do not claim first conformal anomaly detection. The defensible novelty is integrating conformal p-value views into a low-storage few-shot DINOv2 subspace AD reliability-routing pipeline.
- The current conformal gate uses validation labels to choose the expert, so the next paper-grade step is to lock a validation protocol or derive a normal-only/no-label gate rule.
