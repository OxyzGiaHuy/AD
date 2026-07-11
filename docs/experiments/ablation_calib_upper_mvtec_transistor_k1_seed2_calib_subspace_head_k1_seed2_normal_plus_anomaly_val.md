# Run ablation_calib_upper_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7272744814598071`
- `auroc`: `0.7893518518518519`
- `brier`: `0.42753722347560136`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.480673762348791`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003128185848860691`
- `max_f1`: `0.6739130434782609`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.6397311166424668`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
