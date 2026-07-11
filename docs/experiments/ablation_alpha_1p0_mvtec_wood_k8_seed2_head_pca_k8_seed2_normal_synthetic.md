# Run ablation_alpha_1p0_mvtec_wood_k8_seed2_head_pca_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_wood_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.998024728907637`
- `auroc`: `0.993859649122807`
- `brier`: `0.1741717775958678`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.028773417201223214`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018320662688605393`
- `max_f1`: `0.9836065573770492`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5283907947620464`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_wood_k8_seed2_head_pca_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
