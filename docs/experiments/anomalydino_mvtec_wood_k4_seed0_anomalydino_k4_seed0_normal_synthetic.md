# Run anomalydino_mvtec_wood_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_wood_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9742341555231696`
- `auroc`: `0.9342105263157895`
- `brier`: `0.7281301790010948`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7348479638701376`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012557065703823596`
- `max_f1`: `0.9672131147540983`
- `model_storage_mb`: `6.0`
- `nll`: `2.9552463739949575`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_wood_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
