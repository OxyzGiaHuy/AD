# Run ablation_alpha_1p0_mvtec_metal_nut_k4_seed4_head_pca_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9868463077472537`
- `auroc`: `0.9467253176930597`
- `brier`: `0.1531649900914385`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12045098024865859`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026993236464002857`
- `max_f1`: `0.9513513513513514`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4850322794494484`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k4_seed4_head_pca_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
