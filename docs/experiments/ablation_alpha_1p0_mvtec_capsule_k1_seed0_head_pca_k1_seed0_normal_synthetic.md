# Run ablation_alpha_1p0_mvtec_capsule_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9356737026835749`
- `auroc`: `0.7606701236537694`
- `brier`: `0.15470002871081534`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11419494585557421`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018042457205328074`
- `max_f1`: `0.9170305676855895`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.49230590581990247`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
