# Audit claim và protocol cho mục tiêu Q1

Ngày cập nhật: 2026-07-11.

## 1. Kết luận điều hành

Bản V1 chưa đủ chắc để nộp tạp chí Q1 hạng cao. Phần mạnh đã có là một hệ thống anomaly detection ít lưu trữ, tách ranking khỏi reliability, cùng benchmark calibration/transfer/shift khá rộng. Tuy nhiên, novelty không thể dựa trên DINOv2 + PCA, Platt scaling, conformal anomaly detection, LOIO hay weighted conformal riêng lẻ vì đều đã có prior work gần.

Hướng có tiềm năng nhất hiện nay là **Support-Conditioned Cross-Category Reliability Routing (SC3R)**: dùng normal support của category đích để chuẩn hóa nonconformity, dùng archive normal từ category nguồn để tăng độ phân giải thống kê, rồi route an toàn giữa ngưỡng target-only và source-assisted theo shift/ESS/disagreement. Chỉ giữ SC3R làm contribution chính nếu thỏa các điều kiện false-alarm, power và no-harm định trước.

## 2. Claim có thể giữ

1. **Low-storage decoupled detector.** PCA/subspace residual giữ vai trò ranking; probability, uncertainty và quyết định vận hành được xử lý ở lớp reliability riêng. Claim này là kiến trúc hệ thống và efficiency, không phải claim phát minh subspace AD.
2. **Calibration under transfer and structured shift is protocol-dependent.** Vector calibration và shift descriptors có ích ở VisA/MVTec-to-VisA, nhưng không cải thiện phổ quát trên MVTec. Safe fallback/gating cần được mô tả theo đúng phạm vi dữ liệu.
3. **ECE is not deployment-universal for anomaly detection.** Stress test cho thấy ECE và thứ hạng calibrator thay đổi mạnh theo anomaly prevalence, dù ranking score không đổi. Paper phải báo cáo false-alarm, power, attainable alpha và risk-coverage bên cạnh ECE/Brier/NLL.
4. **Conformal signals are statistical diagnostics.** P-value, effective sample size và attainable alpha bổ sung thông tin vận hành; chúng không mặc nhiên là posterior anomaly probability.

## 3. Claim chưa được phép viết

- Không claim SOTA trên MVTec AD.
- Không claim DINOv2 + PCA/subspace residual là mới.
- Không claim first conformal anomaly detection, first LOIO/cross-conformal AD hoặc first weighted conformal AD.
- Không claim adversarial robustness; FGSM hiện là failure diagnostic.
- Không gọi local nearest-neighbor implementation là official PatchCore hoặc official AnomalyDINO.
- Không diễn giải `1 - p_value` thành xác suất hậu nghiệm anomaly nếu chưa có calibration phù hợp.

## 4. Audit baseline

`src/models/baselines.py` hiện để `AnomalyDINO` kế thừa trực tiếp scoring của `PatchCoreNN`. Vì vậy hai hàng local PatchCore/AnomalyDINO thực chất là cùng một controlled DINOv2 nearest-neighbor memory-bank baseline. Bản paper tiếp theo phải đổi nhãn hàng này. Chỉ dùng tên official khi chạy code/config official hoặc trích reported result với protocol được ghi rõ.

Official SubspaceAD representative hiện rất mạnh:

| k | Image AUROC | Pixel AUROC |
|---:|---:|---:|
| 1 | 0.9518 | 0.9710 |
| 4 | 0.9625 | 0.9737 |
| 8 | 0.9639 | 0.9743 |

Kết quả này buộc paper định vị novelty ở reliability/protocol/routing, không ở pure ranking AUROC.

## 5. Collision với prior work

- AnomalyDINO: DINOv2 patch similarity và memory bank cho few-shot AD, arXiv:2405.14529.
- SubspaceAD: frozen DINOv2 và subspace residual, arXiv:2602.23013.
- Khan và Krawczyk: calibration, ECE, Platt scaling và FGSM cho DINOv2-based few-shot AD, arXiv:2510.13643.
- Leave-one-out/bootstrap/cross-conformal AD đã xuất hiện, arXiv:2402.16388.
- Weighted conformal trong low-data và phân tích resolution/ESS đã xuất hiện, arXiv:2603.23205.
- General nonconformity CAD toolkit đã xuất hiện, arXiv:2605.13642.
- Few-shot conformal với auxiliary tasks đã xuất hiện, arXiv:2102.08898.
- Industrial-image VAE + conformal AD cũng đã có báo cáo tại ECNDT 2026.
- SAGE được cite ở mức cảm hứng shared/dynamic expert routing, không claim chuyển nguyên kiến trúc segmentation sang AD.

