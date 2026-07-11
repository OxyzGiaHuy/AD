# Run ablation_pca128_mvtec_bottle_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_bottle_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9837648235782288`
- `auroc`: `0.9595238095238096`
- `brier`: `0.18601187946270112`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2016192713685065`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015759312783379152`
- `max_f1`: `0.96875`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.0281143698910498`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_bottle_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
