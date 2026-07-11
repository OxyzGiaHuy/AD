# Run ablation_alpha_0p75_mvtec_transistor_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_transistor_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8595714346164212`
- `auroc`: `0.8958333333333334`
- `brier`: `0.3083862901035148`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2766363680362702`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00208687461912632`
- `max_f1`: `0.8045977011494253`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8156137328573883`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_transistor_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
