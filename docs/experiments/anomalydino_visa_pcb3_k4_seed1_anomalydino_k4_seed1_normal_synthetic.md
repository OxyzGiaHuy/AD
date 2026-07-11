# Run anomalydino_visa_pcb3_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k4_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7838766831382942`
- `auroc`: `0.8070297029702971`
- `brier`: `0.4876651875660247`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48480008325924107`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0742854922453859`
- `max_f1`: `0.774468085106383`
- `model_storage_mb`: `6.0`
- `nll`: `2.3275216939663275`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
