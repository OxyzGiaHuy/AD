# Novelty Claim Explained 2: Trạng Thái Hiện Tại Và Hướng Claim Q1

Tài liệu này cập nhật tình hình sau khi hoàn thiện phần lớn P0/P1. Bản v1
`docs/novelty_claims_explained.md` giải thích bài toán và flow method từ đầu.
Bản v2 này tập trung vào câu hỏi thực dụng hơn: với kết quả hiện tại, paper Q1
nên claim gì, không nên claim gì, và nên chạy tiếp experiment nào để tăng
novelty.

## 1. Trạng Thái Hiện Tại

**P0 đã xong.** Các artifact chính đã có:

- Pixel metrics MVTec full: `1500` rows trong
  `outputs/paper_tables/pixel_metrics_detailed.csv`.
- Calibration ablation MVTec: `900` rows trong
  `outputs/paper_tables/calibration_ablation_detailed.csv`.
- Heatmap renderer đã có và đã smoke test được.
- Test suite hiện tại: `19 passed, 1 skipped`.

**P1 phần chính đã xong.** Các artifact chính:

- MVTec to VisA transfer: `240` rows trong
  `outputs/paper_tables/mvtec_to_visa_transfer_detailed.csv`.
- VisA corruption robustness đã aggregate trong
  `outputs/paper_tables/visa_robustness_all_summary.csv`.
- FGSM sweep đã đủ `900/900` runs:
  - `2/255`: `300/300`
  - `4/255`: `300/300`
  - `8/255`: `300/300`
  - summary: `outputs/paper_tables/mvtec_fgsm_sweep_summary.csv`.

**P2 mới một phần.** Đã có runtime/efficiency audit, nhưng chưa thể coi là xong:

- Official SubspaceAD reproduction chưa chạy.
- LoRA/adapter thật chưa implement/chạy đầy đủ.
- Selective prediction/risk-coverage chưa có thành bảng paper-ready.

Kết luận trạng thái: dữ liệu hiện tại đủ để viết một câu chuyện paper theo
hướng **calibration + efficiency + transfer/robustness diagnostics**, nhưng chưa
đủ để claim SOTA AUROC hay adversarial robustness.

## 2. Kết Quả Chính Hiện Có

### MVTec clean

`calib_subspace_head` gần PatchCore/AnomalyDINO về AUROC nhưng không thắng toàn
diện:

- k1: `0.9038` vs PatchCore/AnomalyDINO `0.9143`
- k2: `0.9217` vs `0.9294`
- k4: `0.9371` vs `0.9418`
- k8: `0.9452` vs `0.9484`

Đây là lý do không nên viết "dẫn đầu toàn diện trên MVTec". Claim đúng hơn là "competitive
image-level AUROC with lower storage and better calibration".

### Efficiency và storage

`calib_subspace_head` có storage nhỏ hơn memory-bank baselines:

- `calib_subspace_head`: khoảng `0.472 MB`
- PatchCore/AnomalyDINO: khoảng `2.005 MB` ở k1, `4.011 MB` ở k2, và `6 MB` ở
  k4/k8 trong benchmark hiện tại
- cached-feature latency của `calib_subspace_head` trên MVTec: khoảng
  `0.0013s/image`

Claim tốt: method là một **low-storage calibrated alternative** cho memory-bank
few-shot anomaly detection.

### Calibration ablation

Vector Platt trên `[subspace_score, head_score, disagreement]` là điểm đáng
claim nhất. Kết quả ECE MVTec:

- Vector Platt:
  - k1: `0.2735`
  - k4: `0.2144`
  - k8: `0.1538`
- Scalar Platt:
  - k1: `0.3392`
  - k4: `0.2884`
  - k8: `0.3097`
- Raw sigmoid gần như không cải thiện, ECE quanh `0.277`.

Ý nghĩa: head/calibrator không nên thay PCA/subspace ranking, nhưng có ích cho
probability và uncertainty. Đây là core của "decoupled calibrated subspace
head".

### VisA clean

VisA cho câu chuyện AUROC mạnh hơn MVTec. `calib_subspace_head` vượt
PatchCore/AnomalyDINO trong benchmark hiện tại:

- k1: `0.8226` vs `0.8038`
- k2: `0.8534` vs `0.8387`
- k4: `0.8696` vs `0.8619`
- k8: `0.8796` vs `0.8729`

Đây là claim có điều kiện: "stronger on VisA in our benchmark", không viết
thành "dẫn đầu phổ quát".

### MVTec to VisA transfer

Transfer protocol: fit/tune calibrator trên MVTec, sang VisA chỉ dùng k normal
support để fit target PCA/subspace, không dùng anomaly label VisA cho main
calibration.

Kết quả AUROC:

- k1: `0.8226`
- k2: `0.8534`
- k4: `0.8696`
- k8: `0.8824`

