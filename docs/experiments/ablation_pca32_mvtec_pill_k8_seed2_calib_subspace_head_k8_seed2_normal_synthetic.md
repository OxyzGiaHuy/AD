# Run ablation_pca32_mvtec_pill_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.987840008152878`
- `auroc`: `0.9410801963993454`
- `brier`: `0.07399959295276375`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07874208184106907`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001442013698780608`
- `max_f1`: `0.9550173010380623`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.30445845060387033`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
