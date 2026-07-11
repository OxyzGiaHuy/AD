# Run ablation_alpha_0p0_mvtec_transistor_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_transistor_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.7989086673278355`
- `auroc`: `0.8608333333333333`
- `brier`: `0.23817203054659428`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12405008047819133`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0034670275263488292`
- `max_f1`: `0.7674418604651163`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6694519895110358`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_transistor_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
