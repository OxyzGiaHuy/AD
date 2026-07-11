# Run head_pca_mvtec_metal_nut_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_metal_nut_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9944208933801431`
- `auroc`: `0.9760508308895406`
- `brier`: `0.2496487874178837`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.33361307019772735`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001615789386889209`
- `max_f1`: `0.9578947368421052`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6924380188664848`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_mvtec_metal_nut_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
