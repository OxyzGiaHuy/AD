# Run ablation_pca64_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_grid_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9330423928463184`
- `auroc`: `0.8771929824561403`
- `brier`: `0.26904807737840297`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26913914160850727`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015958987701779758`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `3.8103122508084803`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
