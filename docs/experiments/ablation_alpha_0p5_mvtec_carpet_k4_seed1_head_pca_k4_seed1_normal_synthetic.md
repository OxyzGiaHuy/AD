# Run ablation_alpha_0p5_mvtec_carpet_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_carpet_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9961587076397451`
- `auroc`: `0.9879614767255217`
- `brier`: `0.163785521981469`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3307746231046498`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0029769378563023023`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5153571621844235`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_carpet_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
