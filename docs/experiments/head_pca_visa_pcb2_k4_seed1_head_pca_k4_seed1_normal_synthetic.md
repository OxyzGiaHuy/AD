# Run head_pca_visa_pcb2_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k4_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7217484401503371`
- `auroc`: `0.7216`
- `brier`: `0.24517712437396427`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.004400232583284428`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.007674601199105382`
- `max_f1`: `0.7340823970037453`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6834945624573661`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
