# Run head_pca_visa_pcb1_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k1_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8003294849680131`
- `auroc`: `0.8173`
- `brier`: `0.24672183514066076`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.032456925213336936`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026740448642522097`
- `max_f1`: `0.7884615384615384`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6865805592381952`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