ECE vẫn cao ở low-shot và giảm khi k tăng:

- k1: `0.4319`
- k2: `0.3905`
- k4: `0.3140`
- k8: `0.2324`

Claim đúng: MVTec-fitted calibrator transfer được sang VisA về ranking/AUROC,
nhưng calibration vẫn cần cải thiện, nhất là k1/k2.

### Pixel metrics

Pixel AUROC trên MVTec của calibrated subspace family rất tốt và tăng theo k:

- `calib_subspace_head`: k1 `0.9436`, k2 `0.9525`, k4 `0.9567`, k8 `0.9599`
- PatchCore/AnomalyDINO: k1 `0.9402`, k2 `0.9466`, k4 `0.9507`, k8 `0.9516`

Đây là một điểm có lợi cho paper: image AUROC trên MVTec không thắng toàn diện,
nhưng pixel AUROC của subspace ranking đang rất cạnh tranh, thậm chí cao hơn
memory-bank baselines trong bảng hiện tại.

### FGSM sweep

FGSM cho thấy method không robust trước tấn công adversarial:

- Clean AUROC:
  - k1 `0.9038`
  - k2 `0.9217`
  - k4 `0.9371`
  - k8 `0.9452`
- FGSM `2/255`: AUROC chỉ còn khoảng `0.1302` đến `0.1755`
- FGSM `4/255`: AUROC chỉ còn khoảng `0.2747` đến `0.3296`
- FGSM `8/255`: AUROC khoảng `0.4397` đến `0.4489`

Kết quả này non-monotonic: `2/255` tệ hơn `8/255`. Đây là dấu hiệu cần audit
attack objective/direction, targeted vs untargeted behavior, label handling, và
surrogate score sign. Trước khi viết paper, không nên diễn giải nó như một quy
luật robustness tổng quát. Claim an toàn là: **benchmark exposes severe
adversarial fragility and reveals that the current surrogate attack needs
direction/objective auditing**.

## 3. Verify Novelty Sau Khi Có Kết Quả Mới

### AnomalyDINO

AnomalyDINO đã làm frozen DINOv2 patch similarity/memory-bank few-shot anomaly
detection, có image-level và pixel-level output. Vì vậy:

- không claim DINOv2 few-shot AD là mới;
- không claim patch memory bank với DINOv2 là mới;
- không claim DINOv2 pixel anomaly map là mới.

Link: https://arxiv.org/abs/2405.14529

### SubspaceAD

SubspaceAD đã làm frozen DINOv2 + PCA/subspace residual, training-free, không
memory bank. Vì vậy:

- không claim PCA residual trên DINOv2 là mới;
- không claim subspace scoring không memory bank là mới;
- cần tách rõ phần của mình: calibration/head/disagreement/transfer benchmark.

Link: https://arxiv.org/abs/2602.23013

### Khan & Krawczyk 2025

Khan & Krawczyk đã đánh giá DINOv2-based few-shot AD về ECE, Platt scaling,
entropy và FGSM. Vì vậy:

- không claim benchmark calibration đầu tiên;
- không claim first FGSM benchmark;
- không claim Platt scaling là mới.

Link: https://arxiv.org/abs/2510.13643

Novelty còn lại hẹp hơn nhưng rõ hơn:

- decoupled ranking vs calibration;
- vector calibrator dùng `[subspace_score, head_score, disagreement]`;
- synthetic head dùng làm tín hiệu phụ cho probability/uncertainty, không thay
  ranking;
- unified empirical story gồm clean, pixel, calibration, storage, corruption,
  FGSM, và transfer.

## 4. Claim Hiện Tại Nên Viết

Claim mạnh nhất:

> A decoupled calibrated subspace head provides competitive few-shot anomaly
> detection with much lower storage than memory-bank methods and substantially
> better calibration, while enabling a unified transfer and robustness diagnostic
> benchmark.

Claim phụ:

- Vector Platt trên `[subspace_score, head_score, disagreement]` cải thiện ECE
  mà không thay thế PCA/subspace ranking.
- MVTec-fitted calibration transfer sang VisA với AUROC tăng theo k, nhưng
  calibration low-shot vẫn là vấn đề mở.
- Method có pixel AUROC rất cạnh tranh trên MVTec, trong khi image AUROC không
  phải SOTA toàn diện.
- Robustness benchmark cho thấy fragility rõ ràng, nên paper nên claim
  diagnostic/quantification, không claim robust.

Không claim:

- dẫn đầu toàn diện trên MVTec;
- first DINOv2 PCA/subspace method;
- first calibration/adversarial benchmark;
- robust trước tấn công adversarial;
- trainable adapter/LoRA nếu chưa implement và evaluate thật.

## 5. Plan Tiếp Theo Để Tăng Novelty

