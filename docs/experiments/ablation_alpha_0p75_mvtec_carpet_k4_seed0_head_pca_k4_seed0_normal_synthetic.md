# Run ablation_alpha_0p75_mvtec_carpet_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9984966749698292`
- `auroc`: `0.9951845906902087`
- `brier`: `0.16344587523346898`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27403329376481533`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002794332929656037`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5103685751111066`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
