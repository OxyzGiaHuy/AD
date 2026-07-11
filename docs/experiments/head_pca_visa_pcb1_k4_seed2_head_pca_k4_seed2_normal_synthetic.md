# Run head_pca_visa_pcb1_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k4_seed2.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8845047382280334`
- `auroc`: `0.8964`
- `brier`: `0.24350920239078505`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09144931614398955`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003259717971086502`
- `max_f1`: `0.8272727272727273`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6801445174733645`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
