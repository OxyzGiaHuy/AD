# Run ablation_alpha_0p0_mvtec_screw_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_screw_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.902643388949189`
- `auroc`: `0.8026234884197582`
- `brier`: `0.25321287763281614`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2935125587508082`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002204567764420062`
- `max_f1`: `0.896`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6995676899577916`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_screw_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
