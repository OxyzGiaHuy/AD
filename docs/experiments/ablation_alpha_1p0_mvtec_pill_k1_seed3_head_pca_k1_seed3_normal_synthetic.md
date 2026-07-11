# Run ablation_alpha_1p0_mvtec_pill_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9506402724486335`
- `auroc`: `0.7853246044735407`
- `brier`: `0.1457526739931898`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12058064751996256`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017596052479958105`
- `max_f1`: `0.9185667752442996`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.47267975586772204`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
