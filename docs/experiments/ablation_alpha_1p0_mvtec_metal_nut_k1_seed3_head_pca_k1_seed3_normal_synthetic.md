# Run ablation_alpha_1p0_mvtec_metal_nut_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9484728731981066`
- `auroc`: `0.7978983382209188`
- `brier`: `0.16224229383132`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09066158947737324`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019862533587476482`
- `max_f1`: `0.9064039408866995`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5083922909304274`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
