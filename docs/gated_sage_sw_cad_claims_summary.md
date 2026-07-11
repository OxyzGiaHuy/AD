# Tổng Hợp Dễ Hiểu: Gated Từ SAGE, SW-CAD, Và Claim Hiện Tại

Date: 2026-07-09

## 1. Bối Cảnh Ban Đầu

Idea ban đầu của mình là xây dựng một method cho **few-shot industrial anomaly detection**:

- chỉ có rất ít ảnh normal, thường k = 1, 2, 4, 8;
- dùng frozen DINOv2 để lấy patch features;
- dùng PCA/subspace residual để detect anomaly;
- thêm calibration để raw anomaly score trở thành probability đáng tin hơn;
- benchmark thêm efficiency, calibration, robustness, transfer.

Claim ban đầu khá tham vọng:

> trainable head/adapter over frozen DINOv2 có thể thắng memory-bank methods về AUROC, rẻ hơn inference, calibrated hơn, và robust hơn.

Sau nhiều experiment, claim này đã được chỉnh lại cho trung thực hơn:

> low-storage DINOv2 subspace detector có AUROC cạnh tranh, storage thấp hơn memory bank, calibration tốt hơn trong một số setup, và cung cấp benchmark calibration/transfer/robustness rõ ràng.

Lý do phải chỉnh:

- MVTec AUROC không thắng toàn diện PatchCore/AnomalyDINO/SubspaceAD.
- DINOv2 + PCA/subspace residual không còn là novelty riêng vì gần với SubspaceAD.
- Calibration/FGSM đã có paper liên quan, nên không claim first calibration/robustness benchmark.
- Kết quả thật support mạnh hơn cho **Calibration + Efficiency + Diagnostics**, không phải pure AUROC SOTA.

## 2. Nhánh 1: Gated Shift-Aware Calibration Từ Ý Tưởng SAGE

### 2.1. SAGE là gì trong ngữ cảnh này?

Bài SAGE là về histopathology image segmentation. Nó không làm anomaly detection. Ý quan trọng mình lấy từ SAGE là:

- model không nên dùng cùng một processing path cho mọi input;
- có nhiều expert;
- router/gate quyết định input nào nên đi qua expert nào;
- có shared/safe path và dynamic expert path;
- có top-k expert routing.

Trong SAGE gốc:

- expert là các block CNN/Transformer;
- task là segmentation;
- gate hoạt động trong backbone/model architecture.

Trong task của mình:

- expert không phải CNN/Transformer block;
- expert là các **calibration/reliability views**;
- gate nằm sau detector, ở calibration layer;
- ranking anomaly vẫn giữ nguyên bằng PCA/subspace residual.

Vì vậy mình không copy SAGE architecture. Mình chỉ lấy nguyên lý:

> shared safe path + dynamic expert routing theo đặc điểm input/shift.

### 2.2. Expert ban đầu là calibrator

Lúc đầu mình tạo các expert dạng calibrator:

- `vector_platt`: baseline an toàn, dùng `[pca_score, head_score, disagreement]`.
- `shift_aware_vector_platt`: thêm shift descriptors vào calibration.
- `weighted_platt`: dùng density-ratio weights, lấy cảm hứng từ SW-CAD.

Kết quả:

- Trên VisA, shift-aware/weighted thường cải thiện ECE.
- Trên MVTec, shift-aware/weighted có thể làm calibration tệ hơn Vector Platt.

Điều này rất quan trọng: direct shift-aware không ổn định. Nó có thể over-adapt dưới dataset shift.

### 2.3. Anchored Gated Calibration

Để tránh over-adaptation, mình thêm anchor:

```text
p_final = p_vector + lambda(x) * (p_expert_mix - p_vector)
```

Ý nghĩa:

- `p_vector` là safe baseline.
- `p_expert_mix` là mixture của shift-aware/weighted expert.
- `lambda(x)` quyết định đi xa khỏi baseline bao nhiêu.

Nếu gate không chắc, output gần Vector Platt.
Nếu shift signal mạnh và đáng tin, output đi về expert.

### 2.4. Full VisA result

