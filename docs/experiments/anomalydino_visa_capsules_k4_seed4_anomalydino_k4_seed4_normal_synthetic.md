# Run anomalydino_visa_capsules_k4_seed4_anomalydino_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_capsules_k4_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9601297894359279`
- `auroc`: `0.9446666666666667`
- `brier`: `0.6146942579416944`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6121894490745035`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.10130477346247062`
- `max_f1`: `0.9306930693069307`
- `model_storage_mb`: `6.0`
- `nll`: `3.056032529982727`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_capsules_k4_seed4_anomalydino_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
