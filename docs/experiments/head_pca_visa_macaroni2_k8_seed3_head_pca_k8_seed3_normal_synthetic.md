# Run head_pca_visa_macaroni2_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni2_k8_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8529641200775699`
- `auroc`: `0.8123`
- `brier`: `0.2412684853983453`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09452231466770171`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.006386248003691435`
- `max_f1`: `0.746268656716418`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6756566020120794`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni2_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
