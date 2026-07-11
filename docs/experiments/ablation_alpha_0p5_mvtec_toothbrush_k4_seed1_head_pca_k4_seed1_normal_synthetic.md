# Run ablation_alpha_0p5_mvtec_toothbrush_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_toothbrush_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9869942243146266`
- `auroc`: `0.9638888888888889`
- `brier`: `0.20516962237845612`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14816047038350788`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0048988281882234985`
- `max_f1`: `0.9491525423728814`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6013620588588483`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_toothbrush_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
