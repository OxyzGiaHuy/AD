# Run ablation_calib_upper_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9920185712778306`
- `auroc`: `0.9814814814814815`
- `brier`: `0.07478109793447625`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.08442824157193685`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0032929877917736005`
- `max_f1`: `0.9629629629629629`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.27398741733716125`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
