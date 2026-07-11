# Run ablation_alpha_0p0_mvtec_transistor_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_transistor_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.889883983882882`
- `auroc`: `0.9116666666666666`
- `brier`: `0.23908623049343286`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0996713161468506`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0036498480476439`
- `max_f1`: `0.8048780487804879`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6713046827670237`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_transistor_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
