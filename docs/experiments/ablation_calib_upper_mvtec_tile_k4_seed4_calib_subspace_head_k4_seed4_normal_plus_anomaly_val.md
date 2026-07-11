# Run ablation_calib_upper_mvtec_tile_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.992766417577466`
- `auroc`: `0.9844497607655502`
- `brier`: `0.06368777611809816`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.11609379311493775`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015464002317791684`
- `max_f1`: `0.9806451612903225`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.22237062386571574`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_tile_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
