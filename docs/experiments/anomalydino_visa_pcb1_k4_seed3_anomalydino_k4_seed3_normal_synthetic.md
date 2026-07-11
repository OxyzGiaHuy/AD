# Run anomalydino_visa_pcb1_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb1_k4_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.6972267333674768`
- `auroc`: `0.7509`
- `brier`: `0.43102837348409734`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4216738585755229`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.08010784465819597`
- `max_f1`: `0.7272727272727273`
- `model_storage_mb`: `6.0`
- `nll`: `1.3384838420129006`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb1_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
