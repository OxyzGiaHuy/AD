# Run ablation_alpha_0p75_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9338857109002019`
- `auroc`: `0.8802473763118441`
- `brier`: `0.24080124635713834`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08691757361094166`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0034148963168263435`
- `max_f1`: `0.8620689655172413`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6751199634647473`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
