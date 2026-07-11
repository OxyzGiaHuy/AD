# Run ablation_alpha_0p75_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_bottle_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9960460848281878`
- `auroc`: `0.9873015873015873`
- `brier`: `0.18292466000169758`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20775407696344764`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002165550029421427`
- `max_f1`: `0.9692307692307692`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5535376492533652`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