### P1-Finalize: khóa bảng và figure paper

1. Sinh reliability diagram data/figure cho raw, scalar Platt, isotonic, vector
   Platt.
2. Render qualitative heatmaps cho MVTec và VisA: clean, corruption, FGSM.
3. Tạo bảng paper-ready gồm:
   - clean AUROC/AP/ECE/storage;
   - pixel AUROC/PRO;
   - MVTec to VisA transfer;
   - FGSM sweep;
   - corruption robustness.
4. Audit FGSM non-monotonic:
   - attack direction;
   - targeted/untargeted objective;
   - label handling;
   - score sign;
   - surrogate path có đúng với mục tiêu "increase anomaly score for normal" hay
     "decrease separation" không.

### P2-High Novelty Experiments

1. Official SubspaceAD comparison:
   - nếu chạy được code official thì report official;
   - nếu không, ghi rõ local reimplementation và protocol difference.
2. Selective prediction/uncertainty:
   - AURC;
   - risk-coverage;
   - entropy separation clean vs corrupted/adversarial.
3. Cross-dataset calibration ablation:
   - MVTec-transfer calibrator;
   - VisA normal_synthetic calibrator;
   - VisA upper-bound anomaly-val calibrator.
4. PCA128 high-accuracy setting:
   - full grid nếu compute cho phép;
   - nếu không, representative grid theo class/k để chứng minh accuracy-storage
     tradeoff.
5. LoRA/adapter:
   - chỉ làm nếu muốn giữ claim "trainable adapter";
   - nếu không, bỏ khỏi main paper để tránh làm loãng novelty.

## 6. Ưu Tiên Claim Mới

**Ưu tiên 1: Calibration under transfer and robustness shift.**  
Đây là hướng có novelty tốt nhất hiện tại. Thay vì chỉ nói Platt scaling raw
score, ta nói vector calibrator + disagreement giúp probability/uncertainty có
ích khi domain/perturbation shift.

**Ưu tiên 2: Low-storage calibrated alternative to memory bank.**  
Không cần thắng AUROC toàn diện. Nếu method gần AUROC, pixel AUROC mạnh, storage
thấp, latency thấp, và calibration tốt hơn, thì câu chuyện paper vẫn có giá trị
thực dụng.

**Ưu tiên 3: Robustness diagnostic benchmark, not robust method.**  
FGSM/corruption được dùng để chỉ ra giới hạn và để phân tích uncertainty/risk,
không để claim đã giải quyết robustness.

## 7. Acceptance Cho Vòng Tiếp Theo

- Không có overclaim trong docs/paper draft:
  - không có "dẫn đầu toàn diện trên MVTec";
  - không có "benchmark calibration đầu tiên";
  - không có "robust trước tấn công adversarial".
- `bash scripts/run_tests.sh` pass.
- Các file paper-ready tồn tại:
  - `outputs/paper_tables/mvtec_fgsm_sweep_summary.csv`;
  - `outputs/paper_tables/mvtec_to_visa_transfer_summary.csv`;
  - `outputs/paper_tables/calibration_ablation_summary.csv`;
  - `outputs/paper_tables/pixel_metrics_summary.csv`.
- `docs/research_log.md` và `docs/experiment_findings.md` ghi caveat về FGSM
  non-monotonic.


## Cập Nhật Sau Test-Plan Refresh Ngày 2026-07-02

- Đã refresh lại các artifact chính sau khi quota chạy lệnh được mở lại:
  - test suite: `19 passed, 1 skipped`;
  - FGSM sweep: `900` runs;
  - MVTec robustness: `6000` paired runs;
  - VisA robustness: `2872` paired runs;
  - pixel metrics: `1500` runs;
  - calibration ablation: `900` rows;
  - uncertainty aggregation: `14745` rows;
  - runtime audit: `4737` runs.
- Đã thêm artifact scripts:
  - `scripts/generate_calibration_curves.py` -> `outputs/paper_tables/calibration_reliability_bins_*`;
  - `scripts/aggregate_selective_risk.py` -> `outputs/paper_tables/selective_risk_*`;
  - `scripts/build_paper_ready_tables.py` -> `outputs/paper_tables/paper_ready_tables.md`.
- Đã render heatmap đại diện trong `outputs/figures/` cho MVTec clean, MVTec brightness/contrast, MVTec FGSM 8/255, và VisA clean.
- Claim cần chỉnh thêm: selective-risk hiện chưa ủng hộ câu “entropy giúp reject sample để tăng AUROC”. Low-entropy 50% coverage thường có AUROC thấp hơn full coverage. Vì vậy entropy hiện chỉ nên được dùng như **diagnostic signal** để phân tích shift/uncertainty, không phải claim selective prediction mạnh.
- Claim vẫn mạnh nhất sau refresh: **low-storage calibrated subspace detector** với AUROC cạnh tranh, calibration tốt hơn ở k lớn, pixel metrics tốt, transfer MVTec→VisA có xu hướng tăng theo k, và robustness benchmark chỉ ra giới hạn rõ ràng dưới FGSM.


