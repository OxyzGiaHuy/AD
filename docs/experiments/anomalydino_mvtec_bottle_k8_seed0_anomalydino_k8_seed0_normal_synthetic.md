# Run anomalydino_mvtec_bottle_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9961161021368834`
- `auroc`: `0.9888888888888889`
- `brier`: `0.4337962660322561`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.589065142783774`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012340770787503346`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `6.0`
- `nll`: `1.100283691287644`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_bottle_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
