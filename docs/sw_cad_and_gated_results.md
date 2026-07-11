# SW-CAD Và Gated Shift-Aware Results

## Trạng thái hiện tại

- Đã implement `src/conformal.py` cho conformal p-values, LOIO/spatial split, weighted conformal và density-ratio logistic.
- Đã implement `src/calibration/gated.py` cho normalize gate, trộn probability và rule/soft gates.
- Đã thêm `sample_weight` cho `VectorPlattScaler`.
- Đã thêm scripts:
  - `scripts/evaluate_sw_cad.py`
  - `scripts/evaluate_gated_shift_aware.py`
- Unit tests hiện tại: `26 passed, 1 skipped`.

## Smoke test

- VisA `candle`, k=4, seed=0, corruptions `blur`, `gaussian_noise`, max 10 images: chạy xong cho cả SW-CAD và gated.
- MVTec `bottle`, k=4, seed=0, corruptions `blur`, `gaussian_noise`, max 10 images: chạy xong cho cả SW-CAD và gated.

## Finding ban đầu

- Gated calibration giữ AUROC/AP không đổi so với Vector Platt, đúng thiết kế vì chỉ đổi probability.
- Trên MVTec smoke blur, shift-aware/weighted/gated giảm ECE so với Vector Platt.
- Trên Gaussian noise smoke, gate không làm ECE tệ đáng kể so với Vector Platt.
- SW-CAD sinh đủ p-values, false alarm, patch rejection và `n_eff`.
- Weighted conformal có thể làm p-value ranking thay đổi mạnh; vì vậy p-value AUROC chỉ nên dùng diagnostic, không thay thế raw PCA ranking.

## Output tables

- `outputs/paper_tables/sw_cad_conformal_summary.csv`
- `outputs/paper_tables/sw_cad_weighted_conformal_delta.csv`
- `outputs/paper_tables/gated_shift_aware_summary.csv`
- `outputs/paper_tables/gated_shift_aware_delta.csv`
- `outputs/paper_tables/gated_shift_aware_oracle_gap.csv`

## Claim tạm thời

Claim vẫn ở mức prototype: SW-CAD và gated calibration là hướng có tín hiệu, nhưng cần representative grid trước khi đưa vào paper.

Không claim:

- adversarial robustness;
- conformal AD đầu tiên;
- SOTA AUROC;
- gate deployment hoàn chỉnh.
