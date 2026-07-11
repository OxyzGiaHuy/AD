# Báo Cáo Ngắn Cho Thầy: Trạng Thái Hiện Tại Của Hướng Few-Shot Anomaly Detection

## 1. Mục Tiêu Ban Đầu

Ý tưởng ban đầu là xây dựng một phương pháp few-shot anomaly detection cho industrial images với:

- backbone frozen DINOv2 ViT-S/14;
- chỉ dùng 1-8 ảnh normal mỗi category;
- thay memory bank nặng bằng một head/adapter nhỏ kết hợp PCA/subspace residual;
- thêm calibration để raw anomaly score trở thành probability đáng tin hơn;
- đánh giá robustness với corruption và adversarial attack.

Claim ban đầu khá tham vọng:

> Một trainable head/adapter nhỏ trên frozen DINOv2 có thể thắng hoặc ngang memory-bank methods về AUROC, rẻ hơn ở inference, đồng thời calibrated và robust hơn.

## 2. Những Gì Đã Chạy

Đã scaffold codebase paper-grade với CLI, configs, tests, docs, outputs và benchmark artifacts. Các phần chính đã chạy:

- MVTec full benchmark với k `{1,2,4,8}`, nhiều seeds, nhiều baseline.
- VisA full benchmark với cùng protocol.
- Pixel metrics, calibration ablation, robustness/corruption, FGSM sweep.
- MVTec to VisA transfer calibration.
- Official SubspaceAD representative/k-trend để kiểm tra novelty guardrail.
- P2 full VisA cho hai hướng ưu tiên:
  - PCA128 high-accuracy low-storage setting.
  - Shift-Aware Calibration.

Test suite hiện tại pass: `19 passed, 1 skipped`.

## 3. Kết Quả Chính Hiện Tại

### MVTec

`calib_subspace_head` đạt AUROC cạnh tranh nhưng chưa thắng toàn diện PatchCore/AnomalyDINO/SubspaceAD.

- MVTec `calib_subspace_head` AUROC:
  - k1: `0.9038`
  - k4: `0.9371`
  - k8: `0.9452`
- Storage khoảng `0.472 MB`, thấp hơn memory-bank baselines khoảng `2-6 MB`.

Official SubspaceAD representative rất mạnh:

- image AUROC trung bình k1/k4/k8: `0.9518 / 0.9625 / 0.9639`;
- pixel AUROC trung bình k1/k4/k8: `0.9710 / 0.9737 / 0.9743`.

Vì vậy không nên claim DINOv2 + PCA/subspace residual là mới, cũng không nên claim SOTA MVTec AUROC.

### VisA

VisA là nơi method hiện tại có tín hiệu tốt hơn.

Baseline PCA64 `calib_subspace_head` AUROC:

- k1: `0.8226`
- k2: `0.8534`
- k4: `0.8696`
- k8: `0.8796`

PCA128 full VisA cải thiện AUROC ở mọi k:

- k1: `0.8226 -> 0.8335`, tăng `+0.0110`;
- k2: `0.8534 -> 0.8684`, tăng `+0.0150`;
- k4: `0.8696 -> 0.8852`, tăng `+0.0156`;
- k8: `0.8796 -> 0.8967`, tăng `+0.0171`.

Storage vẫn thấp:

- PCA64: khoảng `0.472 MB`;
- PCA128: khoảng `0.566 MB`.

### Calibration

Vector Platt và decoupled calibration giúp probability đáng tin hơn, đặc biệt khi k tăng.

Shift-Aware Calibration full VisA không đổi AUROC vì không đổi ranking, nhưng cải thiện ECE mạnh ở k4/k8:

- k1 ECE: `0.4295 -> 0.4320`, hơi xấu hơn;
- k2 ECE: `0.3780 -> 0.3768`, gần như hòa;
- k4 ECE: `0.2839 -> 0.2032`, tốt hơn rõ;
- k8 ECE: `0.2066 -> 0.1447`, tốt hơn rõ.

NLL giảm ở mọi k:

- k1: `4.3117 -> 4.0028`;
- k2: `2.4165 -> 1.9310`;
- k4: `1.3818 -> 0.8226`;
- k8: `0.8597 -> 0.5487`.

### Robustness

FGSM cho thấy method vẫn fragile, AUROC tụt mạnh. Vì vậy không claim adversarial robustness.

Robustness nên được viết như diagnostic benchmark:

> Method quantify failure modes and uncertainty behavior under corruption/adversarial shift, not solve adversarial robustness.

## 4. Claim Ban Đầu So Với Claim Hiện Tại

