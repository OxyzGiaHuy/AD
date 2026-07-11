# Run head_pca_visa_pcb4_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k8_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8937898899979385`
- `auroc`: `0.9115841584158416`
- `brier`: `0.24019087707854672`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.00118811569403654`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0043840637495416905`
- `max_f1`: `0.875`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6735178361879149`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
