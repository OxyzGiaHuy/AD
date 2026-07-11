# Run ablation_pca32_mvtec_leather_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_leather_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.20627369853554492`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19188427204085937`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019650557378847753`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6542094868742931`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_leather_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
