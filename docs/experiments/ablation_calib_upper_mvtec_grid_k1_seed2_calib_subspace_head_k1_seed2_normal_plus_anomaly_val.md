# Run ablation_calib_upper_mvtec_grid_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_grid_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9545011257935122`
- `auroc`: `0.902014652014652`
- `brier`: `0.1926024808875457`
- `calibration_anomaly_val_count`: `5`
- `ece`: `0.2162380396095041`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0033189491560197855`
- `max_f1`: `0.912621359223301`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6892906695105704`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_grid_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
