# Run ablation_alpha_0p0_mvtec_toothbrush_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_toothbrush_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9866652428088227`
- `auroc`: `0.9666666666666667`
- `brier`: `0.24761336969483197`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22481430996031992`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004772730570818696`
- `max_f1`: `0.9508196721311475`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6883650371386656`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_toothbrush_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
