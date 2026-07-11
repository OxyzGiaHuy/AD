# Run ablation_alpha_1p0_mvtec_metal_nut_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9676901606548974`
- `auroc`: `0.8905180840664711`
- `brier`: `0.154286312466652`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08914765015892354`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0027195916389641554`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4882445300813293`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
