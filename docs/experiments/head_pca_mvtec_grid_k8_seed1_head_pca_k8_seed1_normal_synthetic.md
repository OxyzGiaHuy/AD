# Run head_pca_mvtec_grid_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_grid_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.26539756924590896`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.37459616019175607`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016305534503398798`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7236956212805052`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_grid_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
