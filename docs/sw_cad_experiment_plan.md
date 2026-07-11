# SW-CAD Prototype Plan

## Mục tiêu

Kiểm tra liệu lớp conformal reliability lấy cảm hứng từ `Methode for SW-CAD.pdf` có bổ sung được claim mới cho hệ hiện tại: DINOv2 frozen + PCA/subspace residual + calibrated head.

Điểm mới muốn test không phải AUROC, mà là khả năng báo p-value, false-alarm control và effective sample size dưới corruption/domain shift.

## Method

- Ranking chính vẫn là PCA/subspace residual trên patch tokens DINOv2.
- Conformal layer nhận residual score và sinh:
  - patch-level p-values;
  - image-level p-values;
  - patch rejection mask bằng Benjamini-Hochberg FDR;
  - image false alarm rate ở mức alpha.
- Ba mode:
  - `insample_conformal`: fit PCA và calibrate trên cùng support, dùng như leakage baseline.
  - `loio_conformal`: leave-one-image-out khi k >= 2; k = 1 dùng spatial split chẵn/lẻ.
  - `weighted_conformal`: thêm density-ratio weighting bằng logistic domain classifier trên PCA-compressed features.

## Metrics

- `false_alarm_rate` trên normal test images.
- `coverage_gap = false_alarm_rate - alpha`.
- `image_p_auroc` và `image_p_ap` chỉ là diagnostic cho p-value ranking.
- `raw_auroc` và `raw_ap` là ranking chính của PCA residual.
- `patch_rejection_rate` từ BH-FDR.
- `n_eff_patch`, `n_eff_image` để biết density-ratio weighting còn đáng tin không.

## Acceptance

- LOIO phải ít anti-conservative hơn in-sample trên normal false alarm hoặc ít nhất cho thấy sự khác biệt rõ.
- Weighted conformal chỉ được claim khi `n_eff` hợp lý và cải thiện false alarm/coverage dưới structured shift.
- Không claim conformal AD là mới nói chung; claim chỉ là tích hợp vào low-storage few-shot DINOv2 subspace detector và benchmark transfer/shift.
