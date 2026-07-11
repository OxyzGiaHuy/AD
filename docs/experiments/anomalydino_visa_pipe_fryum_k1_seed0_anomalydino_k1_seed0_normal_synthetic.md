# Run anomalydino_visa_pipe_fryum_k1_seed0_anomalydino_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pipe_fryum_k1_seed0.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9656742378814204`
- `auroc`: `0.9384`
- `brier`: `0.3333333333333333`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33333333333333337`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0551522512982289`
- `max_f1`: `0.9371980676328503`
- `model_storage_mb`: `2.00537109375`
- `nll`: `6.140226919642535`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_visa_pipe_fryum_k1_seed0_anomalydino_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
