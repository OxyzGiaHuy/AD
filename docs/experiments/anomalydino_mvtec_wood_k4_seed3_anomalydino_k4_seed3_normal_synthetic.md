# Run anomalydino_mvtec_wood_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_wood_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9841633742767669`
- `auroc`: `0.9543859649122807`
- `brier`: `0.7570674246396611`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7565275038193906`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01261388074276568`
- `max_f1`: `0.959349593495935`
- `model_storage_mb`: `6.0`
- `nll`: `5.010282330040727`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_wood_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
