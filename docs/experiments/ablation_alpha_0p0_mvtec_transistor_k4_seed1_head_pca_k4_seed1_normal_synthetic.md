# Run ablation_alpha_0p0_mvtec_transistor_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_transistor_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7625609398358252`
- `auroc`: `0.7975`
- `brier`: `0.2421777262087776`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08947197914123534`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0053831697255373005`
- `max_f1`: `0.6851851851851852`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6774930021747412`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_transistor_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
