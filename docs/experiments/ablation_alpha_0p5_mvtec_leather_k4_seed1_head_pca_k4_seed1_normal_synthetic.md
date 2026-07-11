# Run ablation_alpha_0p5_mvtec_leather_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p5_mvtec_leather_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9990894355453852`
- `auroc`: `0.9972826086956522`
- `brier`: `0.1844666790673275`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18790622223769465`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003690093740700714`
- `max_f1`: `0.989010989010989`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5575693339355078`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p5_mvtec_leather_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
