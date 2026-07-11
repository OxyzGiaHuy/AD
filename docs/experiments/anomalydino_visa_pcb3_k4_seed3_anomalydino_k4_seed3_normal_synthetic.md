# Run anomalydino_visa_pcb3_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k4_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8017294479228764`
- `auroc`: `0.8024752475247525`
- `brier`: `0.47583855738715414`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.47139280351963064`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0920860080039175`
- `max_f1`: `0.7559808612440191`
- `model_storage_mb`: `6.0`
- `nll`: `1.9176115977853925`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
