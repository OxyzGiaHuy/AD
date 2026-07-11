# Run ablation_calib_upper_mvtec_tile_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_tile_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9934277113304965`
- `auroc`: `0.9848484848484849`
- `brier`: `0.12814651668371888`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.17495773691649832`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021854958778947864`
- `max_f1`: `0.9620253164556962`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3541880819911051`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_tile_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
