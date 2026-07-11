# Run head_pca_visa_candle_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k1_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8746234668740668`
- `auroc`: `0.8838`
- `brier`: `0.2405451561239427`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.017977906912565164`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002787883309647441`
- `max_f1`: `0.8140703517587939`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6742234545506587`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
