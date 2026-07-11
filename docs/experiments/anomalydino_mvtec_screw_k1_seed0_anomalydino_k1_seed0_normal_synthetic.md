# Run anomalydino_mvtec_screw_k1_seed0_anomalydino_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8391223828577997`
- `auroc`: `0.6753433080549293`
- `brier`: `0.25625`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25625`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005236814497038722`
- `max_f1`: `0.8778625954198473`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.720299446787697`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_screw_k1_seed0_anomalydino_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