Full VisA k4/k8 seeds 0-2, 288 cases:

| Method | Mean ECE | Worst ECE | Mean AUROC | No-harm vs Vector |
|---|---:|---:|---:|---:|
| vector_platt | 0.2497 | 0.3166 | 0.8938 | - |
| shift_aware_vector_platt | 0.2179 | 0.3256 | 0.8938 | 15/16 |
| weighted_platt | 0.2172 | 0.3257 | 0.8938 | 15/16 |
| anchored_soft_gate_adaptive | 0.2352 | 0.3166 | 0.8938 | 16/16 |
| anchored_structured_gate_adaptive | 0.2258 | 0.3166 | 0.8938 | 16/16 |
| oracle_best | 0.2033 | 0.3158 | 0.8938 | 16/16 |

Kết luận VisA:

- shift-aware/weighted cải thiện ECE rõ;
- anchored gate giữ no-harm tốt hơn;
- AUROC không đổi vì ranking không đổi.

### 2.5. Full MVTec result

Full MVTec k4/k8 seeds 0-2, 360 cases:

| Method | Mean ECE | Worst ECE | Mean AUROC | No-harm vs Vector |
|---|---:|---:|---:|---:|
| vector_platt | 0.1952 | 0.5348 | 0.9126 | - |
| shift_aware_vector_platt | 0.2164 | 0.5961 | 0.9126 | 92/360 |
| weighted_platt | 0.2169 | 0.5961 | 0.9126 | 91/360 |
| anchored_structured_gate | 0.1954 | 0.5398 | 0.9126 | 199/360 |
| oracle_best | 0.1853 | 0.5348 | 0.9126 | 360/360 |

Kết luận MVTec:

- Vector Platt đã rất mạnh.
- Direct shift-aware/weighted làm tệ hơn.
- Anchored gate kéo performance về gần baseline.
- Không thể claim universal improvement.
- Có thể claim gate giúp tránh over-adaptation.

### 2.6. Offline SAGE-style gate

Sau đó mình thử 3 idea lấy cảm hứng sâu hơn từ SAGE:

1. `Class-Held-Out Learned Gate`: train trên class khác, test trên class unseen.
2. `Risk-Aware Gate`: chỉ rời Vector Platt nếu predicted gain đủ lớn.
3. `SAGE-Style Hierarchical Gate`: shared safe path trước, dynamic expert path sau.

Kết quả offline trên case-level metrics:

| Split | Best non-oracle gate | Mean ECE | Delta vs Vector | No-harm |
|---|---|---:|---:|---:|
| Leave-one-class-out | risk_aware_margin_0.01 | 0.1938 | -0.0222 | 596/648 |
| VisA -> MVTec | sage_hier_shared_dynamic_t0.7 | 0.1963 | +0.0011 | 307/360 |
| MVTec -> VisA | risk_aware_margin_0 | 0.2292 | -0.0128 | 286/288 |

Kết luận:

- Offline case-level gate có tín hiệu mạnh.
- Đặc biệt risk-aware và hierarchical routing hợp với claim safe routing.
- Nhưng đây vẫn là case-level analysis, chưa phải deployed per-image gate.

### 2.7. Expert không chỉ là calibrator

Bạn gợi ý thử expert không chỉ là calibrator. Mình thêm `view_experts`:

- `vector_platt`: safe probability view.
- `shift_aware_vector_platt`: shift descriptor view.
- `weighted_platt`: density-ratio view.
- `anchored_structured_gate`: anchored routing view.

Kết quả đáng chú ý:

- MVTec -> VisA: view-expert gate đạt delta ECE khoảng `-0.0164`, tốt hơn calibrator-only khoảng `-0.0128`.
- VisA -> MVTec vẫn chưa tốt.

Kết luận:

> Expert nên được hiểu là reliability view, không chỉ là calibrator family.

Đây là hướng khá hay cho paper vì nó khác với “chỉ thêm Platt scaling”.

### 2.8. Sample-level deployed gate

Để biến gate thành method thật hơn, mình thêm script sample-level:

- lưu per-image probabilities của từng expert;
- train gate per-image;
- đánh giá leave-one-class-out và cross-dataset.

