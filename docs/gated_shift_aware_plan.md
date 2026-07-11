# Gated Shift-Aware Calibration Plan

## Mục tiêu

Tăng novelty của Shift-Aware Calibration bằng cơ chế gated experts lấy cảm hứng ở mức nguyên lý từ Thai SAGE: nhiều expert calibration và một gate chọn/trộn expert theo descriptor của shift.

Mục tiêu thực dụng: giữ lợi ích calibration trên blur/JPEG/brightness nhưng tránh làm tệ Gaussian noise.

## Experts

- `vector_platt`: Vector Platt gốc trên `[subspace_score, head_score, disagreement]`.
- `shift_aware_vector_platt`: thêm shift descriptors như norm shift, PCA residual mean/std/concentration.
- `weighted_platt`: Vector Platt có sample weight từ density-ratio weighting.
- `oracle_best`: upper bound chọn expert có ECE tốt nhất theo label test; không dùng cho claim deployment.

## Gates

- `structured_rule_gate`: hard gate theo loại corruption, dùng như diagnostic có nhãn shift.
- `soft_neff_gate`: oracle-free heuristic dùng `domain_confidence`, `n_eff_ratio`, `pca_concentration`.
- `oracle_best`: đo room còn lại nếu gate hoàn hảo.

## Metrics

- Mean ECE và worst-corruption ECE.
- Brier/NLL.
- No-harm count so với Vector Platt.
- Entropy shift.
- AUROC/AP phải giữ nguyên vì ranking vẫn là PCA/subspace residual.

## Caveat

Thai SAGE là segmentation và gated experts theo shape/domain, không phải anomaly detection. Paper hiện tại chỉ mượn ý tưởng routing/gating, không copy architecture hoặc claim direct extension.