## 6. Kết quả protocol audit mới

### 6.1 Matched LOIO k=4 trên MVTec representative

Matched LOIO so sánh support-held-out và test dưới cùng fold-specific PCA. Nó đúng cặp statistic hơn legacy LOIO, nhưng không cải thiện trade-off vận hành:

| Condition | FAR matched | FAR legacy | Power matched | Power legacy |
|---|---:|---:|---:|---:|
| clean | 0.2458 | 0.1695 | 0.9056 | 0.8944 |
| blur | 0.2458 | 0.1723 | 0.9019 | 0.8926 |
| brightness/contrast | 0.2571 | 0.1751 | 0.9074 | 0.9037 |
| Gaussian noise | 0.3701 | 0.3249 | 0.9130 | 0.9167 |
| JPEG | 0.3842 | 0.3333 | 0.9148 | 0.9093 |

Kết luận: matched LOIO là protocol audit/negative result, chưa phải method contribution.

### 6.2 Prevalence stress

Trên full VisA, ECE của LOIO thay đổi từ 0.4039 ở prevalence 1% xuống 0.1493 ở 50%; weighted conformal thay đổi từ 0.2655 xuống 0.2102. Thứ hạng hai method đảo chiều theo prevalence. MVTec representative cũng có hiện tượng tương tự: LOIO 0.4904 xuống 0.2195, weighted 0.2026 lên 0.2548.

Kết luận: ECE trên tập anomaly-balanced không đủ để chứng minh reliability triển khai. Đây là finding mạnh và nên xuất hiện trong main paper.

### 6.3 Source-conditioned routing pilot

Pooling normal archive từ các category nguồn mở được mức alpha mà target-only few-shot conformal không thể biểu diễn:

- MVTec k=4, alpha=0.1: source pool có FAR khoảng 0.049-0.068 và power khoảng 0.108-0.111; target-only có FAR=0 và power=0 do p-value tối thiểu là 0.2.
- Full VisA k=8, alpha=0.1: source pool có FAR 0.0478, power 0.2299 và precision 0.8304; target-only tiếp tục không phát hiện.
- Full VisA k=4 vẫn có power rất thấp, cho thấy pooling quantized target p-value chưa đủ.

Thí nghiệm quyết định tiếp theo là pooling **support-normalized raw residual**, không pooling p-value đã lượng tử hóa.

## 7. Protocol bắt buộc cho bản paper tiếp theo

- Sampling corruption phải stratified-random hoặc chạy full test set; lưu manifest image/seed.
- Báo cáo paired/hierarchical statistics theo class rồi seed; không coi từng image/corruption row là replicate độc lập.
- Main operational metrics: normal false-alarm rate, anomaly power/recall, alarm precision, attainable alpha, coverage gap, AURC/risk-coverage.
- ECE/Brier/NLL là secondary metrics cho probability calibrator; với conformal confidence phải ghi rõ đây là diagnostic score.
- Tách cached-feature latency khỏi end-to-end encoder latency.
- Tách local controlled baseline khỏi official reproduction/reported numbers.

## 8. Decision gate cho SC3R

SC3R chỉ được nâng thành contribution chính nếu trên class-held-out và cross-dataset evaluation:

1. Có power khác 0 tại alpha 0.05 hoặc 0.10.
2. Mean normal FAR không vượt alpha + 0.02.
3. Safe gate đạt no-harm ít nhất 80% so với target-only/vector anchor trên các dataset-condition-k.
4. Không dùng anomaly label của target test để chọn route hay threshold.
5. Có paired confidence interval hoặc hierarchical bootstrap theo class/seed.

Nếu không đạt, giữ source/conformal routing ở phần analysis và đóng paper quanh low-storage detector + calibration-under-shift benchmark + prevalence stress finding.

## 9. Trạng thái triển khai

- Unit/integration suite trước audit: 37 passed, 1 skipped.
- Các test mới cho prevalence stress và source routing đã pass riêng.
- Matched LOIO k=4 hoàn tất; k=8 đang chạy.
- Support-normalized source pooling đang được kiểm định.
- Official AnomalyDINO đã được tải về `third_party/AnomalyDINO`; chưa được phép dùng số liệu trước khi reproduction hoàn tất và protocol được đối chiếu.
