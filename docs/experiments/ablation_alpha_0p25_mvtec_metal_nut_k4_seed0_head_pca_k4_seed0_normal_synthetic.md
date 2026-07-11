# Run ablation_alpha_0p25_mvtec_metal_nut_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_metal_nut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.993711895448754`
- `auroc`: `0.9740957966764419`
- `brier`: `0.20876834023099394`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32239498444225473`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002790119434180467`
- `max_f1`: `0.9680851063829787`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6101854085442371`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_metal_nut_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
