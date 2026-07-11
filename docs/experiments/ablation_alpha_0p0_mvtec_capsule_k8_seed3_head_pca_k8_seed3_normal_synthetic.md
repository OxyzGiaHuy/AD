# Run ablation_alpha_0p0_mvtec_capsule_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9435474181617609`
- `auroc`: `0.7989629038691664`
- `brier`: `0.24500827628637625`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3390754587722547`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00287979839821205`
- `max_f1`: `0.933920704845815`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6831491404978547`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_capsule_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
