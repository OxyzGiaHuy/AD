# Run anomalydino_mvtec_tile_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_tile_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.998555321903316`
- `auroc`: `0.9963924963924964`
- `brier`: `0.7094683871552604`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7055519894800253`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01267840038252692`
- `max_f1`: `0.9882352941176471`
- `model_storage_mb`: `6.0`
- `nll`: `3.8475588136742274`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_tile_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
