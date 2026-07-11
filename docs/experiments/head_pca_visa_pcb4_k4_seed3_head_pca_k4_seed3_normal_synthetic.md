# Run head_pca_visa_pcb4_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k4_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9070449184424205`
- `auroc`: `0.9099009900990099`
- `brier`: `0.24103564827512067`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.014698338745838311`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00389324831984826`
- `max_f1`: `0.8544600938967136`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6752062668654009`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
