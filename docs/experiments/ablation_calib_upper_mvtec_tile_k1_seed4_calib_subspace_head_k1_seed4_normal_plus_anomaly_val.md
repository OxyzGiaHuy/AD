# Run ablation_calib_upper_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_tile_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9962246347739928`
- `auroc`: `0.9916267942583732`
- `brier`: `0.1446280840454382`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.1908670830617257`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002229865657490328`
- `max_f1`: `0.9803921568627451`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.39458751961246913`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_tile_k1_seed4_calib_subspace_head_k1_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
