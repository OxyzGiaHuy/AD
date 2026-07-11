# Run ablation_alpha_1p0_mvtec_metal_nut_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9807757158269214`
- `auroc`: `0.9413489736070382`
- `brier`: `0.1432777475972859`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16497525806012353`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0024355115611916`
- `max_f1`: `0.9787234042553191`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4608569837416549`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
