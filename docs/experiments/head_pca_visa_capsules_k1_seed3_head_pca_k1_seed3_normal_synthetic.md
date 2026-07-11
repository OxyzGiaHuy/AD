# Run head_pca_visa_capsules_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_capsules_k1_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.9380483705725965`
- `auroc`: `0.8885`
- `brier`: `0.23908410126814078`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11540253721177574`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0061358045437373224`
- `max_f1`: `0.863849765258216`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6712937702988404`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_capsules_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
