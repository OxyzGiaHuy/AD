# Run ablation_alpha_0p75_mvtec_screw_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_screw_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8902743547414004`
- `auroc`: `0.7729042836646853`
- `brier`: `0.18831077990225525`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1553793236613274`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0028796386322937906`
- `max_f1`: `0.8803088803088803`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5646269749326409`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_screw_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
