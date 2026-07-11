# Run ablation_pca128_mvtec_carpet_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9950028856778802`
- `auroc`: `0.9847512038523274`
- `brier`: `0.1965737067588692`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21541532186361467`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002558270867309`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.9490419739210075`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
