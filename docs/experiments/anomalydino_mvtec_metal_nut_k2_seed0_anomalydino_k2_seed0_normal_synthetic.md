# Run anomalydino_mvtec_metal_nut_k2_seed0_anomalydino_k2_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_metal_nut_k2_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9940151108179327`
- `auroc`: `0.9755620723362659`
- `brier`: `0.19130434782608696`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19130434782608696`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008751638233661652`
- `max_f1`: `0.9787234042553191`
- `model_storage_mb`: `4.0107421875`
- `nll`: `3.5239563233600646`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_metal_nut_k2_seed0_anomalydino_k2_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
