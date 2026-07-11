# Run ablation_calib_upper_mvtec_grid_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_grid_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9541506552221063`
- `auroc`: `0.9047619047619048`
- `brier`: `0.1758816890179225`
- `calibration_anomaly_val_count`: `5`
- `ece`: `0.19717441642121092`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003556541460630012`
- `max_f1`: `0.9454545454545454`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.563465390808512`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_grid_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
