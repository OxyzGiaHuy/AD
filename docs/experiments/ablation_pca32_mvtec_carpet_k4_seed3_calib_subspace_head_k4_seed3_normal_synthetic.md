# Run ablation_pca32_mvtec_carpet_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9972119277113654`
- `auroc`: `0.9911717495987159`
- `brier`: `0.41075608073983977`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4468136841299919`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00217419555490343`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.3520022885502163`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
