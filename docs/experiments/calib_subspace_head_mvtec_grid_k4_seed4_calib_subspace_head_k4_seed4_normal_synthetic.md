# Run calib_subspace_head_mvtec_grid_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_grid_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9988150200061557`
- `auroc`: `0.9966583124477861`
- `brier`: `0.25276931950570375`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2595979426151666`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013240733160040318`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.6086717896365603`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_grid_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
