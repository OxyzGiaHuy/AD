# Run ablation_alpha_0p75_mvtec_capsule_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9837454766475187`
- `auroc`: `0.9210211408057439`
- `brier`: `0.15797211821939952`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2266204451972788`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003067916484944748`
- `max_f1`: `0.9304347826086956`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.500981907243845`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
