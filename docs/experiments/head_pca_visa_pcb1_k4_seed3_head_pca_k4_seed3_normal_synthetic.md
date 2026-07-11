# Run head_pca_visa_pcb1_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb1_k4_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7439975209804952`
- `auroc`: `0.7575`
- `brier`: `0.24463151888809084`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.048943762630224236`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003781163226813078`
- `max_f1`: `0.7466666666666667`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6824010982449726`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/head_pca_visa_pcb1_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
