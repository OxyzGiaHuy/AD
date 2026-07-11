# Run anomalydino_mvtec_carpet_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_carpet_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9992562409636175`
- `auroc`: `0.9975922953451043`
- `brier`: `0.7235705482102794`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7304815271089218`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01255941252486828`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `6.0`
- `nll`: `2.8222166228782024`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_carpet_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
