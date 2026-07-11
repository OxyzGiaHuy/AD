# Run ablation_calib_upper_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9913690089145136`
- `auroc`: `0.981658692185008`
- `brier`: `0.16615789608118914`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.20175588896515173`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0027378874941976794`
- `max_f1`: `0.9681528662420382`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4621301205747706`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
