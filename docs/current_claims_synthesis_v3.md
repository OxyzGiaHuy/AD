# 2026-07-11 Addendum: từ CRR-ECE sang operational reliability

Audit mới cho thấy CRR không nên được bảo vệ chủ yếu bằng ECE của 1 - conformal p-value. Stress test prevalence làm ECE và thứ hạng calibrator thay đổi mạnh; matched LOIO cũng tăng FAR nhiều hơn power. Claim chắc hơn là low-storage decoupled detector cung cấp ranking ổn định, còn reliability layer phải được đánh giá bằng attainable alpha, normal FAR, anomaly power và risk-coverage.

Hướng mới SC3R dùng support-normalized residual, cross-category normal archive và source-class-validated threshold. Pilot matched-condition MVTec k4 mở được alpha 0.05/0.10 với mean FAR 0.044/0.076 và power 0.120/0.307, trong khi target-only p-value không thể biểu diễn alpha dưới 1/(k+1)=0.2. Đây là candidate novelty, chưa phải claim chốt vì Gaussian/JPEG chưa đạt no-harm theo từng cell và sampling representative cũ cần stratified rerun.

# Tổng Hợp Claim Hiện Tại Sau Toàn Bộ Experiment

Tài liệu này là bản tổng hợp mới nhất sau các vòng benchmark MVTec, VisA, transfer, calibration, robustness, PCA128, official SubspaceAD check, và Shift-Aware Calibration dưới corruption shift. Mục tiêu là giải thích bằng tiếng Việt, theo flow dễ hiểu, rằng hiện tại paper nên claim gì, dựa trên evidence nào, và không nên claim gì.

## 1. Một Câu Tóm Tắt Claim Hiện Tại

Claim mạnh nhất hiện tại không còn là “thắng SOTA AUROC”. Claim tốt hơn, sắc hơn và defensible hơn là:

> Một detector few-shot anomaly detection dựa trên frozen DINOv2 + subspace/PCA residual có thể đạt AUROC cạnh tranh với storage rất thấp; khi tách ranking và calibration, Shift-Aware Vector Calibration cải thiện độ tin cậy xác suất dưới structured/domain shift như blur, brightness/contrast, và JPEG, trong khi vẫn giữ nguyên ranking anomaly.

Nói gọn hơn cho paper:

> **Low-storage calibrated subspace anomaly detection with shift-aware reliability under structured corruptions.**

Đây là framing hiện tại:

- **Efficiency**: ít storage hơn memory-bank methods.
- **Calibration**: probability đáng tin hơn, nhất là k lớn và dưới structured shift.
- **Transfer/Robustness Diagnostics**: benchmark chỉ ra khi nào method ổn, khi nào fail.
- **Không claim pure SOTA AUROC**: vì MVTec và official SubspaceAD rất mạnh.

## 2. Bài Toán Và Vì Sao Claim Này Có Ý Nghĩa

Few-shot industrial anomaly detection nghĩa là mỗi category chỉ có rất ít ảnh normal, thường k = 1, 2, 4, 8. Không có hoặc gần như không có anomaly labels để train supervised đầy đủ. Bài toán khó vì anomaly hiếm, đa dạng, và test-time defect có thể khác rất xa synthetic anomaly.

Các method memory-bank như PatchCore/AnomalyDINO lưu nhiều patch features normal rồi dùng nearest neighbor để chấm anomaly. Cách này mạnh nhưng storage và inference cost tăng theo số support patches.

Subspace/PCA residual đi theo hướng khác: học một không gian con của normal patches. Patch nào lệch khỏi normal subspace thì residual cao, có khả năng anomaly. Cách này rẻ hơn memory bank vì chỉ lưu PCA mean/components, không lưu toàn bộ bank patch features.

Điểm mới trong hướng hiện tại không phải “DINOv2 + PCA” đơn thuần. SubspaceAD đã làm việc đó. Điểm mới nên nhấn là:

- giữ **PCA/subspace residual** làm ranking anomaly;
- dùng head/calibrator để biến raw score thành probability đáng tin hơn;
- thêm **Shift-Aware Calibration** để probability biết khi input đang bị structured shift;
- benchmark đầy đủ clean, storage, calibration, transfer, pixel, corruption, FGSM.

