# Run head_pca_visa_macaroni1_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni1_k8_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8991914962717513`
- `auroc`: `0.8828`
- `brier`: `0.23232994524065553`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13306721568107605`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005782284801825881`
- `max_f1`: `0.8076923076923077`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6577338013308076`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni1_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
