# Run anomalydino_visa_capsules_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_capsules_k8_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.964687863310852`
- `auroc`: `0.9428333333333333`
- `brier`: `0.6111741047558437`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6086838670933503`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.07963885322678835`
- `max_f1`: `0.9261083743842364`
- `model_storage_mb`: `6.0`
- `nll`: `2.864116830042647`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_capsules_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
