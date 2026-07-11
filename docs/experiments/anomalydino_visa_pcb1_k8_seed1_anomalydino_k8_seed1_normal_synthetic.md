# Run anomalydino_visa_pcb1_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb1_k8_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7804020542949304`
- `auroc`: `0.8232`
- `brier`: `0.41535115006259987`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4008986686915159`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09135443899780511`
- `max_f1`: `0.7725321888412017`
- `model_storage_mb`: `6.0`
- `nll`: `1.2355356544149454`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb1_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
