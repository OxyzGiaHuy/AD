# Run head_pca_mvtec_grid_k2_seed3_head_pca_k2_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_grid_k2_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9946360359612121`
- `auroc`: `0.985797827903091`
- `brier`: `0.278071143537634`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.41685824440075797`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0016611149677863489`
- `max_f1`: `0.9734513274336283`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7493580060370462`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_mvtec_grid_k2_seed3_head_pca_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
