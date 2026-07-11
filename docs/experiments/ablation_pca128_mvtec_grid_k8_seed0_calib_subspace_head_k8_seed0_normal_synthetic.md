# Run ablation_pca128_mvtec_grid_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_grid_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.999697519661222`
- `auroc`: `0.9991645781119465`
- `brier`: `0.20400436928727012`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22072924740421465`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002117253648929107`
- `max_f1`: `0.991304347826087`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.0145695145612796`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_grid_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
