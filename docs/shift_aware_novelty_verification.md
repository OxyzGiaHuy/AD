# Verify Novelty: Shift-Aware Calibration Under Corruption Shift

## Mục Tiêu Kiểm Tra

Hướng mới đang chạy là: dùng `shift_aware_calib_subspace_head` cho few-shot industrial anomaly detection, giữ PCA/subspace residual làm ranking, nhưng mở rộng vector Platt calibration bằng các shift descriptors để cải thiện ECE/Brier/NLL dưới corruption/domain shift.

## Các Work Gần Nhất Đã Kiểm Tra

### Khan & Krawczyk 2025

Link: https://arxiv.org/abs/2510.13643

Paper này rất gần với bài của mình ở phần DINOv2 few-shot AD, calibration và FGSM. Họ chỉ ra raw anomaly scores poorly calibrated, dùng Platt scaling, đo ECE, và dùng entropy để flag adversarial perturbations.

Không được claim:

- first calibration benchmark for DINOv2 few-shot AD;
- first FGSM robustness benchmark;
- Platt scaling itself is novel;
- entropy for adversarial flagging is entirely new.

Khoảng trống còn lại:

- paper này dựa trên AnomalyDINO/memory-bank style và scalar Platt/post-hoc uncertainty;
- chưa thấy họ đánh giá decoupled subspace ranking + vector/disagreement/shift descriptors như một calibrator riêng;
- chưa thấy claim low-storage subspace detector + calibration under corruption/transfer shift như một unified benchmark.

### Anomaly Detection Under Distribution Shift

Link: https://arxiv.org/abs/2303.13845

Paper này nghiên cứu anomaly detection khi train/test distribution lệch nhau và benchmark AD dưới distribution shift. Đây là guardrail quan trọng: distribution-shift AD không phải mới.

Không được claim:

- first anomaly detection under distribution shift;
- first benchmark showing AD degrades under distribution shift.

Khoảng trống còn lại:

- hướng của mình hẹp hơn: few-shot industrial AD, frozen DINOv2, PCA/subspace residual, calibration reliability under corruption shift;
- trọng tâm của mình là calibrated probability/reliability, không phải chỉ robust accuracy.

### Unsupervised Calibration Under Covariate Shift

Link: https://arxiv.org/abs/2006.16405

Paper này formalize calibration under covariate/domain shift. Nó cho thấy calibration có thể mất ổn định dưới shift và cần phương pháp calibration riêng.

Không được claim:

- calibration under shift is a new problem;
- post-hoc calibration under covariate shift is new.

Khoảng trống còn lại:

- paper này là calibration theory/general ML, không phải few-shot industrial anomaly detection;
- không xử lý DINOv2 subspace residual, pseudo-anomaly calibration, hoặc MVTec/VisA corruption diagnostics.

### Robust Calibration With Multi-Domain Temperature Scaling

Link: https://arxiv.org/abs/2206.02757

Paper này dùng multi-domain temperature scaling để tăng robust calibration dưới distribution shift.

Không được claim:

- first robust calibration under distribution shift;
- first use of domain heterogeneity for calibration.

Khoảng trống còn lại:

- phương pháp của mình không dùng multi-domain temperature scaling;
- mình dùng vector Platt với features đặc thù cho subspace anomaly detection: `[pca_score, head_score, disagreement, norm shift, residual statistics]`;
- setting là few-shot AD với normal-only support, không phải supervised multi-domain classification.

### Calibration Under Dataset Shift In Image Classification

Link: https://arxiv.org/abs/2507.07780

Paper này survey/benchmark calibration under shift trong image classification và chỉ ra post-hoc methods có thể có tradeoff ID/OOD calibration.

Không được claim:

- calibration under shift in vision is unexplored;
- post-hoc calibrators under shift are generally novel.

Khoảng trống còn lại:

- image classification khác industrial anomaly detection: AD thường thiếu anomaly labels, cần normal-only/pseudo anomaly calibration;
- paper của mình có thể đóng góp empirical benchmark cho few-shot AD, nơi calibration/ranking/storage/robustness được báo cáo cùng protocol.

## Kết Luận Novelty Thận Trọng

Claim nên viết:

> We study shift-aware vector calibration for low-storage DINOv2 subspace few-shot industrial anomaly detection, where PCA residuals provide ranking and additional subspace/disagreement/shift descriptors improve calibrated probability reliability under transfer and corruption shifts.

Không nên viết:

- first calibration under shift;
- first robust calibration;
- first DINOv2 few-shot calibration;
- adversarially robust method;
- SOTA MVTec AUROC.

## Experiment Đang Chạy Để Support Claim

Đã thêm official model variant:

- `shift_aware_calib_subspace_head`

Đã thêm runner:

- `scripts/evaluate_shift_aware_corruption_calibration.py`

Smoke test đã chạy pass trên VisA `candle`, k1, seed0, Gaussian noise, `max_images=10`.

Full background job đang chạy:

- dataset: VisA;
- classes: 12 classes;
- k: `{4,8}`;
- seeds: `{0,1,2,3,4}`;
- corruptions: Gaussian noise, blur, brightness/contrast, JPEG;
- methods: vector Platt vs shift-aware vector Platt;
- total rows: `960`;
- output detail: `outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_detailed.csv`;
- output summary: `outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_summary.csv`;
- output delta: `outputs/paper_tables/shift_aware_corruption_calibration_visa_k4k8_full_corruptions_delta.csv`.

Nếu kết quả cho thấy ECE/Brier/NLL giảm dưới corruption ở k4/k8 mà AUROC giữ nguyên, đây sẽ là bằng chứng mạnh cho claim `calibration under corruption shift`.


## Full Corruption Result Update

The full VisA corruption experiment is complete (`960/960` rows). The result supports a conditional novelty claim:

> Shift-aware vector calibration improves probability reliability under structured corruption/domain shift while preserving PCA/subspace anomaly ranking.

Evidence:

| Corruption | k | Vector ECE | Shift-Aware ECE | Delta |
| --- | ---: | ---: | ---: | ---: |
| blur | 4 | `0.2844` | `0.2111` | `-0.0733` |
| blur | 8 | `0.2078` | `0.1439` | `-0.0640` |
| brightness/contrast | 4 | `0.2845` | `0.2118` | `-0.0727` |
| brightness/contrast | 8 | `0.2086` | `0.1532` | `-0.0554` |
| JPEG | 4 | `0.2876` | `0.2297` | `-0.0579` |
| JPEG | 8 | `0.2119` | `0.1564` | `-0.0554` |
| Gaussian noise | 4 | `0.2695` | `0.2762` | `+0.0067` |
| Gaussian noise | 8 | `0.1900` | `0.1913` | `+0.0013` |

AUROC/AP are unchanged by design because Shift-Aware Calibration does not change ranking. NLL improves for all corruptions, including Gaussian noise.

Novelty wording should remain careful: this is not the first calibration-under-shift method, but a task-specific shift-aware vector calibrator for frozen DINOv2 subspace few-shot industrial anomaly detection.
