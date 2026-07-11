# Run head_pca_mvtec_toothbrush_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/head_pca_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9902702275906299`
- `auroc`: `0.975`
- `brier`: `0.23862591641344671`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.395903576697622`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016275328096179735`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6703641988744515`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_mvtec_toothbrush_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
