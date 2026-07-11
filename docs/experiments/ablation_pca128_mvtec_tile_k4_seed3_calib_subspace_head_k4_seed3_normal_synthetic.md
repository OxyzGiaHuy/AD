# Run ablation_pca128_mvtec_tile_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.997433106719434`
- `auroc`: `0.9938672438672439`
- `brier`: `0.09189431849517651`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14144596594393757`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002256295970107755`
- `max_f1`: `0.9880952380952381`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.3505385691935394`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
