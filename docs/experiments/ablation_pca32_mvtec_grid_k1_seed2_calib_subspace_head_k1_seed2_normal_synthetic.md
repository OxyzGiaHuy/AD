# Run ablation_pca32_mvtec_grid_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_grid_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9781887838106723`
- `auroc`: `0.9423558897243107`
- `brier`: `0.26923005703690506`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26923041313122487`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016027331017912962`
- `max_f1`: `0.9391304347826087`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `4.701871057775895`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_grid_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
