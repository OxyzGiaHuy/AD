# Run head_pca_visa_candle_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_candle_k4_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.84886049567264`
- `auroc`: `0.8584`
- `brier`: `0.23442314003515413`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14471259102225303`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0029577276483178138`
- `max_f1`: `0.7980295566502463`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6619327370840673`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_candle_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
