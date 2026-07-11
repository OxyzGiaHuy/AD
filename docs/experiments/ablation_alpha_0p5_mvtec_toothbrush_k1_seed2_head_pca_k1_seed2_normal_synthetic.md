# Run ablation_alpha_0p5_mvtec_toothbrush_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_toothbrush_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9611163808312109`
- `auroc`: `0.8944444444444445`
- `brier`: `0.211038046679112`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09948990742365516`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001986970282381489`
- `max_f1`: `0.8813559322033898`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6138321722330128`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_toothbrush_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
