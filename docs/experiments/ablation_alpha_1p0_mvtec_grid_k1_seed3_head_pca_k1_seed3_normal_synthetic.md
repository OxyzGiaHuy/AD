# Run ablation_alpha_1p0_mvtec_grid_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8527846589335923`
- `auroc`: `0.5931495405179615`
- `brier`: `0.19956080033118292`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04736516567376944`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002995792203224622`
- `max_f1`: `0.8444444444444444`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5891304008042487`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
