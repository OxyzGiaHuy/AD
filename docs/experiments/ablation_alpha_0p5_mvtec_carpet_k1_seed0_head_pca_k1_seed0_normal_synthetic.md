# Run ablation_alpha_0p5_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_carpet_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9893309162216688`
- `auroc`: `0.9646869983948636`
- `brier`: `0.18908090802693225`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3516924062855223`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022225707737553832`
- `max_f1`: `0.9613259668508287`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5685472527343429`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_carpet_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
