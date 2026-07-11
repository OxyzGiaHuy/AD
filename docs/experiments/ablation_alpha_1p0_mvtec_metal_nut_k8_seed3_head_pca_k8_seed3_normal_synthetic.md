# Run ablation_alpha_1p0_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9988329643313155`
- `auroc`: `0.9951124144672532`
- `brier`: `0.14334457287494956`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19827689917191216`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002613039897835773`
- `max_f1`: `0.9893617021276596`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.46085130022355`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
