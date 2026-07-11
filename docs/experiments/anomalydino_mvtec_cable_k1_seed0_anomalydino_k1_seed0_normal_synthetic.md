# Run anomalydino_mvtec_cable_k1_seed0_anomalydino_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_cable_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9385221210841516`
- `auroc`: `0.8869940029985007`
- `brier`: `0.38666666666666666`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3866666666666667`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005050635449588298`
- `max_f1`: `0.8512820512820513`
- `model_storage_mb`: `2.00537109375`
- `nll`: `7.122663225185343`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_cable_k1_seed0_anomalydino_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
