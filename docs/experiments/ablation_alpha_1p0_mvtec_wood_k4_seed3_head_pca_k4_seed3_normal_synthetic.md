# Run ablation_alpha_1p0_mvtec_wood_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9980663315702074`
- `auroc`: `0.993859649122807`
- `brier`: `0.17279819535904078`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10644178752657726`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003152570793334442`
- `max_f1`: `0.9833333333333333`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5269308205790169`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
