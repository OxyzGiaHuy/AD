# Run ablation_alpha_0p25_mvtec_metal_nut_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_metal_nut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9864375573840306`
- `auroc`: `0.9491691104594331`
- `brier`: `0.20912631125730144`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31323470395544306`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0022930861977131472`
- `max_f1`: `0.9633507853403142`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6108761932055295`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_metal_nut_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
