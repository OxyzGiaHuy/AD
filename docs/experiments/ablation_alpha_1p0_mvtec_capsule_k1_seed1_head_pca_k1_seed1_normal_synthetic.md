# Run ablation_alpha_1p0_mvtec_capsule_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8853923035575564`
- `auroc`: `0.6262465097726366`
- `brier`: `0.1521319069653831`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10826469280503016`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001711395653811368`
- `max_f1`: `0.9191489361702128`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4859530356789853`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
