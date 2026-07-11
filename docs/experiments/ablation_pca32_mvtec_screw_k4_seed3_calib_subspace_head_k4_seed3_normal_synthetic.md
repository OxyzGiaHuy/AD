# Run ablation_pca32_mvtec_screw_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8518285414880921`
- `auroc`: `0.6780077884812462`
- `brier`: `0.3345632770365186`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3488495269837358`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019235624233260751`
- `max_f1`: `0.8613138686131386`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.3124833007358083`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
