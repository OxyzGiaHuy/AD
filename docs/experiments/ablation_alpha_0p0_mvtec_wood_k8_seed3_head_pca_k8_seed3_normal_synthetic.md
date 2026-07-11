# Run ablation_alpha_0p0_mvtec_wood_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_wood_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9842801569004818`
- `auroc`: `0.9587719298245614`
- `brier`: `0.2631520161127949`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.30407771505886994`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0019118733751245691`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7193641244064751`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_wood_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
