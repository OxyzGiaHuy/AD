# Run anomalydino_mvtec_zipper_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_zipper_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9932088695382223`
- `auroc`: `0.975577731092437`
- `brier`: `0.7312588002433209`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7527221685633161`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012722506366719474`
- `max_f1`: `0.9661016949152542`
- `model_storage_mb`: `6.0`
- `nll`: `2.621890737126367`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_zipper_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
