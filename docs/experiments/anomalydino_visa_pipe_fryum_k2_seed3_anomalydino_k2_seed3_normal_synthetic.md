# Run anomalydino_visa_pipe_fryum_k2_seed3_anomalydino_k2_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pipe_fryum_k2_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9982845923272865`
- `auroc`: `0.9968`
- `brier`: `0.3333333333333333`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33333333333333337`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.10179631260534128`
- `max_f1`: `0.9950248756218906`
- `model_storage_mb`: `4.0107421875`
- `nll`: `6.140226919642535`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_visa_pipe_fryum_k2_seed3_anomalydino_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
