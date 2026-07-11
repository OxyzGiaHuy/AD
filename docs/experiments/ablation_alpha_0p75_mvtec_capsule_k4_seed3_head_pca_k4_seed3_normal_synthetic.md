# Run ablation_alpha_0p75_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9613179014665069`
- `auroc`: `0.8396489828480256`
- `brier`: `0.1600587834683125`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17939989765485126`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002869886416716106`
- `max_f1`: `0.9316239316239316`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5059303602180992`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
