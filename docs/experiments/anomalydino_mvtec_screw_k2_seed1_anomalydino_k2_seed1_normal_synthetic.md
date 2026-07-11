# Run anomalydino_mvtec_screw_k2_seed1_anomalydino_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_screw_k2_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8907852254133448`
- `auroc`: `0.7669604427136708`
- `brier`: `0.25625`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25625`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008828422287479043`
- `max_f1`: `0.8698884758364313`
- `model_storage_mb`: `4.0107421875`
- `nll`: `4.720299446787697`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_screw_k2_seed1_anomalydino_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
