# Run head_pca_visa_pcb2_k8_seed4_head_pca_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb2_k8_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7697695534730898`
- `auroc`: `0.7814`
- `brier`: `0.24378810273840462`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.012149016857147189`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.007509995820000768`
- `max_f1`: `0.7404255319148936`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.680716235206177`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb2_k8_seed4_head_pca_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