## 3. Method Hiện Tại Theo Flow

### 3.1 Frozen DINOv2 Feature

Ảnh được đưa qua frozen DINOv2 ViT-S/14 để lấy patch features. Backbone không fine-tune trong baseline chính. Điều này giúp benchmark gọn và giảm overfit trong few-shot.

### 3.2 PCA/Subspace Residual Là Ranking Chính

Với k ảnh normal support, ta fit PCA trên patch features normal. Khi test:

- mỗi patch được reconstruct qua PCA subspace;
- residual càng cao nghĩa là patch càng lệch khỏi normal manifold;
- image score là max patch residual.

Đây là `raw_anomaly_score` dùng để xếp hạng anomaly. Ranking này quyết định AUROC/AP.

### 3.3 Decoupled Calibration

Thay vì trộn trực tiếp head score với PCA score để tạo ranking, method hiện tại tách hai việc:

- **ranking**: dùng PCA/subspace residual;
- **calibration**: dùng vector Platt để map score/features thành probability.

Vector Platt nhận các feature như:

- `pca_score`: image-level PCA residual;
- `head_score`: score từ synthetic anomaly head;
- `disagreement`: độ lệch giữa PCA score và head score.

Ý nghĩa: head không cần thắng PCA về ranking. Head chỉ cần cung cấp tín hiệu phụ để calibrator biết score này đáng tin đến đâu.

### 3.4 Shift-Aware Calibration

Shift-Aware Calibration mở rộng vector Platt bằng các shift descriptors, ví dụ:

- norm distance của features so với normal support center;
- mean/std/max concentration của PCA residual;
- dấu hiệu score bị tập trung bất thường hay phân tán bất thường.

Điều quan trọng: Shift-Aware không đổi `raw_anomaly_score`. Vì vậy AUROC/AP giữ nguyên. Nó chỉ đổi `calibrated_probability`, tức xác suất anomaly sau calibration.

Nói cách khác:

> Shift-Aware không làm model “xếp hạng anomaly tốt hơn”; nó làm model “nói xác suất đáng tin hơn” khi ảnh bị shift.

## 4. Kết Quả Clean: Method Cạnh Tranh Nhưng Không SOTA MVTec

### 4.1 MVTec Clean

`calib_subspace_head` đạt AUROC cạnh tranh nhưng không thắng PatchCore/AnomalyDINO toàn diện:

| k | calib_subspace_head AUROC | PatchCore/AnomalyDINO AUROC |
| ---: | ---: | ---: |
| 1 | `0.9038` | `0.9143` |
| 4 | `0.9371` | `0.9418` |
| 8 | `0.9452` | `0.9484` |

Do đó không nên claim “SOTA on MVTec”. Claim đúng là:

> competitive MVTec AUROC with much lower storage and better calibration.

### 4.2 VisA Clean

VisA cho kết quả thuận lợi hơn. `calib_subspace_head` vượt PatchCore/AnomalyDINO trong benchmark hiện tại:

| k | calib_subspace_head AUROC | PatchCore/AnomalyDINO AUROC |
| ---: | ---: | ---: |
| 1 | `0.8226` | `0.8038` |
| 2 | `0.8534` | `0.8387` |
| 4 | `0.8696` | `0.8619` |
| 8 | `0.8796` | `0.8729` |

Claim nên viết cẩn thận:

> stronger VisA clean AUROC in our benchmark protocol.

Không viết thành “universal SOTA”.

## 5. Efficiency: Low-Storage Là Claim Rất Mạnh

Storage là nơi method có câu chuyện rõ:

- `calib_subspace_head`: khoảng `0.472 MB`.
- PCA128 setting: khoảng `0.566 MB`.
- PatchCore/AnomalyDINO trong benchmark hiện tại: khoảng `2 MB` đến `6 MB`.

PCA128 trên full VisA tăng AUROC nhưng storage vẫn thấp:

