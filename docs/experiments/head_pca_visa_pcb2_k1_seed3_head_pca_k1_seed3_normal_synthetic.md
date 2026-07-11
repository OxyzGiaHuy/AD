# Run head_pca_visa_pcb2_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k1_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.6296079306617727`
- `auroc`: `0.6393`
- `brier`: `0.24748730180824294`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.007980610430240613`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.007715581217780709`
- `max_f1`: `0.7025089605734767`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6881194813682514`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
