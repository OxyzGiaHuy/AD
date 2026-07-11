# Run head_pca_visa_pcb2_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k4_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7478914348070146`
- `auroc`: `0.762`
- `brier`: `0.24385225683317743`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.04521383643150325`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0095671393442899`
- `max_f1`: `0.736`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6808398287204663`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
