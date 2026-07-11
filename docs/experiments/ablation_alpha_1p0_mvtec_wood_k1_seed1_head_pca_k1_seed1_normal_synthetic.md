# Run ablation_alpha_1p0_mvtec_wood_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9589933430898896`
- `auroc`: `0.9394736842105263`
- `brier`: `0.17851247356060193`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08676666700387305`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0042304950471543055`
- `max_f1`: `0.9586776859504132`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5420835065796253`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
