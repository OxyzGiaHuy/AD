# Run ablation_alpha_0p0_mvtec_transistor_k8_seed0_head_pca_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_transistor_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8179823462086027`
- `auroc`: `0.85125`
- `brier`: `0.2373320708293549`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11334668785333636`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00216417433694005`
- `max_f1`: `0.7391304347826086`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6677698516150374`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_transistor_k8_seed0_head_pca_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
