# Run ablation_alpha_0p75_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9990604881882976`
- `auroc`: `0.9960899315738025`
- `brier`: `0.15502774709400377`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2513310758963876`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002601516700309256`
- `max_f1`: `0.9893617021276596`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.49319092555539484`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
