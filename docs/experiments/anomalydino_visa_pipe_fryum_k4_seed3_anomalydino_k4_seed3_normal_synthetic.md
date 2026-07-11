# Run anomalydino_visa_pipe_fryum_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pipe_fryum_k4_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9979271896324916`
- `auroc`: `0.9952`
- `brier`: `0.6386133294288338`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6393703768029808`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.11385675905893246`
- `max_f1`: `0.99`
- `model_storage_mb`: `6.0`
- `nll`: `2.5755352885216545`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pipe_fryum_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
