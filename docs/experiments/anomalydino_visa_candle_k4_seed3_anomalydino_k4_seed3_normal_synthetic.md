# Run anomalydino_visa_candle_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_candle_k4_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8726194897275669`
- `auroc`: `0.8948`
- `brier`: `0.4970148480801567`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.49478543934732444`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.05484736485406756`
- `max_f1`: `0.8446601941747572`
- `model_storage_mb`: `6.0`
- `nll`: `2.9831794131004203`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_candle_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
