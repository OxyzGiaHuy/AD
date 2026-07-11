# Conformal Reliability Routing: Claim Hiện Tại

Ngày: 2026-07-09

## 1. Method chính nên khóa

Tên làm việc:

> Low-storage Decoupled DINOv2 Subspace Detector with Conformal Reliability Routing

Flow chính:

1. Dùng frozen DINOv2 ViT-S/14 để trích patch features.
2. Fit PCA/subspace trên k ảnh normal support.
3. Dùng PCA residual làm `raw_anomaly_score` để ranking anomaly.
4. Không thay ranking bằng head/calibrator.
5. Thêm reliability layer gồm:
   - Vector Platt / Shift-Aware Platt / Weighted Platt như calibrator baselines.
   - LOIO conformal p-value view: `conformal_prob_loio = 1 - image_p_loio`.
   - Optional routing/gating dựa trên validation ECE hoặc rule no-label.
6. Dùng entropy/disagreement/conformal signals để selective prediction hoặc flag sample rủi ro.

Điểm quan trọng: ranking và reliability được tách riêng. PCA/subspace residual trả lời “ảnh nào bất thường hơn”; conformal/calibration layer trả lời “xác suất và độ tin cậy của quyết định này có đáng tin không”.

## 2. Kết quả protocol mới

Nguồn bảng:

- `outputs/paper_tables/conformal_routing_protocols_full_summary.csv`
- `outputs/paper_tables/conformal_routing_claim_evidence.md`

Kết quả nổi bật của `fixed_conformal_loio`:

| Split | ECE | Vector ECE | Delta | No-Harm |
|---|---:|---:|---:|---:|
| MVTec -> VisA | 0.0985 | 0.3014 | -0.2028 | 1.000 |
| VisA -> MVTec | 0.1019 | 0.3035 | -0.2016 | 1.000 |
| LOCO | 0.1156 | 0.3039 | -0.1883 | 1.000 |
| Within split | 0.1537 | 0.3606 | -0.2068 | 1.000 |

Ý nghĩa:

- Kết quả mạnh không chỉ đến từ việc dùng validation label để chọn expert.
- `fixed_conformal_loio` là rule cố định, không cần tune expert bằng label test.
- `validation_best_vector_or_conformal` cũng chọn cùng hướng conformal trên representative splits.
- `no_label_shift_or_neff_gate` yếu hơn nhưng vẫn cải thiện ECE và không harm trong các split được báo cáo.

## 3. Ablation kết luận

- `fixed_vector`: baseline an toàn nhưng ECE cao.
- `fixed_conformal_loio`: mạnh nhất và ổn định nhất hiện tại.
- `fixed_conformal_weighted`: có ích ở vài split nhưng hại VisA -> MVTec, không nên làm main.
- `fixed_vector_conformal_mix_50_50`: cải thiện ổn nhưng kém hơn conformal LOIO.
- `no_label_shift_or_neff_gate`: đáng giữ như practical no-label fallback.
- `validation_best_vector_or_conformal`: protocol tốt để báo cáo khi có validation split hợp lệ.

## 4. Claim mạnh

Claim chính có thể viết:

> We propose a low-storage decoupled DINOv2 subspace detector whose PCA residual ranking is complemented by conformal reliability routing. Across representative MVTec/VisA class-held-out and cross-dataset shift protocols, a fixed LOIO conformal reliability view substantially reduces ECE over Vector Platt while preserving the underlying anomaly ranking.

Claim diagnostic/selective:

> Conformal probability, entropy, expert disagreement, and effective-sample-size signals identify high-risk samples; abstaining on the riskiest 20% reduces ECE by about 41% overall, 50% on VisA, and 65% on MVTec in the representative conformal-view benchmark.

## 5. Claim yếu/cần caveat

Không claim:

- SOTA AUROC trên MVTec.
- Adversarial robustness.
- First conformal anomaly detection.
- First DINOv2 PCA/subspace residual.
- Universal learned SAGE gate outperforming all experts.

