# Run anomalydino_mvtec_bottle_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_bottle_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9981765446147077`
- `auroc`: `0.9944444444444445`
- `brier`: `0.7433096279513387`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7433074192138366`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012510004823645914`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `6.0`
- `nll`: `3.5105644803226403`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_bottle_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
