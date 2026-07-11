# Run anomalydino_visa_candle_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_candle_k4_seed2.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8856948602112356`
- `auroc`: `0.9024`
- `brier`: `0.48312267512489804`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4770900531671941`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.08854724254459143`
- `max_f1`: `0.8558139534883721`
- `model_storage_mb`: `6.0`
- `nll`: `2.0629665517967273`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_candle_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
