# Run ablation_calib_upper_mvtec_tile_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9945900508640942`
- `auroc`: `0.988835725677831`
- `brier`: `0.06063553221309078`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.12265851738256056`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0037999204744439607`
- `max_f1`: `0.9806451612903225`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.21240320882997815`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_tile_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
