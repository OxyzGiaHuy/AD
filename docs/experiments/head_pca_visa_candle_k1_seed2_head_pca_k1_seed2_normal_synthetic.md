# Run head_pca_visa_candle_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k1_seed2.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8608481396634263`
- `auroc`: `0.8763`
- `brier`: `0.2406409736728213`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.007963900417089418`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004644982162863016`
- `max_f1`: `0.8262910798122066`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6744190271522962`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
