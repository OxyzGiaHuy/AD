# Run ablation_alpha_0p0_mvtec_carpet_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_carpet_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9974658285988621`
- `auroc`: `0.9919743178170144`
- `brier`: `0.23558487819682689`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.45069632672855997`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022340253409412173`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6640880164059488`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_carpet_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
