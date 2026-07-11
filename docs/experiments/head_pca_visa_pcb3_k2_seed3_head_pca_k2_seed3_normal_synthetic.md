# Run head_pca_visa_pcb3_k2_seed3_head_pca_k2_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/head_pca_visa_pcb3_k2_seed3.yaml`
- Dataset: `visa`
- Model: `head_pca`

## Metrics

- `ap`: `0.7446474367183665`
- `auroc`: `0.6986138613861386`
- `brier`: `0.247282250778158`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0061289467918339`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.004388886480708027`
- `max_f1`: `0.6850393700787402`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6877101560884231`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/head_pca_visa_pcb3_k2_seed3_head_pca_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
