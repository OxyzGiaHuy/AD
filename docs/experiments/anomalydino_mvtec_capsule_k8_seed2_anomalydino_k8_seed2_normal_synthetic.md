# Run anomalydino_mvtec_capsule_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_capsule_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9811903925071608`
- `auroc`: `0.9234144395692062`
- `brier`: `0.7974947225157809`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8053604919237621`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012367376323902246`
- `max_f1`: `0.9493087557603687`
- `model_storage_mb`: `6.0`
- `nll`: `3.3933894606965174`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_capsule_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
