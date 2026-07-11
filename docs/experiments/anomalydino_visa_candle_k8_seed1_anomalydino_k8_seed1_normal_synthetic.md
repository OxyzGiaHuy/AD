# Run anomalydino_visa_candle_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_candle_k8_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9057988369939399`
- `auroc`: `0.9059`
- `brier`: `0.4915748168909576`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48673208996537143`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09011051795445382`
- `max_f1`: `0.848780487804878`
- `model_storage_mb`: `6.0`
- `nll`: `2.437184301072659`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_candle_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
