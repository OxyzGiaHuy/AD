# Run anomalydino_mvtec_capsule_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_capsule_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9714614486531268`
- `auroc`: `0.877143996808935`
- `brier`: `0.8114125919013864`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8156747810584917`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012428504880517721`
- `max_f1`: `0.9321266968325792`
- `model_storage_mb`: `6.0`
- `nll`: `3.992182896711652`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_capsule_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
