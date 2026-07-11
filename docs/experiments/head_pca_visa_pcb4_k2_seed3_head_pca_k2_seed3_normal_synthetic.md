# Run head_pca_visa_pcb4_k2_seed3_head_pca_k2_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k2_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8527787411696336`
- `auroc`: `0.8757425742574257`
- `brier`: `0.24066098247304502`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.051325534854955376`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.021970751987241986`
- `max_f1`: `0.8355555555555556`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6744459664351259`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k2_seed3_head_pca_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
