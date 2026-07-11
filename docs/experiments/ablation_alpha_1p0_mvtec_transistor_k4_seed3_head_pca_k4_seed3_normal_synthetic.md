# Run ablation_alpha_1p0_mvtec_transistor_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_transistor_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8574233422565136`
- `auroc`: `0.8879166666666667`
- `brier`: `0.34027571858981304`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3273640984296798`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002746143825352192`
- `max_f1`: `0.7764705882352941`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.8909758758880625`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_transistor_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
