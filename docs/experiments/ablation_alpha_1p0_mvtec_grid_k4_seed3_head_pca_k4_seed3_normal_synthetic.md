# Run ablation_alpha_1p0_mvtec_grid_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8970474615778145`
- `auroc`: `0.7577276524644946`
- `brier`: `0.19838305468872525`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06194574328569269`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017641737388494688`
- `max_f1`: `0.873015873015873`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5871686442539756`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
