# Run ablation_alpha_0p0_mvtec_screw_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_screw_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8236425417775428`
- `auroc`: `0.6001229760196761`
- `brier`: `0.25580581880200076`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2563944550231099`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002374292479362339`
- `max_f1`: `0.8530465949820788`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7047620857795736`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_screw_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
