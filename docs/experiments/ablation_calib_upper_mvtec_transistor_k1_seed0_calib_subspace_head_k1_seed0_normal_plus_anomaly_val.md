# Run ablation_calib_upper_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7365007789386029`
- `auroc`: `0.8018518518518518`
- `brier`: `0.40421902932158577`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.46342263029267394`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002820480517887821`
- `max_f1`: `0.6966292134831461`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2944807725880942`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
