# Run anomalydino_mvtec_capsule_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_capsule_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9779154479521625`
- `auroc`: `0.9034702832070204`
- `brier`: `0.8017005159550914`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8090411564793833`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01273503548211672`
- `max_f1`: `0.9357798165137615`
- `model_storage_mb`: `6.0`
- `nll`: `3.5342941165077812`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_capsule_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
