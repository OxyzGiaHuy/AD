# Run ablation_alpha_1p0_mvtec_grid_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9907290856809723`
- `auroc`: `0.9724310776942355`
- `brier`: `0.19021263840880123`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24039976184184736`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0031164339146552943`
- `max_f1`: `0.9464285714285714`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5668173396346807`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
