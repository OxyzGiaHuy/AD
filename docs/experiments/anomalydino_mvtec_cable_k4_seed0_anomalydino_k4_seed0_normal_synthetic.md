# Run anomalydino_mvtec_cable_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_cable_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9564555329513548`
- `auroc`: `0.9190404797601199`
- `brier`: `0.5906344653439894`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5895807924121618`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012561934404075145`
- `max_f1`: `0.8736842105263158`
- `model_storage_mb`: `6.0`
- `nll`: `2.477875476205594`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_cable_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