## 8. Cập Nhật Cuối Sau Transfer Calibration Ablation Full

- P1 mở rộng đã hoàn tất: `outputs/paper_tables/transfer_calibration_ablation_detailed.csv` có `720` rows.
- MVTec-transfer normal_synthetic sang VisA giữ AUROC tốt và tăng theo k: k1 `0.8226`, k2 `0.8534`, k4 `0.8696`, k8 `0.8824`.
- ECE của transfer giảm khi có nhiều support normal hơn: k1 `0.4319`, k2 `0.3905`, k4 `0.3140`, k8 `0.2324`.
- VisA normal_synthetic calibration không đổi ranking nhưng tốt hơn ở k lớn: k8 ECE `0.2066`.
- VisA anomaly-val upper-bound tốt hơn ở k1 ECE `0.3787`, nhưng dùng anomaly label nên chỉ là upper-bound, không phải main protocol.
- Official SubspaceAD representative đã chạy và rất mạnh: average image AUROC `0.9518`, pixel AUROC `0.9710`. Điều này làm claim novelty phải hẹp và sắc hơn: không claim DINOv2 + PCA/subspace, chỉ claim decoupled calibration/head/transfer diagnostics.
- Trạng thái hiện tại đủ để viết paper draft theo framing **Calibration + Efficiency + Transfer/Robustness Diagnostics**.

### Claim sau cập nhật này

> A decoupled calibrated subspace head provides competitive low-storage few-shot anomaly detection, improves calibration as support grows, and enables a unified transfer/robustness diagnostic benchmark across MVTec and VisA.

### Claim vẫn phải tránh

- Không claim SOTA on MVTec.
- Không claim first calibration benchmark.
- Không claim adversarially robust.
- Không claim DINOv2 PCA residual is novel.


## 9. Cập Nhật Sau Full VisA PCA128 Và Shift-Aware Calibration

Hai hướng ưu tiên đã được chạy kỹ trên full VisA: PCA128 và Shift-Aware Calibration.

### PCA128 cho accuracy-storage tradeoff

Bản PCA64 cũ lưu rất ít thông tin subspace, khoảng `0.472 MB`. PCA128 tăng số component PCA, tức là giữ lại nhiều chiều subspace normal hơn, nên storage tăng nhẹ lên khoảng `0.566 MB`. Kết quả full VisA cho thấy AUROC tăng đều theo mọi k:

- k1: `0.8226 -> 0.8335`;
- k2: `0.8534 -> 0.8684`;
- k4: `0.8696 -> 0.8852`;
- k8: `0.8796 -> 0.8967`.

Điều này tạo claim hợp lý hơn: không phải model thắng mọi thứ, mà là có một điểm tradeoff tốt giữa accuracy và storage. So với memory bank, detector vẫn rất nhẹ.

### Shift-Aware Calibration cho reliability

Shift-Aware Calibration là biến thể calibrator thêm feature liên quan đến mức độ lệch/shift của score, nhằm giúp logistic calibrator biết khi nào raw score đến từ vùng phân phối khó tin cậy hơn. Nó không thay ranking nên AUROC giữ nguyên, nhưng xác suất anomaly đáng tin hơn ở k lớn.

Trên full VisA:

- k1 ECE: `0.4295 -> 0.4320`, hơi xấu hơn;
- k2 ECE: `0.3780 -> 0.3768`, gần như hòa;
- k4 ECE: `0.2839 -> 0.2032`, tốt hơn rõ;
- k8 ECE: `0.2066 -> 0.1447`, tốt hơn rõ.

NLL cũng giảm ở mọi k, nên claim có thể nói Shift-Aware giúp probability quality, đặc biệt khi có đủ support normal hơn.

### Claim mới mạnh hơn

Claim nên theo hướng:

> Method không cố thay thế subspace residual để ranking. Thay vào đó, nó giữ subspace residual làm anomaly ranking, dùng PCA128 để cải thiện accuracy-storage Pareto, và dùng shift-aware vector calibration để cải thiện độ tin cậy xác suất dưới dataset shift.

### Cẩn thận khi viết paper

- Không nói Shift-Aware tốt hơn ở mọi k, vì k1 ECE chưa tốt.
- Không nói PCA128 là novelty cốt lõi; đây là ablation tradeoff, không phải phát minh mới.
- Không nói thắng SubspaceAD về accuracy, vì official SubspaceAD representative rất mạnh.
- Novelty nên nằm ở tổ hợp: decoupled ranking/calibration, shift-aware vector calibrator, transfer/calibration benchmark, và low-storage evidence.
