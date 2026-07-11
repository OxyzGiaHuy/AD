# Run head_pca_visa_pcb1_k2_seed3_head_pca_k2_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k2_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7274635873303026`
- `auroc`: `0.7232`
- `brier`: `0.24597527913762585`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.02632233843207362`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0036723018158227204`
- `max_f1`: `0.7188940092165899`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6850911125628975`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k2_seed3_head_pca_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
