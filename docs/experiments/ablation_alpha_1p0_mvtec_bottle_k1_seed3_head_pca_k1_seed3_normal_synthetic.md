# Run ablation_alpha_1p0_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_bottle_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9777562249156339`
- `auroc`: `0.9297619047619048`
- `brier`: `0.17813606965918552`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08251223219446391`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018047220466366734`
- `max_f1`: `0.9264705882352942`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5412665954090511`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_bottle_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
