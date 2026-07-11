# Run anomalydino_mvtec_capsule_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_capsule_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9760204807745188`
- `auroc`: `0.8970881531711209`
- `brier`: `0.8191041904302485`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8207865397782756`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012691639363765717`
- `max_f1`: `0.9375`
- `model_storage_mb`: `6.0`
- `nll`: `4.652571735050868`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_capsule_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
