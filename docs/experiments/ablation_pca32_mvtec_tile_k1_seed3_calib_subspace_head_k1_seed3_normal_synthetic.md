# Run ablation_pca32_mvtec_tile_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.992655220911912`
- `auroc`: `0.9823232323232324`
- `brier`: `0.24877975238696218`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2262955236638713`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021898363454219624`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.8415843502674853`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