Claim ban đầu:

> Trainable head/adapter nhỏ thắng memory-bank methods về AUROC, đồng thời calibrated và robust.

Claim hiện tại nên đổi thành:

> A low-storage calibrated subspace detector keeps subspace residual for ranking, uses compact PCA representations for efficient few-shot anomaly detection, and improves probability reliability through vector/shift-aware calibration, especially under VisA/domain-shift settings at moderate/high shot.

Nói ngắn gọn:

- Không claim SOTA MVTec AUROC.
- Không claim adversarial robustness.
- Không claim DINOv2 + PCA/subspace là mới.
- Claim chính nên là **Calibration + Efficiency + Transfer/Robustness Diagnostics**.
- Claim mới có tiềm năng nhất là **Shift-Aware Calibration under dataset/corruption shift**.

## 5. Verify Novelty Hiện Tại

Các work đã phải đối chiếu:

- AnomalyDINO: đã dùng frozen DINOv2 + patch similarity/memory bank cho few-shot AD.
- SubspaceAD: đã dùng frozen DINOv2 + PCA/subspace residual, training-free và rất mạnh.
- Khan & Krawczyk 2025: đã chỉ ra DINOv2 few-shot AD poorly calibrated, dùng Platt scaling, FGSM fragility và entropy/uncertainty.
- Calibration under distribution shift là một hướng rộng đã có trong image classification và covariate shift literature.

Khoảng trống còn lại:

> Trong few-shot industrial anomaly detection, chưa thấy work nào trực tiếp kết hợp frozen DINOv2 subspace detector với vector/disagreement/shift-aware calibration, đánh giá cùng lúc clean accuracy, storage, transfer calibration, corruption shift, FGSM diagnostic, và pixel metrics trên MVTec/VisA.

Đây là novelty theo hướng empirical-methodological benchmark, không phải một component hoàn toàn chưa từng tồn tại.

## 6. Hướng Tiếp Theo

Ưu tiên 1:

- Biến Shift-Aware Calibration thành method variant chính thức trong code/config.
- Chạy corruption/robustness calibration trên VisA và MVTec:
  - Gaussian noise;
  - blur;
  - brightness/contrast;
  - JPEG;
  - FGSM nếu surrogate hợp lệ.
- So sánh ECE/Brier/NLL/entropy shift giữa vector Platt và shift-aware vector Platt.

Ưu tiên 2:

- Viết bảng paper-ready:
  - clean AUROC/AP/ECE/storage;
  - PCA64 vs PCA128;
  - vector Platt vs shift-aware calibration;
  - transfer calibration;
  - robustness/corruption calibration.

Ưu tiên 3:

- Nếu còn compute, chạy thêm:
  - Shift-Aware Calibration trên MVTec full;
  - corruption calibration full VisA;
  - end-to-end runtime audit không cache cho representative classes.

## 7. Định Vị Paper

Với kết quả hiện tại, paper có khả năng aim Q1/Q2 theo hướng applied/empirical computer vision hoặc industrial AI, nếu phần benchmark và ablation được viết chặt.

Không nên target top-tier CV theo claim pure SOTA accuracy, vì official SubspaceAD và memory-bank baselines rất mạnh.

Paper nên được định vị là:

> Reliability-centered few-shot industrial anomaly detection: low-storage subspace inference, calibrated probabilities, and transfer/robustness diagnostics.


## 8. Cập Nhật Mới: Shift-Aware Dưới Corruption Shift

Đã chạy xong full VisA corruption calibration: `960/960` rows.

Kết quả chính: Shift-Aware Calibration không đổi AUROC/AP vì không đổi ranking, nhưng cải thiện ECE/Brier/NLL dưới các structured corruptions:

- blur k4/k8 ECE: `0.2844 -> 0.2111`, `0.2078 -> 0.1439`;
- brightness/contrast k4/k8 ECE: `0.2845 -> 0.2118`, `0.2086 -> 0.1532`;
- JPEG k4/k8 ECE: `0.2876 -> 0.2297`, `0.2119 -> 0.1564`.

Caveat: Gaussian noise không được cải thiện về ECE:

- k4: `0.2695 -> 0.2762`;
- k8: `0.1900 -> 0.1913`.

Điều này làm claim sắc hơn:

> Shift-Aware Calibration cải thiện reliability dưới structured/domain-style shift như blur, illumination/contrast, JPEG compression, nhưng không phải universal fix cho stochastic additive noise.

Đây là hướng claim tốt cho paper vì có both positive result và failure mode rõ ràng.
