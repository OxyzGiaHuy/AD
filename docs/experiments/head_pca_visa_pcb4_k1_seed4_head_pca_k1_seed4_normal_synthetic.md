# Run head_pca_visa_pcb4_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k1_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.797610639254431`
- `auroc`: `0.8392079207920792`
- `brier`: `0.24435608067603154`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.004917928383718018`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0032023367337623045`
- `max_f1`: `0.8085106382978723`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6818559728832306`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
