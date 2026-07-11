# Run head_pca_visa_macaroni2_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_macaroni2_k4_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7984649187108233`
- `auroc`: `0.7964`
- `brier`: `0.2412824806228604`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04568545907735827`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.005093753458932042`
- `max_f1`: `0.7596153846153846`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6756968510642654`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_macaroni2_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
