# Run head_pca_visa_pcb1_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k4_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7298968348080206`
- `auroc`: `0.7246`
- `brier`: `0.24510504791716184`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.015922519266605414`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.009861975116655231`
- `max_f1`: `0.7196969696969697`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6833507648500301`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