Caveat hiện tại:

- Full representative đã tốt, nhưng cần full VisA hoặc full MVTec để thành main table paper.
- `conformal_prob_loio` hiện là expert thắng áp đảo; SAGE nên được cite như inspiration cho reliability routing/shared-vs-specialized logic, không nên nói dùng nguyên architecture SAGE.
- Weighted conformal chưa an toàn dưới VisA -> MVTec.

## 6. Scale-up đang chạy

Đã khởi chạy job nền full VisA conformal image views:

- 12 VisA classes.
- k `{4,8}`.
- seeds `{0,1,2,3,4}`.
- corruptions `{gaussian_noise, blur, brightness_contrast, jpeg}`.
- `max_images=120` mỗi case.
- Log: `logs/sw_cad_image_views_visa_full_k4k8_s0s4.log`.
- Output dự kiến: `outputs/paper_tables/sw_cad_image_views_visa_full_k4k8_s0s4.csv`.

Sau khi job xong, cần merge với prediction table tương ứng hoặc sinh prediction table full để chạy lại conformal routing protocol trên full VisA.

## 7. Full VisA k4/k8 Corruption Result

Full VisA conformal export is complete:

- `480/480` cases.
- `56,000` image rows.
- Classes: 12 VisA classes.
- k: `{4,8}`.
- seeds: `{0,1,2,3,4}`.
- corruptions: Gaussian noise, blur, brightness/contrast, JPEG.

Main artifacts:

- `outputs/paper_tables/sw_cad_image_views_visa_full_k4k8_s0s4_combined.csv`
- `outputs/paper_tables/visa_full_conformal_main_table.md`
- `outputs/paper_tables/visa_full_conformal_extended_summary.csv`
- `outputs/paper_tables/visa_full_conformal_vs_baselines_k_corruption.csv`
- `outputs/paper_tables/visa_full_conformal_reliability_bins.csv`
- `outputs/paper_tables/visa_full_conformal_selective_reliability.csv`
- `outputs/figures/visa_full_conformal_figure_manifest.md`

Key full VisA result for LOIO conformal:

| Split | AUROC | AP | ECE | Brier | NLL |
|---|---:|---:|---:|---:|---:|
| all k4/k8 | 0.8234 | 0.8458 | 0.0766 | 0.1875 | 0.6861 |
| k=4 | 0.8200 | 0.8415 | 0.0391 | 0.1868 | 0.7598 |
| k=8 | 0.8281 | 0.8512 | 0.1140 | 0.1881 | 0.6124 |

Comparison with prior calibrators under k/corruption:

- k=4: LOIO conformal ECE is about `0.036-0.043` across all corruptions, much lower than Vector Platt around `0.269-0.288` and Shift-Aware around `0.211-0.276`.
- k=8: LOIO conformal ECE is about `0.108-0.123`, lower than Vector Platt around `0.190-0.212` and Shift-Aware around `0.144-0.191`.
- Weighted conformal is mixed: it beats LOIO on k=8 blur/brightness/JPEG ECE, but fails under k=4 and Gaussian noise. Keep it as an ablation, not the main method.

Interpretation:

- Full VisA strongly supports the reliability claim.
- LOIO conformal is the current main reliability layer.
- The k=8 caveat is real: normal mean conformal probability rises from `0.3645` at k=4 to `0.4665` at k=8, while anomaly mean rises from `0.6494` to `0.7671`. Separation improves slightly, but normal overconfidence increases ECE.
- This means k=8 improves ranking/AP and anomaly confidence, but calibration becomes less conservative for normal samples.

Paper-safe claim after full VisA:

> On the full VisA k4/k8 corruption benchmark, LOIO conformal reliability reduces ECE substantially compared with Vector Platt and Shift-Aware Platt across all tested corruptions, while preserving the PCA/subspace ranking. The strongest effect is at k=4; k=8 remains better than Platt baselines but shows normal-sample overconfidence that should be discussed as a limitation.
