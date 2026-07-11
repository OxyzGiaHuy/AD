# Run ablation_alpha_1p0_mvtec_leather_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_leather_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9848567867901821`
- `auroc`: `0.953125`
- `brier`: `0.1741184527236621`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.0749711178002818`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003806912745799749`
- `max_f1`: `0.93048128342246`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5280075071713748`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_leather_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
