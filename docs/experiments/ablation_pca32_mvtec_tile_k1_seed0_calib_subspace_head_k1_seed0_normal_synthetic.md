# Run ablation_pca32_mvtec_tile_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9922016304124478`
- `auroc`: `0.9819624819624819`
- `brier`: `0.27883308698890186`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2804024311212393`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001821562552299255`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.02846577293129`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
