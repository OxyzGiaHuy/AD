# Run head_pca_visa_pcb1_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k8_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7851304552849157`
- `auroc`: `0.7895`
- `brier`: `0.24349589188514642`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.004296427965164176`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.005500575248152018`
- `max_f1`: `0.7636363636363637`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.680131070389351`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
