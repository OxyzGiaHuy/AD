# Run ablation_alpha_0p5_mvtec_cable_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_cable_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9441210343119405`
- `auroc`: `0.8924287856071964`
- `brier`: `0.226133540980107`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0949366199970246`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002151636704802513`
- `max_f1`: `0.8654970760233918`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6438801038882059`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_cable_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
