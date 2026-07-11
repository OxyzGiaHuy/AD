# Run ablation_pca64_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_wood_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9886949159873254`
- `auroc`: `0.968421052631579`
- `brier`: `0.1527358671809674`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1755002434778063`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00264772183344334`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.0725620625288665`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
