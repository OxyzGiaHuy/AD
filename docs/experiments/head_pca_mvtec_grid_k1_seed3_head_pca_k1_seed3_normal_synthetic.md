# Run head_pca_mvtec_grid_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_grid_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9601180321331445`
- `auroc`: `0.908939014202172`
- `brier`: `0.2520152109029652`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2691311671947822`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001649205381862628`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6971703010575102`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_mvtec_grid_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
