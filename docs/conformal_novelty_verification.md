# Novelty Verification Cho Conformal Reliability Routing

Ngày: 2026-07-09

## Mục tiêu kiểm tra

Ta cần tránh đụng claim với các hướng đã có:

- DINOv2 few-shot AD bằng memory bank.
- DINOv2 + PCA/subspace residual.
- Calibration/ECE/Platt/FGSM cho DINOv2 few-shot AD.
- Conformal anomaly detection nói chung.
- Gated expert routing kiểu SAGE trong segmentation.

## Prior Work Chính

### AnomalyDINO

Link: https://arxiv.org/abs/2405.14529

AnomalyDINO dùng frozen DINOv2 features và patch similarity/memory-bank cho few-shot anomaly detection. Paper này đã claim mạnh về DINOv2 vision-only, patch-based few-shot AD, image-level và pixel-level anomaly.

Không được claim mới:

- “DINOv2 for few-shot anomaly detection”.
- “Patch-level DINOv2 features for industrial anomaly detection”.
- “Training-free DINOv2 memory-bank AD”.

### SubspaceAD

Link: https://arxiv.org/abs/2602.23013

SubspaceAD dùng frozen DINOv2 patch features và PCA/subspace residual để phát hiện anomaly, training-free và không cần memory bank lớn.

Không được claim mới:

- “DINOv2 + PCA residual”.
- “Subspace modeling for few-shot AD”.
- “Low-memory alternative to memory-bank” nếu chỉ nói PCA residual đơn thuần.

### Khan & Krawczyk 2025

Link: https://arxiv.org/abs/2510.13643

Paper này đã phân tích robustness và uncertainty cho DINOv2-based few-shot AD, gồm FGSM, ECE, Platt scaling, entropy trên adversarial inputs.

Không được claim mới:

- “First calibration benchmark for DINOv2 few-shot AD”.
- “First FGSM/adversarial robustness study”.
- “Platt scaling fixes raw anomaly score calibration” như contribution chính.

### Conformal anomaly detection

Ví dụ gần đây: https://arxiv.org/abs/2605.13642

Conformal anomaly detection đã là hướng rộng: biến anomaly scores thành p-values, hỗ trợ threshold thống kê, false discovery control, split/weighted conformal, và reliability dưới một số giả định.

Không được claim mới:

- “First conformal anomaly detection”.
- “First p-values for anomaly scores”.
- “First FDR/false-alarm control for anomaly detection”.

### SAGE / Gated Experts

Link tham khảo: https://arxiv.org/abs/2511.18493

SAGE dùng dynamic/hierarchical expert routing trong segmentation, với shared path và expert path để thích nghi input variability.

Không được claim:

- Dùng nguyên architecture SAGE.
- Gated experts là mới nói chung.

Nên cite SAGE như inspiration cho:

- shared safe anchor + dynamic specialized reliability view;
- hierarchical routing;
- input-adaptive expert selection.

## Novelty còn defensible

Contribution có thể bảo vệ:

1. **Decoupled low-storage reliability pipeline**
   - Ranking dùng PCA/subspace residual.
   - Reliability dùng calibration/conformal layer riêng.
   - Tránh thay ranking bằng probability calibrator.

2. **Conformal reliability view cho DINOv2 subspace few-shot industrial AD**
   - LOIO conformal p-value được tính từ few-shot support normal patches/images.
   - Dùng `1 - p-value` như probability-like reliability view.
   - Tích hợp với Vector Platt/Shift-Aware/Weighted experts trong cùng benchmark.

3. **Protocol evidence under transfer/corruption shift**
   - MVTec -> VisA và VisA -> MVTec.
   - LOCO class-held-out.
   - Structured corruptions.
   - Metrics gồm ECE, Brier, NLL, risk-coverage, no-harm.

4. **Selective reliability diagnostic**
   - Entropy/disagreement/`n_eff`/conformal signals flag high-risk samples.
   - Có risk-coverage table thay vì chỉ báo ECE trung bình.

## Paper-safe wording

Nên viết:

> Unlike prior DINOv2 memory-bank or subspace detectors that primarily focus on ranking accuracy, we study the reliability layer of low-storage few-shot industrial AD. We show that LOIO conformal p-value views can be decoupled from PCA residual ranking and used as a statistically interpretable reliability route, improving calibration under representative class and dataset shifts.

Không nên viết:

- “We are the first to use conformal prediction for anomaly detection.”
- “We are SOTA on MVTec.”
- “Our method is adversarially robust.”
- “DINOv2 PCA residual is novel.”
