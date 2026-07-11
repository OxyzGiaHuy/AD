# Run ablation_pca16_mvtec_cable_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_cable_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8376749071004612`
- `auroc`: `0.7708020989505248`
- `brier`: `0.23502159407639045`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22663877844461244`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028347806880871453`
- `max_f1`: `0.8095238095238095`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.0028879396225605`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_cable_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
