# Run ablation_alpha_0p75_mvtec_metal_nut_k4_seed2_head_pca_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9924911068038921`
- `auroc`: `0.9657869012707723`
- `brier`: `0.16431917399569912`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14834524082100903`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0033390156924724577`
- `max_f1`: `0.9621621621621622`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5140220796617636`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k4_seed2_head_pca_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
