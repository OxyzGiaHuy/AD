# Run ablation_alpha_0p75_mvtec_capsule_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9718168495773666`
- `auroc`: `0.8787395293179099`
- `brier`: `0.1589201921420377`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22094467688690536`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.004170066648812005`
- `max_f1`: `0.9304347826086956`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5030230142268826`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
