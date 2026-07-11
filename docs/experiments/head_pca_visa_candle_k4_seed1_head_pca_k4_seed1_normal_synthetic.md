# Run head_pca_visa_candle_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k4_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8724919006889439`
- `auroc`: `0.9035`
- `brier`: `0.23430886900281336`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13800599217414858`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025700391829013825`
- `max_f1`: `0.8625592417061612`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6617168173780386`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
