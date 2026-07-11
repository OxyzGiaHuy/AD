# Run ablation_alpha_0p0_mvtec_toothbrush_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_toothbrush_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.978379479997127`
- `auroc`: `0.9416666666666667`
- `brier`: `0.2503618460962003`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2732149440617788`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004068644096453984`
- `max_f1`: `0.9090909090909091`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6938608303616409`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_toothbrush_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
