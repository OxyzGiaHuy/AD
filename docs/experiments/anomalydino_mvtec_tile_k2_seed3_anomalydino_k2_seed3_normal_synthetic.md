# Run anomalydino_mvtec_tile_k2_seed3_anomalydino_k2_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_tile_k2_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9986937105921248`
- `auroc`: `0.9967532467532467`
- `brier`: `0.28205128205128205`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28205128205128205`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.00872548047102924`
- `max_f1`: `0.9882352941176471`
- `model_storage_mb`: `4.0107421875`
- `nll`: `5.195576625851375`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_tile_k2_seed3_anomalydino_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
