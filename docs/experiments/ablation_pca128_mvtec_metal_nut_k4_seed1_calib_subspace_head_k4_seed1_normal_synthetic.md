# Run ablation_pca128_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9972060141425317`
- `auroc`: `0.987781036168133`
- `brier`: `0.12920928286820563`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14854603280191828`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014826177254967069`
- `max_f1`: `0.972972972972973`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.5857721625300095`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
