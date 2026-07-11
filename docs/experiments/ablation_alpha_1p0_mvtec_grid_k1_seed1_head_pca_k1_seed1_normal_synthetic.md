# Run ablation_alpha_1p0_mvtec_grid_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_grid_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7776251677698678`
- `auroc`: `0.5572263993316625`
- `brier`: `0.19763555095364183`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.013210365405449552`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0050429249277863745`
- `max_f1`: `0.8444444444444444`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5845857123882466`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_grid_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
