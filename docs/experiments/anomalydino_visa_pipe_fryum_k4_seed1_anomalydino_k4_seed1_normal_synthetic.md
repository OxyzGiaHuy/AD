# Run anomalydino_visa_pipe_fryum_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pipe_fryum_k4_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9830129853775819`
- `auroc`: `0.9686`
- `brier`: `0.6398820257963576`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.641706737037748`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.11664761487394572`
- `max_f1`: `0.9514563106796117`
- `model_storage_mb`: `6.0`
- `nll`: `2.61263344955872`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pipe_fryum_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
