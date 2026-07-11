# Sample-Level SAGE-Style Gate Results

Date: 2026-07-09

## Mục tiêu

Nâng Gated Shift-Aware từ offline case-level routing lên sample-level routing: mỗi ảnh có expert probabilities riêng và gate chọn expert/view theo sample descriptors.

Experts/views:

- `vector_platt`: safe probability view.
- `shift_aware_vector_platt`: shift descriptor view.
- `weighted_platt`: density-ratio view.
- `anchored_structured_gate`: anchored routing view.

Gate variants:

- `sample_logistic_top1_nll`: train softmax gate chọn expert giảm NLL theo sample.
- `sample_risk_margin_*`: predict per-expert NLL loss và chỉ rời anchor nếu gain vượt margin.
- `sample_sage_hier_t*`: SAGE-style shared/dynamic gate, threshold càng cao càng conservative.

## Grid

Representative grid:

- VisA: `candle`, `cashew`, `pcb1`, `pipe_fryum`.
- MVTec: `bottle`, `cable`, `hazelnut`.
- k `{4,8}`.
- seeds `{0,1}`.
- corruptions `{gaussian_noise, blur, brightness_contrast, jpeg}`.
- max `120` images/case.

Completed:

- `112/112` cases.
- `12128` per-image prediction rows.
- `126` evaluation rows.

Outputs:

- `outputs/paper_tables/sage_sample_gate_representative_predictions.csv`
- `outputs/paper_tables/sage_sample_gate_representative_evaluation.csv`

## Main Results

### Leave-One-Class-Out, All Representative Classes

| Method | ECE | Brier | NLL | AUROC |
|---|---:|---:|---:|---:|
| oracle_sample_best_nll | 0.2564 | 0.2303 | 1.2593 | 0.8859 |
| sample_logistic_top1_nll | 0.2581 | 0.2553 | 1.6849 | 0.8859 |
| sample_sage_hier_t0.5 | 0.2587 | 0.2557 | 1.6578 | 0.8859 |
| sample_risk_margin_0 | 0.2611 | 0.2520 | 1.4286 | 0.8859 |

Interpretation: sample-level learned gates improve only modestly under LOCO. The oracle gap is also small in ECE, meaning current per-sample expert probabilities do not create large ECE headroom on this representative grid.

### Leave-One-Class-Out, VisA Only

| Method | ECE | Brier | NLL | AUROC |
|---|---:|---:|---:|---:|
| oracle_sample_best_nll | 0.2297 | 0.2007 | 0.9648 | 0.9015 |
| sample_logistic_top1_nll | 0.2305 | 0.2322 | 1.5304 | 0.9015 |
| sample_sage_hier_t0.5 | 0.2309 | 0.2324 | 1.5127 | 0.9015 |
| weighted_platt | 0.2341 | 0.2312 | 1.1305 | 0.9015 |

Interpretation: sample-level gate slightly beats individual experts on ECE, but NLL remains worse than weighted/shift-aware experts. This suggests the gate objective should be ECE/risk-aware, not sample NLL only.

### Leave-One-Class-Out, MVTec Only

| Method | ECE | Brier | NLL | AUROC |
|---|---:|---:|---:|---:|
| oracle_sample_best_nll | 0.2976 | 0.2760 | 1.7140 | 0.8617 |
| sample_logistic_top1_nll | 0.3008 | 0.2910 | 1.9234 | 0.8617 |
| sample_sage_hier_t0.5 | 0.3017 | 0.2917 | 1.8818 | 0.8617 |
| sample_risk_margin_0.02 | 0.3017 | 0.2910 | 1.8676 | 0.8617 |

Interpretation: MVTec remains hard. Sample-level gating helps only slightly and does not create a strong new MVTec claim.

### Cross-Dataset: VisA -> MVTec

| Method | ECE | Brier | NLL | AUROC |
|---|---:|---:|---:|---:|
| oracle_sample_best_nll | 0.2976 | 0.2760 | 1.7140 | 0.8969 |
| sample_sage_hier_t0.6 | 0.2988 | 0.2906 | 1.8788 | 0.8969 |
| sample_risk_margin_0.02 | 0.2991 | 0.2886 | 2.1421 | 0.8969 |
| vector_platt | 0.3035 | 0.2949 | 1.8922 | 0.8969 |

