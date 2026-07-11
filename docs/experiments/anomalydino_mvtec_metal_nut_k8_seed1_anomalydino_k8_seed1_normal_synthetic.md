# Run anomalydino_mvtec_metal_nut_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9967555939888826`
- `auroc`: `0.9863147605083089`
- `brier`: `0.774559817443635`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7835908505660684`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012385747938052468`
- `max_f1`: `0.9789473684210527`
- `model_storage_mb`: `6.0`
- `nll`: `3.134267261348468`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_metal_nut_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
