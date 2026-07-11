# Run ablation_alpha_1p0_mvtec_toothbrush_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_toothbrush_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9504109282740362`
- `auroc`: `0.8611111111111112`
- `brier`: `0.20398746314418226`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.00895177608444575`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005840980359131382`
- `max_f1`: `0.8813559322033898`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5980338893134317`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_toothbrush_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
