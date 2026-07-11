# Run head_pca_visa_pcb4_k2_seed4_head_pca_k2_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k2_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8935273123988958`
- `auroc`: `0.9206930693069307`
- `brier`: `0.2400426380072601`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.009004694015825553`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.005349357969206364`
- `max_f1`: `0.8868778280542986`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6732186749178906`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k2_seed4_head_pca_k2_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
