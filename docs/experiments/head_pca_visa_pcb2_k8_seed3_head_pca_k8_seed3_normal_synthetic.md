# Run head_pca_visa_pcb2_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k8_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.773886291528736`
- `auroc`: `0.7855`
- `brier`: `0.24242943343114512`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.012050482630729668`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026872638054192067`
- `max_f1`: `0.74235807860262`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.677994527903544`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
