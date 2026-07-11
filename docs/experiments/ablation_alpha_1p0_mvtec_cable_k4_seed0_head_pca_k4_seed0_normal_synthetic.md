# Run ablation_alpha_1p0_mvtec_cable_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_cable_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9358237991840531`
- `auroc`: `0.893928035982009`
- `brier`: `0.25202455909786303`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1311585692564646`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018674661840001742`
- `max_f1`: `0.8651685393258427`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7025248224068508`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_cable_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
