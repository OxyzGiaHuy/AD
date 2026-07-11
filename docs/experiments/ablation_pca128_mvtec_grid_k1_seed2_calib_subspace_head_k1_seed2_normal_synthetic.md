# Run ablation_pca128_mvtec_grid_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_grid_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9438239646881786`
- `auroc`: `0.8788638262322472`
- `brier`: `0.2690988173407206`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26916412206796503`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002667001448571682`
- `max_f1`: `0.9243697478991597`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.0821049435214425`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_grid_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
