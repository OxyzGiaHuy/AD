# Run ablation_alpha_0p25_mvtec_carpet_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_carpet_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9928981555629263`
- `auroc`: `0.9747191011235955`
- `brier`: `0.2033584939255554`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3736789567857726`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002714637842061173`
- `max_f1`: `0.96045197740113`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5992084151925896`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_carpet_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
