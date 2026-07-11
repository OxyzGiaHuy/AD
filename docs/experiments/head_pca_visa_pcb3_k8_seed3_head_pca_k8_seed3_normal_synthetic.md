# Run head_pca_visa_pcb3_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k8_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7954113797481815`
- `auroc`: `0.7558415841584158`
- `brier`: `0.24515513302513703`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.00865490564066379`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0038833510112110062`
- `max_f1`: `0.6976744186046512`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6834520344560919`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
