# Run anomalydino_visa_capsules_k1_seed4_anomalydino_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_capsules_k1_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9605990478044453`
- `auroc`: `0.9428333333333333`
- `brier`: `0.375`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.375`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.09447303413180634`
- `max_f1`: `0.9215686274509803`
- `model_storage_mb`: `2.00537109375`
- `nll`: `6.9077552833478535`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_visa_capsules_k1_seed4_anomalydino_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
