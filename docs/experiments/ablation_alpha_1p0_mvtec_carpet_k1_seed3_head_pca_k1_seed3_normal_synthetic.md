# Run ablation_alpha_1p0_mvtec_carpet_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_carpet_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9756637339700579`
- `auroc`: `0.9093097913322632`
- `brier`: `0.17708591672967436`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07282222743727203`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022155982243199633`
- `max_f1`: `0.9101796407185628`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5387158551308007`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_carpet_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
