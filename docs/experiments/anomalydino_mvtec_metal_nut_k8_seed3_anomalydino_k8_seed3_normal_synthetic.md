# Run anomalydino_mvtec_metal_nut_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_metal_nut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9959468213722033`
- `auroc`: `0.9833822091886608`
- `brier`: `0.802475095472995`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8030661613336237`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012240224412601928`
- `max_f1`: `0.9738219895287958`
- `model_storage_mb`: `6.0`
- `nll`: `4.574062786539829`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_metal_nut_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
