# Run head_pca_visa_pcb1_k2_seed4_head_pca_k2_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k2_seed4.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7226205466004931`
- `auroc`: `0.7528`
- `brier`: `0.24605961388327047`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.007788701653480556`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.007328561311587691`
- `max_f1`: `0.7551867219917012`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6852618826593075`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k2_seed4_head_pca_k2_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
