# SAGE-Style Gate Experiments For Shift-Aware Calibration

Date: 2026-07-09

## Mục tiêu

Test tiếp ba idea để giữ claim Gated Shift-Aware Calibration theo hướng mạnh hơn nhưng không overclaim:

1. `Class-Held-Out Learned Gate`: gate học từ các class khác và test trên class unseen.
2. `Risk-Aware Gate`: gate chỉ rời Vector Platt khi predicted ECE gain đủ lớn, nhằm tối ưu no-harm/worst-case thay vì mean ECE đơn thuần.
3. `SAGE-Style Hierarchical Gate`: gate hai tầng theo tinh thần SAGE, gồm shared/safe anchor gate và dynamic expert selection.

Ngoài ra test thêm `view_experts`, không chỉ calibrator đơn lẻ:

- `vector_platt`: safe probability view.
- `shift_aware_vector_platt`: shift descriptor view.
- `weighted_platt`: density-ratio view.
- `anchored_structured_gate`: anchored routing view.

## SAGE được tham khảo như thế nào

Code SAGE trong `SAGE/sage/components/router.py` dùng các ý chính:

- shared expert gate `g_s` để cân bằng shared/safe path và dynamic expert path;
- query-key affinity routing;
- top-k expert selection;
- gating weights;
- load-balance/statistics cho expert usage.

Trong AD task này, mình không dùng segmentation backbone của SAGE. Mình chuyển nguyên lý sang calibration/reliability layer:

- shared path = `vector_platt` anchor;
- dynamic experts = shift-aware, weighted, anchored/view experts;
- input routing features = `n_eff_ratio`, domain confidence, PCA concentration, k-shot, corruption/dataset descriptors;
- output = chọn expert/view theo case class-held-out hoặc cross-dataset.

## Files đã thêm

- `src/calibration/offline_sage_gate.py`
- `scripts/evaluate_sage_style_gate_offline.py`
- updated tests in `tests/test_conformal_and_gated.py`

Verification:

```text
30 passed, 1 skipped
```

Command:

```bash
/home/crl/miniconda3/envs/ad/bin/python scripts/evaluate_sage_style_gate_offline.py --run-tag sage_style_gate_offline_full
```

Outputs:

- `outputs/paper_tables/sage_style_gate_offline_full_detailed.csv`
- `outputs/paper_tables/sage_style_gate_offline_full_summary.csv`

## Kết quả chính

### Pool 1: calibration experts

Experts: `vector_platt`, `shift_aware_vector_platt`, `weighted_platt`.

| Split | Best non-oracle gate | Mean ECE | Delta vs Vector | No-harm |
|---|---|---:|---:|---:|
| Leave-one-class-out | `risk_aware_margin_0.01` | 0.1938 | -0.0222 | 596/648 |
| Leave-one-class-out | `class_heldout_logistic_top1` | 0.1943 | -0.0217 | 608/648 |
| VisA -> MVTec | `sage_hier_shared_dynamic_t0.7` | 0.1963 | +0.0011 | 307/360 |
| MVTec -> VisA | `risk_aware_margin_0` | 0.2292 | -0.0128 | 286/288 |

Oracle room:

- Leave-one-class-out oracle: ECE 0.1842, delta -0.0318.
- VisA -> MVTec oracle: ECE 0.1853, delta -0.0099.
- MVTec -> VisA oracle: ECE 0.1829, delta -0.0592.

### Pool 2: view experts

Experts: `vector_platt`, `shift_aware_vector_platt`, `weighted_platt`, `anchored_structured_gate`.

| Split | Best non-oracle gate | Mean ECE | Delta vs Vector | No-harm |
|---|---|---:|---:|---:|
| Leave-one-class-out | `risk_aware_margin_0.01` | 0.1939 | -0.0221 | 595/648 |
| Leave-one-class-out | `sage_hier_shared_dynamic_t0.7` | 0.1955 | -0.0205 | 612/648 |
| VisA -> MVTec | `sage_hier_shared_dynamic_t0.7` | 0.1980 | +0.0028 | 282/360 |
| MVTec -> VisA | `risk_aware_margin_0` | 0.2256 | -0.0164 | 286/288 |

Oracle room:

- Leave-one-class-out oracle: ECE 0.1831, delta -0.0329.
- VisA -> MVTec oracle: ECE 0.1846, delta -0.0105.
- MVTec -> VisA oracle: ECE 0.1811, delta -0.0609.

## Diễn giải

### Idea 1: Class-Held-Out Learned Gate

Có tín hiệu tốt. Leave-one-class-out giảm ECE khoảng `0.021-0.022` so với Vector Platt trên 648 cases. Đây là evidence tốt hơn full MVTec/VisA static gate vì nó test unseen class, gần hơn với claim generalization.

Caveat: đây là offline gate trên case-level metrics, chưa phải sample-level probability gate. Cần nâng cấp nếu muốn đưa vào method chính.

### Idea 2: Risk-Aware Gate

Đây là idea triển vọng nhất hiện tại. `risk_aware_margin_0.01` cho LOCO tốt nhất trong pool calibrator: ECE `0.1938`, delta `-0.0222`. Nó hợp với claim safe routing vì không cố dùng dynamic expert mọi lúc.

Caveat: VisA -> MVTec vẫn hơi làm hại nếu gate học từ VisA và deploy sang MVTec. SAGE-style threshold 0.7 an toàn hơn trên hướng này: delta chỉ `+0.0011`.

### Idea 3: SAGE-Style Hierarchical Gate

Có ích nhất khi cross-dataset từ VisA sang MVTec. Threshold cao `t=0.7` làm gate conservative hơn, chọn Vector Platt nhiều hơn và giảm hại so với logistic/risk gate thường.

Điều này support thiết kế SAGE-like:

- shared/safe anchor trước;
- dynamic expert sau;
- threshold/top-k để tránh over-adaptation.

### View Experts Không Chỉ Là Calibrator

Thêm `anchored_structured_gate` như một routing view giúp MVTec->VisA tốt hơn (`0.2256`, delta `-0.0164`) so với calibrator-only best (`0.2292`, delta `-0.0128`). Đây là tín hiệu rằng expert nên được định nghĩa theo **view/reliability mechanism**, không chỉ theo calibrator family.

Tuy nhiên view expert chưa giúp VisA->MVTec; nó vẫn hơi làm hại. Do đó claim nên là `view-expert routing is promising`, chưa phải chốt.

## Claim cập nhật

Claim nên thử đẩy tiếp:

> A SAGE-inspired hierarchical, risk-aware gate can route between safe, shift-aware, density-ratio, and anchored reliability views. In class-held-out evaluation, it reduces calibration error while preserving the low-storage subspace ranking; under hard cross-dataset transfer, conservative shared-anchor routing prevents most over-adaptation.

Không claim:

- first gated anomaly detection;
- universal ECE improvement;
- sample-level deployed gate đã hoàn chỉnh;
- SAGE architecture copied to AD.

## Next Steps

1. Nâng offline case-level gate thành sample-level probability gate bằng cách lưu per-image expert probabilities trong `predictions.parquet` hoặc CSV.
2. Train learned gate với held-out classes, không dùng test anomaly labels trong main protocol; dùng synthetic/normal-only proxy hoặc validation classes.
3. Thử objective risk-aware trực tiếp: minimize ECE plus no-harm penalty.
4. Thêm view experts mới:
   - conformal p-value view từ SW-CAD;
   - entropy/selective prediction view;
   - clean-transfer Vector Platt view;
   - corruption-shift density-ratio view.
5. Làm novelty framing: SAGE-inspired routing at the reliability layer, not image segmentation routing.
