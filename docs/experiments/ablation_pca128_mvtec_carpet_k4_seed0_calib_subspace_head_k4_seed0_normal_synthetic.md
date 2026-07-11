# Run ablation_pca128_mvtec_carpet_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9976215809700564`
- `auroc`: `0.9923756019261637`
- `brier`: `0.10792494974165956`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13703474892765033`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023073774690811452`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.5910223125843512`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
