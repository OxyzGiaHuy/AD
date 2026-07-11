# Run ablation_alpha_0p75_mvtec_capsule_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9002153810101342`
- `auroc`: `0.6234543278819306`
- `brier`: `0.16812871148915354`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1605470957178058`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019664125178347936`
- `max_f1`: `0.9045643153526971`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5236906207282446`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