| k | PCA64 AUROC | PCA128 AUROC | Delta |
| ---: | ---: | ---: | ---: |
| 1 | `0.8226` | `0.8335` | `+0.0110` |
| 2 | `0.8534` | `0.8684` | `+0.0150` |
| 4 | `0.8696` | `0.8852` | `+0.0156` |
| 8 | `0.8796` | `0.8967` | `+0.0171` |

Ý nghĩa:

> Có thể tăng số PCA components để cải thiện AUROC trên VisA mà storage vẫn dưới `0.6 MB`, thấp hơn nhiều so với memory-bank.

Đây là claim accuracy-storage tradeoff rất tốt.

## 6. Calibration: Vì Sao Đây Là Claim Chính

Calibration trong bài này nghĩa là: khi model nói probability anomaly là 0.8, thì trong nhóm sample có probability gần 0.8, khoảng 80% thật sự nên là anomaly. Đây khác với AUROC.

- AUROC đo ranking: anomaly có score cao hơn normal không?
- ECE/Brier/NLL đo probability: xác suất có đáng tin không?

Vector Platt giúp calibration tốt hơn scalar/raw. Trên MVTec:

- Vector Platt ECE k8: `0.1538`.
- Scalar Platt/SubspaceAD ECE k8: `0.3097`.

Điểm cần nhấn:

> Head/calibrator hữu ích cho probability reliability, không nhất thiết hữu ích cho raw ranking.

Đây là lý do decoupling quan trọng. Nếu trộn head score trực tiếp vào ranking, AUROC có thể giảm. Nếu dùng head score làm calibration feature, reliability cải thiện mà ranking PCA vẫn giữ ổn.

## 7. Shift-Aware Calibration: Claim Mạnh Nhất Hiện Tại

### 7.1 Shift-Aware Clean VisA

Trên full VisA clean, Shift-Aware cải thiện ECE mạnh ở k4/k8:

| k | Vector Platt ECE | Shift-Aware ECE | Kết luận |
| ---: | ---: | ---: | --- |
| 1 | `0.4295` | `0.4320` | hơi tệ hơn |
| 2 | `0.3780` | `0.3768` | gần hòa |
| 4 | `0.2839` | `0.2032` | tốt hơn rõ |
| 8 | `0.2066` | `0.1447` | tốt hơn rõ |

NLL giảm ở mọi k:

- k1: `4.3117 -> 4.0028`
- k2: `2.4165 -> 1.9310`
- k4: `1.3818 -> 0.8226`
- k8: `0.8597 -> 0.5487`

Kết luận:

> Shift-Aware hữu ích nhất khi có đủ support normal hơn, đặc biệt k4/k8. Low-shot k1 vẫn khó.

### 7.2 Shift-Aware Dưới Corruption Shift

Full VisA corruption grid đã chạy xong `960/960` rows: 12 classes, k `{4,8}`, 5 seeds, 4 corruptions.

AUROC/AP không đổi, đúng thiết kế. Điểm cải thiện nằm ở calibration.

ECE dưới structured corruptions:

| Corruption | k | Vector ECE | Shift-Aware ECE | Delta |
| --- | ---: | ---: | ---: | ---: |
| blur | 4 | `0.2844` | `0.2111` | `-0.0733` |
| blur | 8 | `0.2078` | `0.1439` | `-0.0640` |
| brightness/contrast | 4 | `0.2845` | `0.2118` | `-0.0727` |
| brightness/contrast | 8 | `0.2086` | `0.1532` | `-0.0554` |
| JPEG | 4 | `0.2876` | `0.2297` | `-0.0579` |
| JPEG | 8 | `0.2119` | `0.1564` | `-0.0554` |

Gaussian noise là caveat:

| Corruption | k | Vector ECE | Shift-Aware ECE | Delta |
| --- | ---: | ---: | ---: | ---: |
| Gaussian noise | 4 | `0.2695` | `0.2762` | `+0.0067` |
| Gaussian noise | 8 | `0.1900` | `0.1913` | `+0.0013` |

NLL vẫn giảm nhẹ cho Gaussian noise, nhưng ECE/Brier không cải thiện.

Claim chính nên viết:

> Shift-Aware Vector Calibration improves probability reliability under structured corruption/domain shift such as blur, brightness/contrast, and JPEG compression while preserving PCA/subspace ranking; it is not a universal fix for additive Gaussian noise.

