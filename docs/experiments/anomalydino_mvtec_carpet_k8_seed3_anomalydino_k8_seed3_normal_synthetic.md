# Run anomalydino_mvtec_carpet_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_carpet_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9970011389013236`
- `auroc`: `0.9903691813804173`
- `brier`: `0.7572098373796804`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7547941660064742`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012471856820022957`
- `max_f1`: `0.9775280898876404`
- `model_storage_mb`: `6.0`
- `nll`: `4.752844267951045`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_carpet_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