Representative grid:

- VisA: candle, cashew, pcb1, pipe_fryum.
- MVTec: bottle, cable, hazelnut.
- k = 4, 8.
- seeds = 0, 1.
- 4 corruptions.
- 112 cases.
- 12,128 per-image predictions.

Kết quả mạnh nhất:

| Split | Method | ECE |
|---|---|---:|
| MVTec -> VisA | sample_sage_hier_t0.5 | 0.2190 |
| MVTec -> VisA | weighted_platt | 0.2305 |
| MVTec -> VisA | shift_aware_vector_platt | 0.2317 |
| VisA -> MVTec | vector_platt | 0.3035 |
| VisA -> MVTec | sample_sage_hier_t0.6 | 0.2988 |

Kết luận:

- Sample-level gate có tín hiệu, nhất là MVTec -> VisA.
- Nhưng chưa đủ mạnh để claim nó thắng mọi nơi.
- Leave-one-class-out gain nhỏ.
- MVTec-only vẫn khó.

### 2.9. Brier/no-harm mixture gate

Mình thử train soft mixture gate trực tiếp bằng Brier/no-harm objective:

- `sample_brier_mix`
- `sample_brier_anchor_reg`
- `sample_brier_noharm`
- `sample_brier_noharm_anchor`

Kết quả:

- Không thắng SAGE hierarchical gate về ECE.
- Brier/no-harm làm gate conservative hơn nhưng không optimize đúng ECE.

Kết luận:

> Brier/no-harm chưa đủ. Nếu muốn đẩy tiếp Gated, cần differentiable ECE, risk-coverage objective, hoặc validation-class group ECE.

## 3. Nhánh 2: SW-CAD Từ `Methode for SW-CAD.pdf`

### 3.1. SW-CAD đưa thêm gì?

PDF SW-CAD đề xuất hướng formal hơn:

- conformal p-values;
- patch-level FDR;
- image-level false alarm control;
- density-ratio weighting under shift;
- effective sample size `n_eff`.

Điểm hay nhất là nó biến anomaly score thành các đại lượng có ý nghĩa thống kê hơn:

- probability từ Platt scaling trả lời: model tin anomaly bao nhiêu;
- conformal p-value trả lời: score này bất thường thế nào so với calibration normal scores;
- FDR/false alarm trả lời: threshold này kiểm soát lỗi kiểu gì.

### 3.2. Vì sao SW-CAD hợp với few-shot AD?

Few-shot AD có vấn đề lớn: không có anomaly labels để chọn threshold.

SW-CAD giúp bằng cách dùng normal support để tạo calibration residuals. Tuy nhiên k rất nhỏ nên image-level conformal yếu:

- k=8 thì minimum p-value khoảng 1/9 = 0.111;
- k=4 thì minimum p-value khoảng 1/5 = 0.2;
- k=1 gần như không có resolution ở image-level.

Vì vậy patch-level conformal quan trọng hơn.

### 3.3. LOIO là điểm methodological tốt

PDF chỉ ra một lỗi quan trọng:

Nếu fit PCA trên toàn bộ support rồi lại dùng chính support đó để lấy calibration residual, residual sẽ bị deflated vì PCA đã “nhìn thấy” data đó. Điều này làm p-value quá nhỏ và false alarm có thể bị sai.

Cách sửa:

- k >= 2: leave-one-image-out calibration.
- k = 1: spatial interleaved split.

Đây là một chi tiết rất đáng đưa vào method/protocol.

### 3.4. Prototype SW-CAD đã làm gì?

Mình đã implement:

- `src/conformal.py`
- `scripts/evaluate_sw_cad.py`
- conformal p-values;
- LOIO/spatial split;
- weighted conformal;
- density-ratio logistic;
- effective sample size.

Kết quả prototype:

- SW-CAD chạy được.
- Sinh được p-values, false alarm metrics, patch rejection, `n_eff`.
- LOIO hữu ích hơn in-sample.
- Weighted conformal có thể đổi ranking p-value mạnh, nên chỉ nên dùng diagnostic, không thay raw PCA ranking.

