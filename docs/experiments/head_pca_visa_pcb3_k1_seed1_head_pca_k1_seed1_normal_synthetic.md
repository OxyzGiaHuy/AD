# Run head_pca_visa_pcb3_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k1_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7432146913855775`
- `auroc`: `0.7112871287128713`
- `brier`: `0.24738704974352904`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.005866176898206676`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0037808664309889523`
- `max_f1`: `0.703125`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6879198148348318`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
