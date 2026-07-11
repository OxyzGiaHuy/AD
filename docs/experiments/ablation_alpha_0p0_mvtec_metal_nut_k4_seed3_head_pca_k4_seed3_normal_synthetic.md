# Run ablation_alpha_0p0_mvtec_metal_nut_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_metal_nut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9955776806902012`
- `auroc`: `0.9804496578690127`
- `brier`: `0.25352098956329405`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.43139935809633007`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003962762410873952`
- `max_f1`: `0.9625668449197861`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7001534706077074`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_metal_nut_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
