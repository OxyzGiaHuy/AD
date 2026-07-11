# Run head_pca_visa_capsules_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_capsules_k4_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9661961180541649`
- `auroc`: `0.9411666666666667`
- `brier`: `0.2268538199575123`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3046338457614184`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0068751745275221765`
- `max_f1`: `0.9134615384615384`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6467198504949222`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_capsules_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