Đây là claim đẹp vì:

- có positive result rõ;
- có failure mode rõ;
- không overclaim robustness;
- novelty nằm ở reliability dưới structured shift trong few-shot industrial AD.

## 8. Transfer Calibration: Dataset Shift Là Khó Nhưng Có Tín Hiệu

MVTec to VisA transfer dùng calibrator fit/tune từ MVTec, sang VisA không dùng anomaly labels cho main calibration.

AUROC tăng theo k:

- k1: `0.8226`
- k2: `0.8534`
- k4: `0.8696`
- k8: `0.8824`

ECE giảm theo k nhưng vẫn cao ở low-shot:

- k1: `0.4319`
- k2: `0.3905`
- k4: `0.3140`
- k8: `0.2324`

Claim:

> Transfer ranking works reasonably, but calibration remains difficult under low-shot dataset shift.

Điều này support thêm cho câu chuyện Shift-Aware: calibration under shift là vấn đề thật và cần cơ chế riêng.

## 9. Pixel Metrics: Điểm Hỗ Trợ Cho Subspace Ranking

MVTec pixel AUROC của `calib_subspace_head` rất cạnh tranh:

| k | calib_subspace_head pixel AUROC | PatchCore/AnomalyDINO pixel AUROC |
| ---: | ---: | ---: |
| 1 | `0.9436` | `0.9402` |
| 2 | `0.9525` | `0.9466` |
| 4 | `0.9567` | `0.9507` |
| 8 | `0.9599` | `0.9516` |

Điều này giúp bảo vệ lựa chọn giữ PCA/subspace residual làm ranking chính. Ranking subspace không chỉ nhẹ mà còn cho pixel localization tốt trong benchmark hiện tại.

Tuy vậy, official SubspaceAD representative cũng rất mạnh, nên không claim “PCA ranking mới”. Claim nên là:

> subspace ranking is a strong low-storage backbone for calibrated reliability.

## 10. Robustness/FGSM: Không Claim Robust

FGSM sweep cho thấy fragility mạnh. Có cả hiện tượng non-monotonic theo epsilon, nên cần viết cẩn thận:

- không claim adversarially robust;
- không claim đã solve robustness;
- chỉ claim benchmark/diagnostic chỉ ra failure mode.

Câu nên dùng:

> Robustness experiments expose severe adversarial fragility and motivate reliability diagnostics; they are not evidence of adversarial robustness.

## 11. Novelty Guardrails

Các work đã phủ một phần quan trọng:

- AnomalyDINO: frozen DINOv2 + memory-bank few-shot AD.
- SubspaceAD: frozen DINOv2 + PCA/subspace residual.
- Khan & Krawczyk 2025: calibration/ECE/Platt scaling/FGSM fragility cho DINOv2-based few-shot AD.
- Calibration under distribution shift: đã là hướng rộng trong ML/CV.

Vì vậy không claim:

- first DINOv2 few-shot AD;
- first DINOv2 PCA/subspace;
- first calibration benchmark;
- first robust calibration under shift;
- SOTA MVTec AUROC;
- adversarial robustness.

Novelty còn lại, nhưng đủ sắc:

> task-specific decoupled calibrated subspace detector with shift-aware vector calibration, evaluated under clean, transfer, corruption, pixel, efficiency, and adversarial diagnostic protocols for few-shot industrial anomaly detection.

## 12. Claim Paper Nên Đưa Vào

### Main Claim

> We propose a low-storage decoupled calibrated subspace detector for few-shot industrial anomaly detection, where PCA/subspace residuals provide anomaly ranking and vector/shift-aware calibration provides reliable probabilities under dataset and structured corruption shifts.

### Claim 1: Low-Storage Competitive Detector

Evidence:

- MVTec AUROC competitive: k8 `0.9452` vs memory-bank `0.9484`.
- Storage: `0.472 MB` to `0.566 MB`, lower than memory-bank `2-6 MB`.
- VisA AUROC strong: PCA128 k8 `0.8967`.

### Claim 2: Decoupling Ranking And Calibration Matters

Evidence:

