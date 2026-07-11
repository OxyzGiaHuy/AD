# Run ablation_alpha_0p0_mvtec_leather_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_leather_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.27436342535987496`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5059794995092576`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025697939638649266`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.741183187092099`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_leather_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
