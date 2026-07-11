# Run ablation_alpha_0p25_mvtec_bottle_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_bottle_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9854167691841963`
- `auroc`: `0.9619047619047619`
- `brier`: `0.21445344728421104`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3979276978825949`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0034102855182914847`
- `max_f1`: `0.96875`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.62169575730256`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_bottle_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