- PCA/subspace residual remains ranking score.
- Vector Platt improves ECE without changing ranking.
- Direct mixing head score is risky for AUROC; head is better as calibration evidence.

### Claim 3: Shift-Aware Calibration Helps Structured Shift

Evidence:

- Full VisA clean k4/k8 ECE improves: `0.2839 -> 0.2032`, `0.2066 -> 0.1447`.
- Corruption ECE improves for blur, brightness/contrast, JPEG by roughly `0.055` to `0.073`.
- AUROC/AP unchanged by design.

### Claim 4: Honest Robustness Diagnostics

Evidence:

- Gaussian noise caveat: Shift-Aware does not improve ECE.
- FGSM collapse: method is not adversarially robust.
- This makes the benchmark valuable as diagnostic, not as inflated robustness claim.

## 13. Câu Chuyện Paper Nên Viết

Một story mạch lạc có thể là:

1. Few-shot industrial AD hiện có memory-bank methods mạnh nhưng storage-heavy và raw scores poorly calibrated.
2. Subspace residual trên frozen DINOv2 là low-storage ranking backbone rất mạnh, nhưng raw score/probability reliability vẫn là vấn đề.
3. Thay vì train/fine-tune backbone hoặc trộn head vào ranking, ta decouple ranking and calibration.
4. Vector calibrator dùng subspace score, head score, disagreement để cải thiện calibration.
5. Shift-Aware calibrator thêm shift descriptors, giúp probability reliability tốt hơn dưới structured corruptions.
6. Kết quả cho thấy method không phải SOTA MVTec AUROC, không adversarially robust, nhưng là một calibrated low-storage alternative với evidence rõ về structured-shift reliability.

## 14. Những Câu Không Nên Viết

Không viết:

- “Our method achieves SOTA on MVTec.”
- “We are the first to use DINOv2 PCA for anomaly detection.”
- “We are the first calibration benchmark for DINOv2 anomaly detection.”
- “Our method is adversarially robust.”
- “Shift-Aware improves all corruptions.”
- “Shift-Aware improves AUROC.”

Nên viết:

- “competitive AUROC with lower storage.”
- “probability reliability improves under structured shifts.”
- “ranking and calibration are decoupled.”
- “Gaussian noise remains a limitation.”
- “FGSM exposes fragility rather than solved robustness.”

## 15. Kết Luận Ngắn Cho Thầy/Paper

Sau nhiều vòng experiment, claim ban đầu đã được chỉnh từ “trainable head beats memory-bank and is robust” thành claim chắc hơn:

> Method là một low-storage calibrated subspace detector. Nó không thắng toàn diện MVTec AUROC, nhưng cạnh tranh tốt, rất nhẹ, có pixel ranking mạnh, cải thiện calibration trên VisA/structured corruptions, và cung cấp benchmark transfer/robustness diagnostics rõ ràng.

Điểm đáng đẩy nhất cho paper hiện tại là:

> **Shift-Aware Calibration under structured corruption/domain shift for low-storage few-shot industrial anomaly detection.**

Đây là claim không quá rộng, có số liệu full-grid support, có novelty guardrail rõ, và có limitation trung thực.


## Update: Full Gated Shift-Aware Calibration

Full VisA and full MVTec results refine the Gated Shift-Aware claim. The strongest defensible claim is no longer "universal improvement". It is:

> A SAGE-inspired anchored/gated calibration layer makes shift-aware calibration safer under dataset shift: it improves calibration clearly on VisA, stays near a strong Vector Platt baseline on MVTec, and exposes when direct shift-aware/weighted experts over-adapt.

Evidence:

- Full VisA k4/k8 seeds 0-2: `anchored_soft_gate_adaptive` improves ECE `0.2497 -> 0.2352` with no-harm `16/16`; `anchored_structured_gate_adaptive` improves to `0.2258` with no-harm `16/16`.
- Full MVTec k4/k8 seeds 0-2: Vector Platt is already strong (`0.1952` ECE). `anchored_structured_gate` is near-tied (`0.1954`) while direct `shift_aware_vector_platt` worsens to `0.2164` and `weighted_platt` to `0.2169`.
- MVTec shows the main reason to gate: direct shift-aware/weighted experts are unsafe across classes/corruptions, while anchored gates recover near-baseline behavior without changing AUROC/AP.
- Oracle best on MVTec is `0.1853`, leaving room for a learned class-held-out gate, but current evidence is not enough to claim universal superiority over Vector Platt.

