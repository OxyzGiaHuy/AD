# Run ablation_alpha_0p25_mvtec_carpet_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_carpet_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9958595012028923`
- `auroc`: `0.9867576243980738`
- `brier`: `0.20854291097764807`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3724943970003699`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002397423387210593`
- `max_f1`: `0.9723756906077348`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6099093793662219`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_carpet_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
