# Gated Shift-Aware Calibration: Full VisA/MVTec Update

## Mục tiêu

Sau các kết quả trước đó, Shift-Aware Calibration có tín hiệu mạnh trên VisA nhưng không ổn định trên MVTec. Mục tiêu mới là làm cơ chế gated đủ an toàn để kiểm tra claim cross-dataset: giữ được lợi ích dưới structured shift khi có tín hiệu, nhưng fallback về Vector Platt khi shift-aware/weighted expert có nguy cơ làm calibration tệ hơn.

Claim nền vẫn giữ nguyên:

- Ranking chính là low-storage DINOv2 PCA/subspace residual.
- Calibration không thay AUROC/AP vì không thay ranking.
- Contribution chính vẫn là calibration + efficiency + transfer/robustness diagnostics.
- Không claim SOTA MVTec AUROC hoặc adversarial robustness.

## Method mới: Anchored No-Harm Gated Calibration

Thay vì trộn experts trực tiếp, dùng Vector Platt làm anchor an toàn:

```text
p_final = p_vector + lambda(x) * (p_expert_mix - p_vector)
```

Trong đó:

- `p_vector`: Vector Platt gốc trên `[subspace_score, head_score, disagreement]`.
- `p_expert_mix`: mixture của shift-aware và weighted experts.
- `lambda(x)`: strength từ shift descriptors, gồm domain confidence, effective sample size ratio, và PCA residual concentration.

Ý tưởng lấy cảm hứng từ SAGE ở mức nguyên lý: routing/gating chọn mức độ dùng expert theo input/domain condition. Khác SAGE, gate ở đây nằm ở calibration layer, không phải segmentation decoder.

## Variants đã test

- `vector_platt`: baseline an toàn.
- `shift_aware_vector_platt`: shift descriptors trực tiếp trong Vector Platt.
- `weighted_platt`: density-ratio weighted calibration.
- `soft_neff_gate`: soft expert mixture không anchor.
- `structured_rule_gate`: hard gate theo corruption label, diagnostic/upper heuristic, không phải deployment claim chính.
- `anchored_soft_gate`: conservative anchor, `lambda` bị scale 0.35.
- `anchored_soft_gate_adaptive`: adaptive anchor, dùng full descriptor strength.
- `anchored_structured_gate_adaptive`: stronger but uses corruption-type rule; useful for analysis, weaker as deployable claim.

## Representative results

Grid:

- VisA: classes `{candle, cashew, pcb1, pipe_fryum}`, k `{4,8}`, seeds `{0,1,2}`, corruptions `{gaussian_noise, blur, brightness_contrast, jpeg}`.
- MVTec: classes `{bottle, cable, hazelnut}`, k `{4,8}`, seeds `{0,1,2}`, same corruptions.

### VisA

| Method | Mean ECE | Worst ECE | Mean AUROC | No-harm vs Vector |
|---|---:|---:|---:|---:|
| vector_platt | 0.2711 | 0.3239 | 0.9035 | - |
| shift_aware_vector_platt | 0.2240 | 0.3115 | 0.9035 | 7/8 |
| weighted_platt | 0.2247 | 0.3115 | 0.9035 | 7/8 |
| soft_neff_gate | 0.2479 | 0.3054 | 0.9035 | 8/8 |
| anchored_soft_gate | 0.2668 | 0.3203 | 0.9035 | 8/8 |
| anchored_soft_gate_adaptive | 0.2597 | 0.3134 | 0.9035 | 8/8 |
| anchored_structured_gate_adaptive | 0.2468 | 0.3053 | 0.9035 | 8/8 |
| oracle_best | 0.2114 | 0.2879 | 0.9035 | 8/8 |

### MVTec

| Method | Mean ECE | Worst ECE | Mean AUROC | No-harm vs Vector |
|---|---:|---:|---:|---:|
| vector_platt | 0.2562 | 0.3063 | 0.8915 | - |
| shift_aware_vector_platt | 0.2857 | 0.3296 | 0.8915 | 0/8 |
| weighted_platt | 0.2862 | 0.3296 | 0.8915 | 0/8 |
| soft_neff_gate | 0.2654 | 0.3168 | 0.8915 | 4/8 |
| anchored_soft_gate | 0.2572 | 0.3085 | 0.8915 | 8/8 |
| anchored_soft_gate_adaptive | 0.2598 | 0.3119 | 0.8915 | 8/8 |
| anchored_structured_gate_adaptive | 0.2615 | 0.3107 | 0.8915 | 7/8 |
| oracle_best | 0.2509 | 0.3063 | 0.8915 | 8/8 |

## Interpretation

- Direct shift-aware and weighted calibration are strong on VisA but fail badly on MVTec.
- Anchoring converts shift-aware calibration from a risky expert into a no-harm correction.
- `anchored_soft_gate_adaptive` is the best deployable candidate so far:
  - no-harm `8/8` on VisA;
  - no-harm `8/8` on MVTec;
  - improves VisA mean ECE by `0.0114` absolute vs Vector Platt;
  - only changes MVTec by `+0.0036` ECE, inside the no-harm tolerance of `0.01`;
  - preserves AUROC/AP because ranking is unchanged.
- `anchored_structured_gate_adaptive` gives stronger VisA gain, but it uses corruption-type routing and has `7/8` no-harm on MVTec, so it should be reported as diagnostic/upper heuristic rather than main deployable method.


## Full MVTec k4/k8 seeds 0-2 update

Completed full MVTec grid: 15 classes, k `{4,8}`, seeds `{0,1,2}`, corruptions `{gaussian_noise, blur, brightness_contrast, jpeg}` = `360/360` cases.