This update does not replace the prior low-storage calibrated subspace detector claim; it strengthens the calibration-under-shift contribution and adds an honest limitation: gains are dataset-conditional.

## Update: SAGE-Style Learned/Risk-Aware Gate

New offline experiments test three SAGE-inspired gate variants on full VisA+MVTec detailed metrics: class-held-out logistic routing, risk-aware margin routing, and hierarchical shared/dynamic routing. The result strengthens the Gated direction but also clarifies the limitation.

Evidence:

- Leave-one-class-out over `648` cases: `risk_aware_margin_0.01` improves mean ECE by about `-0.022` vs Vector Platt.
- Cross MVTec -> VisA: risk-aware/view gate improves ECE by about `-0.016`.
- Cross VisA -> MVTec: learned gates can still over-adapt; conservative SAGE-style hierarchical routing keeps harm small, about `+0.0011` ECE for calibrator experts.
- Adding a non-calibrator `anchored_structured_gate` view helps some transfer settings, suggesting experts should be reliability views rather than only calibrator types.

Claim update:

> SAGE-inspired reliability routing is promising: a shared safe anchor plus dynamic shift/density/anchored views improves class-held-out calibration and exposes when cross-dataset routing must be conservative.

Caveat: this is currently offline case-level evidence. It should become a sample-level gate before being presented as the final deployed method.


## 2026-07-09 Addendum: Claim Shift Toward Conformal Reliability Routing

After testing validation-ECE gates, selective reliability, and SW-CAD conformal views, the strongest current claim is no longer calibrator-only Gated Shift-Aware Calibration. The strongest direction is:

> Low-storage decoupled DINOv2 subspace AD with LOIO conformal reliability routing.

Representative evidence:

- `fixed_conformal_loio` improves ECE from Vector Platt by about `-0.2028` on MVTec -> VisA, `-0.2016` on VisA -> MVTec, `-0.1883` on LOCO, and `-0.2068` on within split.
- `no_label_shift_or_neff_gate` is weaker but still improves ECE without observed harm in reported split groups, supporting a practical no-label fallback.
- Selective reliability with conformal views reduces ECE at 80% coverage by about `40.9%` overall, `49.7%` on VisA, and `64.6%` on MVTec in the representative benchmark.

This makes SW-CAD/conformal views more than a diagnostic supplement: they are now a candidate main reliability contribution. The remaining paper risk is scale: full VisA/MVTec confirmation is needed before using this as the dominant Q1 claim.

## 2026-07-11 Addendum: False-Alarm Claim Strength

The newest P1/P2 results clarify the role of conformal p-values. Full VisA supports CRR as a strong calibration contribution. MVTec representative supports CRR as an interpretable reliability/operating-point layer, but not yet as a strict false-alarm-control guarantee.

Claim strength by component:

- Strong: low-storage decoupled detector; PCA/subspace ranking kept separate from calibration/reliability.
- Strong: full VisA calibration under corruption shift; LOIO conformal has much lower ECE than Vector/Shift-Aware Platt.
- Medium: MVTec representative conformal p-values give useful false-alarm/detection tradeoffs. LOIO alpha `0.20` has false-alarm `0.1057` and precision `0.8680`; alpha `0.25` detects most anomalies but false-alarm rises to `0.3337`.
- Weak/supporting: weighted conformal as a detector. It is conservative and better framed as a safe diagnostic view.

Recommended paper framing:

> Conformal reliability routing improves probability reliability and exposes controllable operating tradeoffs, but formal false-alarm guarantees under dataset/corruption shift require additional threshold calibration or randomized conformal p-values.
# Historical synthesis — superseded

This document predates the Neurocomputing statistical audit. References to a
“safe anchor,” universal routing, or historical gates are development notes,
not final evidence. See `neurocomputing_claim_audit.md` and
`sc3r_formal_specification.md`.

