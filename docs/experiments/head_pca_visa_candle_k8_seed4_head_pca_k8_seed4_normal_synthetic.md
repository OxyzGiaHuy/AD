# Run head_pca_visa_candle_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k8_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8533457616519813`
- `auroc`: `0.8756`
- `brier`: `0.2332582422140363`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1839482009410858`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002982758283615112`
- `max_f1`: `0.8186046511627907`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6595837006351019`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
