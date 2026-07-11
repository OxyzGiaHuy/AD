# Run ablation_alpha_0p75_mvtec_capsule_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.8524258983823014`
- `auroc`: `0.6043079377742322`
- `brier`: `0.16355478893356754`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16586341099305588`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002091687454870253`
- `max_f1`: `0.9191489361702128`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5135331384525555`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
