# Run ablation_calib_upper_mvtec_toothbrush_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9717974200292958`
- `auroc`: `0.9382716049382716`
- `brier`: `0.12717258351704283`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.15440937098211202`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015022333902426255`
- `max_f1`: `0.9310344827586207`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5713222470957489`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
