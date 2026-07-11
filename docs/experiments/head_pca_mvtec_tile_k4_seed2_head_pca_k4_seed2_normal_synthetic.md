# Run head_pca_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9890825784271374`
- `auroc`: `0.9736652236652237`
- `brier`: `0.25112209360708704`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3275397544742649`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015908614374124086`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6953409270136249`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_mvtec_tile_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
