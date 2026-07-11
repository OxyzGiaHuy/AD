# Run head_pca_visa_candle_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k8_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8521831860345257`
- `auroc`: `0.8818`
- `brier`: `0.2308992463388661`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1643479444086552`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.004268945241346955`
- `max_f1`: `0.8272727272727273`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6548523407535733`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
