# Run head_pca_visa_pcb4_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k1_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8595073115381973`
- `auroc`: `0.888019801980198`
- `brier`: `0.24391651177311124`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.040809389815401644`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0041388174268736765`
- `max_f1`: `0.8533333333333334`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6809645012749018`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
