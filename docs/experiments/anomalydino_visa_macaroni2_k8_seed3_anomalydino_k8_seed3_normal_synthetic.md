# Run anomalydino_visa_macaroni2_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_macaroni2_k8_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7834626913499441`
- `auroc`: `0.788`
- `brier`: `0.48429281759604076`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48120289913844316`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09756771810352802`
- `max_f1`: `0.7447698744769874`
- `model_storage_mb`: `6.0`
- `nll`: `2.102077259709198`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_macaroni2_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
