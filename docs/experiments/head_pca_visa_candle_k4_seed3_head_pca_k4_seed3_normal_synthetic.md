# Run head_pca_visa_candle_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k4_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8652211117427917`
- `auroc`: `0.8907`
- `brier`: `0.2317434559338519`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15119321972131727`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.005180006567388773`
- `max_f1`: `0.847926267281106`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.656561570288519`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
