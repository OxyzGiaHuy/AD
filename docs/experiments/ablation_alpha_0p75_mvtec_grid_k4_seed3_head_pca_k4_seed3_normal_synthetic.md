# Run ablation_alpha_0p75_mvtec_grid_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_grid_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9931938341171168`
- `auroc`: `0.9799498746867168`
- `brier`: `0.1927635728557486`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.06608091180141154`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028704630258755805`
- `max_f1`: `0.9557522123893806`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5732521540074896`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_grid_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
