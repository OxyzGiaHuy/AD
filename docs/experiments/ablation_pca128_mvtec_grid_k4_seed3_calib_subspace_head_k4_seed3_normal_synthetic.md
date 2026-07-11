# Run ablation_pca128_mvtec_grid_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_grid_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9993897326498338`
- `auroc`: `0.9983291562238931`
- `brier`: `0.25527402108331004`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26043029511586213`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00396051513365446`
- `max_f1`: `0.991304347826087`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.6698278575514491`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_grid_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
