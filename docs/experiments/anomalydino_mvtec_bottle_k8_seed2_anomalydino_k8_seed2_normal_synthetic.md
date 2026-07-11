# Run anomalydino_mvtec_bottle_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_bottle_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9981765446147077`
- `auroc`: `0.9944444444444445`
- `brier`: `0.7463851347675968`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7456476885393396`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012607179065964308`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `6.0`
- `nll`: `3.6876081492509014`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_bottle_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
