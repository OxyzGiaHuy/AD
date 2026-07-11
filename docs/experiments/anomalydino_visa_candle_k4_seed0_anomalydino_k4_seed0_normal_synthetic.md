# Run anomalydino_visa_candle_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_candle_k4_seed0.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8461472813468532`
- `auroc`: `0.8801`
- `brier`: `0.4914298281880569`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48680576005834153`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.08713292227126658`
- `max_f1`: `0.8440366972477065`
- `model_storage_mb`: `6.0`
- `nll`: `2.427174978833135`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_candle_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