Summary over all class/k/seed/corruption cases:

| Method | Mean ECE | Worst ECE | Mean AUROC | No-harm vs Vector |
|---|---:|---:|---:|---:|
| vector_platt | 0.1952 | 0.5348 | 0.9126 | - |
| shift_aware_vector_platt | 0.2164 | 0.5961 | 0.9126 | 92/360 |
| weighted_platt | 0.2169 | 0.5961 | 0.9126 | 91/360 |
| soft_neff_gate | 0.2010 | 0.5503 | 0.9126 | 114/360 |
| anchored_soft_gate | 0.1960 | 0.5363 | 0.9126 | 121/360 |
| anchored_structured_gate | 0.1954 | 0.5398 | 0.9126 | 199/360 |
| anchored_structured_gate_adaptive | 0.1970 | 0.5491 | 0.9126 | 198/360 |
| oracle_best | 0.1853 | 0.5348 | 0.9126 | 360/360 |

By corruption, selected methods:

| Method | Blur ECE | Brightness/Contrast ECE | Gaussian Noise ECE | JPEG ECE |
|---|---:|---:|---:|---:|
| vector_platt | 0.1808 | 0.1842 | 0.2085 | 0.2072 |
| anchored_structured_gate | 0.1799 | 0.1836 | 0.2085 | 0.2095 |
| shift_aware_vector_platt | 0.1882 | 0.1914 | 0.2561 | 0.2300 |
| oracle_best | 0.1645 | 0.1705 | 0.2065 | 0.1996 |

By k-shot:

| Method | k4 ECE | k8 ECE |
|---|---:|---:|
| vector_platt | 0.2232 | 0.1672 |
| anchored_structured_gate | 0.2241 | 0.1667 |
| shift_aware_vector_platt | 0.2408 | 0.1920 |
| oracle_best | 0.2178 | 0.1528 |

Interpretation:

- Full MVTec does not support a universal-improvement claim over Vector Platt.
- Vector Platt is already a very strong calibration baseline on MVTec.
- Direct shift-aware and weighted experts are clearly unsafe on MVTec: mean ECE worsens from `0.1952` to about `0.216-0.217`, and no-harm is only about `25%`.
- Anchored/gated variants recover near-baseline behavior: `anchored_structured_gate` is almost tied with Vector Platt (`0.1954` vs `0.1952`) and slightly better on blur/brightness, but slightly worse on JPEG.
- The oracle gap remains meaningful (`0.1952 -> 0.1853`), so there is still room for a learned or class-held-out gate.

## Current claim update

Safe claim:

> A SAGE-inspired anchored/gated calibration layer turns shift-aware calibration from a risky universal correction into a dataset-conditional safe routing mechanism: it improves calibration clearly on VisA, stays near a strong Vector Platt baseline on MVTec, and exposes when direct shift-aware/weighted experts over-adapt under distribution shift.

Stronger but still careful claim:

> Dynamic calibration routing is necessary for reliable shift-aware calibration: direct shift-aware/weighted Platt improves VisA but fails on MVTec, while anchored gating recovers near-baseline behavior and preserves ranking.

Do not claim yet:

- universal improvement over Vector Platt on every dataset;
- SOTA AUROC;
- adversarial robustness;
- first gated expert anomaly detection;
- direct reuse/copy of SAGE architecture.

## Next experiments

1. Add held-out class/domain gate validation: tune gate strength on some classes and test on unseen classes.
2. Compare with a learned logistic gate trained only on synthetic corruptions/normal support.
3. Add descriptor ablation: no `n_eff`, no domain confidence, no concentration, no anchor.
4. Report VisA and MVTec separately: VisA supports calibration improvement; MVTec supports safe-routing/over-adaptation diagnostics.
5. Avoid "universal improvement" wording unless a learned gate closes the MVTec oracle gap.


## Full VisA k4/k8 seeds 0-2 update

Completed full VisA grid for anchored adaptive gated calibration: 12 classes, k `{4,8}`, seeds `{0,1,2}`, corruptions `{gaussian_noise, blur, brightness_contrast, jpeg}` = `288/288` cases.

Summary over dataset/corruption/k groups:

| Method | Mean ECE | Worst ECE | Mean AUROC | No-harm vs Vector |
|---|---:|---:|---:|---:|
| vector_platt | 0.2497 | 0.3166 | 0.8938 | - |
| shift_aware_vector_platt | 0.2179 | 0.3256 | 0.8938 | 15/16 |
| weighted_platt | 0.2172 | 0.3257 | 0.8938 | 15/16 |
| soft_neff_gate | 0.2249 | 0.3166 | 0.8938 | 16/16 |
| anchored_soft_gate | 0.2440 | 0.3166 | 0.8938 | 16/16 |
| anchored_soft_gate_adaptive | 0.2352 | 0.3166 | 0.8938 | 16/16 |
| anchored_structured_gate_adaptive | 0.2258 | 0.3166 | 0.8938 | 16/16 |
| oracle_best | 0.2033 | 0.3158 | 0.8938 | 16/16 |

Interpretation:

- Full VisA confirms the representative finding: shift-aware/weighted calibration improves mean ECE but has a small no-harm failure (`15/16`).
- `anchored_soft_gate_adaptive` is the deployable no-harm candidate: mean ECE improves by `-0.0146` absolute vs Vector Platt with no-harm `16/16`.
- `anchored_structured_gate_adaptive` is stronger (`-0.0239` ECE) and still no-harm on full VisA, but it uses corruption-type routing, so keep it as diagnostic/upper heuristic unless the paper defines observable corruption labels at deployment.
- AUROC is unchanged by design because all gated methods preserve PCA/subspace ranking.
