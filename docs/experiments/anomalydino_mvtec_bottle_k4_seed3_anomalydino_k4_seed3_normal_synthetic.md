# Run anomalydino_mvtec_bottle_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_bottle_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9829813545891274`
- `auroc`: `0.9595238095238096`
- `brier`: `0.6713907540928562`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6959101592740381`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012617790353405907`
- `max_f1`: `0.984375`
- `model_storage_mb`: `6.0`
- `nll`: `2.1503292137499024`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_bottle_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
