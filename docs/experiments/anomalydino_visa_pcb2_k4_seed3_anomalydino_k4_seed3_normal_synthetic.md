# Run anomalydino_visa_pcb2_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb2_k4_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.6996960926819716`
- `auroc`: `0.7182`
- `brier`: `0.4783336860302239`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.47502929089590906`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.10021052259951829`
- `max_f1`: `0.7109004739336493`
- `model_storage_mb`: `6.0`
- `nll`: `1.9378311079419723`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb2_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
