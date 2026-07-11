# Run ablation_alpha_0p5_mvtec_bottle_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_bottle_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9860756418854502`
- `auroc`: `0.9642857142857143`
- `brier`: `0.1873375196574849`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18515642579779576`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003941329936665225`
- `max_f1`: `0.9612403100775194`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5646703281760374`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_bottle_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
