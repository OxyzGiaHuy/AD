# Run ablation_alpha_0p75_mvtec_grid_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_grid_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9970026948248364`
- `auroc`: `0.9908103592314118`
- `brier`: `0.19173888949108053`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3351902633141248`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003026187276610961`
- `max_f1`: `0.9821428571428571`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5718412318826125`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_grid_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
