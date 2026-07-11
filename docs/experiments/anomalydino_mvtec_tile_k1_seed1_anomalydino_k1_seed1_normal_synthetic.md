# Run anomalydino_mvtec_tile_k1_seed1_anomalydino_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_tile_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9955468203656755`
- `auroc`: `0.9888167388167388`
- `brier`: `0.28205128205128205`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28205128205128205`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004933817678282403`
- `max_f1`: `0.9764705882352941`
- `model_storage_mb`: `2.00537109375`
- `nll`: `5.195576625851375`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_tile_k1_seed1_anomalydino_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
