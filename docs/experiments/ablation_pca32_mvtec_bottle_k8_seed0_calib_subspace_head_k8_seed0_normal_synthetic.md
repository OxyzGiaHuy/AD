# Run ablation_pca32_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9891255070640803`
- `auroc`: `0.9714285714285714`
- `brier`: `0.06272710584724925`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09327721209770226`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023058460329670504`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.2241032821117364`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
