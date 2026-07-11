# Run ablation_alpha_0p75_mvtec_capsule_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9774888089778835`
- `auroc`: `0.9038691663342641`
- `brier`: `0.15056204093657172`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1626531982963735`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001749712959722136`
- `max_f1`: `0.9302325581395349`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4834999627732433`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
