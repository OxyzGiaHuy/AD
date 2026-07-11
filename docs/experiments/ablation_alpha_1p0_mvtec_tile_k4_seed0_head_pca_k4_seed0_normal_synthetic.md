# Run ablation_alpha_1p0_mvtec_tile_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9731500775922749`
- `auroc`: `0.9242424242424242`
- `brier`: `0.19536234959091628`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07137773841874218`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002939685096598079`
- `max_f1`: `0.9101796407185628`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.578073583930681`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
