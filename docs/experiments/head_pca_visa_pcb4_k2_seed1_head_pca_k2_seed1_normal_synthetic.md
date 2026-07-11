# Run head_pca_visa_pcb4_k2_seed1_head_pca_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb4_k2_seed1.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.8388144086191371`
- `auroc`: `0.8685148514851485`
- `brier`: `0.24162693903588042`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.01504995588639476`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008648630741297902`
- `max_f1`: `0.8275862068965517`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.676387502492387`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_visa_pcb4_k2_seed1_head_pca_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