Representative VisA SW-CAD:

- raw PCA AUROC khoảng `0.903`.
- LOIO conformal image p-AUROC khoảng `0.843`.
- weighted conformal image p-AUROC khoảng `0.709`.
- false alarm rate ở alpha=0.1 khá conservative.

### 3.5. Kết luận SW-CAD

SW-CAD **đáng giữ**, nhưng hiện tại chưa nên là main claim.

Vai trò tốt nhất:

> reliability/statistical diagnostic layer.

Nó giúp paper có chiều sâu hơn:

- không chỉ nói probability calibrated;
- có p-value, FDR, false alarm, effective sample size;
- giải thích calibration dưới shift khó như thế nào.

Không nên claim:

- first conformal anomaly detection;
- formal guarantee mạnh dưới adversarial/corruption shift;
- SW-CAD là detector chính thắng AUROC.

## 4. Tổng Hợp Claim Từ Đầu Tới Giờ

### 4.1. Claim mạnh, có thể đưa vào paper chính

#### Claim A: Low-storage calibrated subspace detector

> Frozen DINOv2 + PCA/subspace residual là ranking backbone nhẹ, cạnh tranh với memory-bank methods, và giảm storage rõ.

Evidence:

- MVTec AUROC cạnh tranh nhưng không SOTA toàn diện.
- Storage khoảng `0.47-0.56 MB`, thấp hơn memory-bank `2-6 MB`.
- Pixel AUROC MVTec tốt, support việc giữ subspace residual làm ranking.

Cách viết:

> competitive AUROC with substantially lower storage.

Không viết:

> SOTA on MVTec.

#### Claim B: Decoupling ranking and calibration matters

> PCA/subspace residual nên làm ranking; head/calibrator nên làm probability/uncertainty.

Evidence:

- Direct mixing head + PCA không ổn định.
- Decoupled vector calibration cải thiện reliability mà không phá AUROC.
- AUROC/AP giữ nguyên vì ranking không đổi.

Đây là claim khá chắc.

#### Claim C: Shift-aware calibration improves VisA/structured shift but must be gated

> Shift-aware/weighted calibration có thể cải thiện ECE dưới structured shift, nhưng direct expert có thể over-adapt; gated/anchored routing cần thiết.

Evidence:

- Full VisA: shift-aware/weighted/gated cải thiện ECE rõ.
- Full MVTec: direct shift-aware/weighted làm tệ hơn Vector Platt.
- Anchored/gated kéo về gần baseline.

Đây là claim trung tâm cho hướng Gated.

#### Claim D: SAGE-inspired reliability routing is promising

> Shared safe anchor + dynamic reliability views có thể cải thiện sample-level/case-level calibration dưới transfer shift.

Evidence:

- Offline case-level LOCO: delta ECE khoảng `-0.022`.
- Sample-level MVTec -> VisA: `0.2305/0.2317 -> 0.2190` ECE.
- VisA -> MVTec cải thiện nhẹ: `0.3035 -> 0.2988`.

Cách viết cẩn thận:

> promising SAGE-inspired reliability-layer routing.

Không viết:

> universal improvement.

#### Claim E: Unified benchmark for calibration, efficiency, transfer, robustness diagnostics

> Paper không chỉ báo AUROC mà còn báo ECE, Brier, NLL, entropy, storage, latency, corruption, FGSM, transfer.

Evidence:

- Có MVTec/VisA clean.
- Có transfer MVTec -> VisA.
- Có corruption robustness.
- Có FGSM sweep.
- Có calibration ablation.
- Có pixel metrics.
- Có official SubspaceAD representative caveat.

Đây là claim benchmark/protocol mạnh.

## 5. Claim yếu hoặc chỉ nên dùng làm diagnostic

### Weak/Diagnostic Claim 1: Adversarial robustness

Không claim robust.

Kết quả FGSM cho thấy AUROC tụt mạnh. Nên viết:

> FGSM exposes fragility; robustness experiments are diagnostic, not evidence of robustness.

### Weak/Diagnostic Claim 2: SW-CAD weighted conformal improves performance

Chưa đủ mạnh.

Có thể viết:

