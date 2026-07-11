# Run anomalydino_mvtec_hazelnut_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9890657813677525`
- `auroc`: `0.9803571428571428`
- `brier`: `0.5046920654020287`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5202630663459951`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012557198699902404`
- `max_f1`: `0.9402985074626866`
- `model_storage_mb`: `6.0`
- `nll`: `1.4280791031200577`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