Interpretation: conservative SAGE-style sample gate improves ECE slightly over Vector Platt under VisA -> MVTec transfer (`0.3035 -> 0.2988`). This is useful but not a strong standalone claim.

### Cross-Dataset: MVTec -> VisA

| Method | ECE | Brier | NLL | AUROC |
|---|---:|---:|---:|---:|
| sample_sage_hier_t0.5 | 0.2190 | 0.2204 | 1.4175 | 0.8712 |
| sample_sage_hier_t0.6 | 0.2214 | 0.2223 | 1.4452 | 0.8712 |
| sample_logistic_top1_nll | 0.2262 | 0.2256 | 1.3850 | 0.8712 |
| weighted_platt | 0.2305 | 0.2312 | 1.1305 | 0.8712 |
| shift_aware_vector_platt | 0.2317 | 0.2297 | 1.1230 | 0.8712 |

Interpretation: this is the strongest sample-level signal. MVTec-trained hierarchical gate transfers to VisA and improves ECE over weighted/shift-aware/vector-like experts. However, NLL is worse than weighted/shift-aware, so the paper should frame this as ECE/risk calibration rather than likelihood optimization.

## Conclusion

Sample-level gate is promising but not yet a decisive main claim.

What it supports:

> SAGE-style shared/dynamic sample routing can improve ECE under cross-dataset shift, especially MVTec -> VisA, while preserving the frozen DINOv2 subspace ranking.

What it does not yet support:

- universal improvement;
- strong MVTec-only improvement;
- claim that sample-level gate dominates all metrics;
- final deployed method without a better ECE-aware training objective.

## Next Step

The next most valuable improvement is to train the sample gate with a direct calibration objective or differentiable soft-ECE/Brier objective instead of sample-level NLL oracle labels. Current NLL-target routing sometimes improves ECE but harms NLL/Brier, meaning the training target is misaligned with the paper claim.

## Brier/No-Harm Mixture Gate Update

After adding direct Brier/no-harm mixture gates, representative evaluation was rerun from existing per-image predictions. Evaluation rows increased from `126` to `162`.

New methods:

- `sample_brier_mix`: soft mixture gate trained directly on Brier.
- `sample_brier_anchor_reg`: Brier plus anchor regularization toward Vector Platt.
- `sample_brier_noharm`: Brier plus no-harm penalty when mixed probability is worse than anchor per sample.
- `sample_brier_noharm_anchor`: combined no-harm and anchor regularization.

Main result: these gates do not beat the best hierarchical gate on ECE.

| Split | Best Brier/no-harm mixture | ECE | Best previous gate | ECE |
|---|---|---:|---|---:|
| LOCO all | `sample_brier_mix` | 0.2615 | `sample_logistic_top1_nll` | 0.2581 |
| LOCO VisA | `sample_brier_mix` | 0.2335 | `sample_logistic_top1_nll` | 0.2305 |
| LOCO MVTec | `sample_brier_noharm` | 0.3029 | `sample_logistic_top1_nll` | 0.3008 |
| VisA -> MVTec | `sample_brier_noharm` | 0.3025 | `sample_sage_hier_t0.6` | 0.2988 |
| MVTec -> VisA | best mixture not in top group | >0.2317 | `sample_sage_hier_t0.5` | 0.2190 |

Interpretation:

- Brier/no-harm mixture is more conservative and often gives more anchor weight, e.g. MVTec LOCO anchor weight around `0.85`.
- It does not optimize ECE well enough. Brier is a proper scoring rule, but the paper claim is reliability/ECE under shift, so Brier-only training is misaligned.
- The previous SAGE-style hierarchical shared/dynamic gate remains the best sample-level candidate.

Updated conclusion:

> Sample-level SAGE routing is promising, but direct Brier/no-harm mixture is not enough. The next serious step is differentiable ECE/risk-coverage/selective calibration, or a validation-class objective that optimizes group ECE rather than per-sample Brier/NLL.

