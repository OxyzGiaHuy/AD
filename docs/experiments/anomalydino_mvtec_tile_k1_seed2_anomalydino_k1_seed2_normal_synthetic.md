# Run anomalydino_mvtec_tile_k1_seed2_anomalydino_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9923066930014978`
- `auroc`: `0.9819624819624819`
- `brier`: `0.28205128205128205`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28205128205128205`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0052347500991617515`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `2.00537109375`
- `nll`: `5.195576625851375`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_tile_k1_seed2_anomalydino_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
