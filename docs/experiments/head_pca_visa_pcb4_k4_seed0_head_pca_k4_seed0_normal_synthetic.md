# Run head_pca_visa_pcb4_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k4_seed0.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.848213548380587`
- `auroc`: `0.8312871287128712`
- `brier`: `0.24379003754490133`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0010208333309610351`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0082785910393913`
- `max_f1`: `0.7677725118483413`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6807218174576395`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
