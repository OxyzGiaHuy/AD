# Run head_pca_visa_candle_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k1_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8781888041101866`
- `auroc`: `0.8876`
- `brier`: `0.24048858286853167`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.007503828704357131`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.008373966924846172`
- `max_f1`: `0.8363636363636363`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6741117560052754`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
