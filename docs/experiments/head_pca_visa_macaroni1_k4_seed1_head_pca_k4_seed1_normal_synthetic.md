# Run head_pca_visa_macaroni1_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni1_k4_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8913002942662512`
- `auroc`: `0.8744`
- `brier`: `0.23851538589272245`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06969276413321492`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01479301775805652`
- `max_f1`: `0.8058252427184466`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6701552966451946`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni1_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