> SW-CAD provides conformal reliability diagnostics and exposes few-shot calibration limits.

Không viết:

> weighted conformal solves shift.

### Weak/Diagnostic Claim 3: Sample-level gate dominates all metrics

Không đúng hiện tại.

Sample gate cải thiện ECE ở vài split, nhưng:

- LOCO gain nhỏ;
- MVTec-only khó;
- Brier/NLL đôi khi tệ hơn;
- Brier/no-harm objective chưa thắng hierarchical gate.

Nên viết:

> sample-level SAGE routing is promising but requires ECE-aware training.

### Weak/Diagnostic Claim 4: Official SAGE architecture works for AD

Không claim.

Mình chỉ dùng SAGE as inspiration. Không dùng segmentation architecture.

Nên viết:

> inspired by SAGE-style shared/dynamic routing.

Không viết:

> adapted SAGE architecture to anomaly detection.

## 6. Claim Không Nên Viết

Không nên viết các câu sau:

- “Our method achieves SOTA on MVTec.”
- “We are the first to use DINOv2 PCA for anomaly detection.”
- “We are the first calibration benchmark for DINOv2 anomaly detection.”
- “Our method is adversarially robust.”
- “Shift-Aware improves all corruptions and all datasets.”
- “Gated calibration universally improves over Vector Platt.”
- “SW-CAD gives strong finite-sample guarantees under arbitrary corruption/adversarial shift.”
- “We directly adapt SAGE architecture to anomaly detection.”

## 7. Story Paper Nên Theo

Một story hợp lý hiện tại:

1. Few-shot industrial AD cần detector rẻ, reliable, không phụ thuộc memory bank lớn.
2. Frozen DINOv2 subspace residual là ranking backbone nhẹ và mạnh.
3. Nhưng raw scores không calibrated, và reliability dưới dataset/corruption shift là vấn đề thật.
4. Ta decouple ranking và calibration.
5. Vector Platt là baseline calibration an toàn.
6. Shift-aware/weighted calibration giúp structured shift nhưng có thể over-adapt.
7. Inspired by SAGE, ta dùng shared safe anchor + dynamic reliability routing.
8. Gated routing cải thiện hoặc giữ an toàn hơn trong các transfer/structured shift settings, nhưng không claim universal win.
9. SW-CAD/conformal layer bổ sung diagnostic về p-values, false alarm, FDR, `n_eff`.
10. Benchmark thống nhất clean/calibration/efficiency/transfer/robustness giúp paper có giá trị dù không claim pure AUROC SOTA.

## 8. Claim Cuối Cùng Nên Dùng Hiện Tại

### Main Claim

> We propose a low-storage decoupled calibrated subspace detector for few-shot industrial anomaly detection, using frozen DINOv2 subspace residuals for ranking and calibration/reliability routing for probability under shift.

### Gated Claim

> Inspired by SAGE-style shared/dynamic routing, we route between safe, shift-aware, density-ratio, and anchored reliability views. This improves calibration under VisA and transfer shifts while revealing that direct shift-aware calibration can over-adapt on MVTec.

### SW-CAD Claim

> A conformal diagnostic layer provides p-values, false-alarm/FDR-style reliability summaries, and effective sample size under shift, clarifying the limits of few-shot calibration.

### Diagnostic Claim

> Robustness and transfer experiments expose when calibrated anomaly detectors fail, especially under adversarial or severe shift, and should be reported as diagnostics rather than robustness claims.

## 9. Hướng Tiếp Theo Nếu Muốn Đẩy Q1

Ưu tiên cao nhất:

1. **Validation-class ECE gate**: optimize gate theo group ECE trên held-out classes, không phải per-sample NLL/Brier.
2. **Risk-coverage/selective prediction**: dùng entropy/gate confidence để abstain hoặc flag unreliable samples.
3. **Add conformal view expert**: đưa SW-CAD p-value/`n_eff` vào expert pool của SAGE-style gate.
4. **Full sample-level gate** nếu representative tốt hơn sau khi đổi objective.
5. **Paper framing rõ**: không SOTA AUROC, mà là low-storage calibrated reliability under shift.
