# Run ablation_alpha_0p75_mvtec_tile_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9669663370252545`
- `auroc`: `0.8986291486291487`
- `brier`: `0.20081667226241862`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.30673080071424824`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017137306336409007`
- `max_f1`: `0.9135802469135802`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5913387412001674`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
