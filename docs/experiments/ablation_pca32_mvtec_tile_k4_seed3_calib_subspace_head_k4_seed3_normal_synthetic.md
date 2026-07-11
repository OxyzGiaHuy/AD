# Run ablation_pca32_mvtec_tile_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9912600067158411`
- `auroc`: `0.9794372294372294`
- `brier`: `0.09249827708618594`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12147754534251162`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026522865916928672`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.3258576755566481`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_tile_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
