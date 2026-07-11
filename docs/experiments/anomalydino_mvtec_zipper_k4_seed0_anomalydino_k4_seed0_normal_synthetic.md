# Run anomalydino_mvtec_zipper_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_zipper_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9910989086272514`
- `auroc`: `0.9695378151260504`
- `brier`: `0.7694068068453116`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7719867490848761`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012706606938744223`
- `max_f1`: `0.959349593495935`
- `model_storage_mb`: `6.0`
- `nll`: `3.5718529498977833`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_zipper_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
