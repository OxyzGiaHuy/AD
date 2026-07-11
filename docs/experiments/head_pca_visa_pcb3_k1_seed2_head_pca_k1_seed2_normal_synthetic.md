# Run head_pca_visa_pcb3_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k1_seed2.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.6895766366622802`
- `auroc`: `0.6680198019801981`
- `brier`: `0.24788953016414142`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.008499192212944595`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.016148696630377674`
- `max_f1`: `0.6798418972332015`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.688924209942076`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
