# Run head_pca_visa_macaroni1_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni1_k4_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.883983053978308`
- `auroc`: `0.8696`
- `brier`: `0.2386420196872694`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0346374633908272`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0037421004846692084`
- `max_f1`: `0.8141592920353983`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6704104829229862`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni1_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
