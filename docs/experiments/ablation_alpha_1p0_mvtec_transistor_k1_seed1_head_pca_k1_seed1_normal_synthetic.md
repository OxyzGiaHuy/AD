# Run ablation_alpha_1p0_mvtec_transistor_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.6148857493392247`
- `auroc`: `0.64875`
- `brier`: `0.3448271507085366`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3238395810127258`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0026382534950971604`
- `max_f1`: `0.6141732283464567`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.9012261024719201`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
