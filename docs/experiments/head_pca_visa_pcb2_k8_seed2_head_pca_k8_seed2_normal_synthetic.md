# Run head_pca_visa_pcb2_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k8_seed2.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7634466194427092`
- `auroc`: `0.7895`
- `brier`: `0.24336438064132082`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.029861891567707063`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003507630042731762`
- `max_f1`: `0.7574468085106383`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6798668527860496`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
