# Run head_pca_mvtec_grid_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9846803503966466`
- `auroc`: `0.9598997493734336`
- `brier`: `0.25390338221454234`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2842455980105278`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018015224964190752`
- `max_f1`: `0.9421487603305785`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7009453433680025`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_mvtec_grid_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
