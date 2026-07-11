# Run anomalydino_mvtec_carpet_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_carpet_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9991314288990252`
- `auroc`: `0.9971910112359551`
- `brier`: `0.739498641004422`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.740117790667006`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012921106340920823`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `6.0`
- `nll`: `3.2614766957497467`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_carpet_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
