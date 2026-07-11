# Run anomalydino_mvtec_bottle_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_bottle_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.998983801734063`
- `auroc`: `0.9968253968253968`
- `brier`: `0.7216210011924595`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7290410527353546`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012395038190914923`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `6.0`
- `nll`: `2.8169089384192594`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_bottle_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
