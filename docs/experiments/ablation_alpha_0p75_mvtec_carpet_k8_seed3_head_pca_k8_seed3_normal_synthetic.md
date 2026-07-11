# Run ablation_alpha_0p75_mvtec_carpet_k8_seed3_head_pca_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_carpet_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9918373760705634`
- `auroc`: `0.9731139646869984`
- `brier`: `0.16236596435051226`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29458574122852754`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017533863329479836`
- `max_f1`: `0.9608938547486033`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5095498699909152`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_carpet_k8_seed3_head_pca_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
