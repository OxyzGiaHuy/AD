# Run ablation_alpha_0p0_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9546808065217498`
- `auroc`: `0.9070464767616192`
- `brier`: `0.2387682395111158`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1450796870390574`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022024024029572804`
- `max_f1`: `0.8953488372093024`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6706634336236156`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_cable_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
