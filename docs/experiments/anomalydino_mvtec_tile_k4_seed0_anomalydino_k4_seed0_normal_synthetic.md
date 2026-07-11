# Run anomalydino_mvtec_tile_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_tile_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9941704857770762`
- `auroc`: `0.9866522366522367`
- `brier`: `0.7103236359157805`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7071489860516631`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01277627918519016`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `6.0`
- `nll`: `3.9189818214619456`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_tile_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
