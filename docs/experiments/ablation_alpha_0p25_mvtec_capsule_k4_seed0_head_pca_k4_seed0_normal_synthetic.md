# Run ablation_alpha_0p25_mvtec_capsule_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_capsule_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9559935437929681`
- `auroc`: `0.8352612684483446`
- `brier`: `0.2042849613625139`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2900064648552374`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025265405349659195`
- `max_f1`: `0.9191489361702128`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6009810879504967`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_capsule_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
