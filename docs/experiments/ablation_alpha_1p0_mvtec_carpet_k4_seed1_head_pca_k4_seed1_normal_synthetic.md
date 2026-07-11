# Run ablation_alpha_1p0_mvtec_carpet_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_carpet_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9905651628278175`
- `auroc`: `0.971107544141252`
- `brier`: `0.14694844738877602`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27675440703701776`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001978109280268351`
- `max_f1`: `0.967032967032967`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.46992224538208527`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_carpet_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
