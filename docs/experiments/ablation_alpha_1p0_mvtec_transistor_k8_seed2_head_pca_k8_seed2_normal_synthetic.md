# Run ablation_alpha_1p0_mvtec_transistor_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.867676936600723`
- `auroc`: `0.8954166666666666`
- `brier`: `0.3256506787822228`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32093858122825625`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002484647575765848`
- `max_f1`: `0.8048780487804879`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8566691807481461`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
