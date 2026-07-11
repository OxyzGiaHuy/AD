# Run ablation_calib_upper_mvtec_grid_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_grid_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9906732848830863`
- `auroc`: `0.9789377289377289`
- `brier`: `0.055478697854935956`
- `calibration_anomaly_val_count`: `5`
- `ece`: `0.08230252398101431`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0038138139890889597`
- `max_f1`: `0.9719626168224299`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.19887676493528833`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_grid_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
