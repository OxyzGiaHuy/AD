# Run ablation_alpha_0p75_mvtec_transistor_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_transistor_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8249657018263331`
- `auroc`: `0.86375`
- `brier`: `0.2995135594738436`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2721041589975357`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003160221502184868`
- `max_f1`: `0.75`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7962540047846716`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_transistor_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
