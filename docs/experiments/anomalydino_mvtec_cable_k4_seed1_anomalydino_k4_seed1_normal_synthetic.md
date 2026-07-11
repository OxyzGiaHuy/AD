# Run anomalydino_mvtec_cable_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_cable_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9506862365908435`
- `auroc`: `0.9044227886056971`
- `brier`: `0.604525214937072`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6033543787058442`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012445633361736933`
- `max_f1`: `0.8681318681318682`
- `model_storage_mb`: `6.0`
- `nll`: `3.108648570598515`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_cable_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
