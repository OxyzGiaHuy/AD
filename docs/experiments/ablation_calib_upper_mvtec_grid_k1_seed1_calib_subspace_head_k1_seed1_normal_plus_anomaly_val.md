# Run ablation_calib_upper_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_grid_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9267278263951552`
- `auroc`: `0.8772893772893773`
- `brier`: `0.2036327362226967`
- `calibration_anomaly_val_count`: `5`
- `ece`: `0.22473979047308232`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027022696266027347`
- `max_f1`: `0.9454545454545454`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7482207772388474`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_grid_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
