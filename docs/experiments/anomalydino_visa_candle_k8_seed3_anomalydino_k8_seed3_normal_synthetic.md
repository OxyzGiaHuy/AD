# Run anomalydino_visa_candle_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_candle_k8_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8623136371409074`
- `auroc`: `0.8963`
- `brier`: `0.49154828111951`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4868432652193587`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.06483396602794528`
- `max_f1`: `0.8544600938967136`
- `model_storage_mb`: `6.0`
- `nll`: `2.4276726720240944`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_candle_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
