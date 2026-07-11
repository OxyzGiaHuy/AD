# Run ablation_alpha_0p75_mvtec_metal_nut_k4_seed0_head_pca_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_metal_nut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9930412572953932`
- `auroc`: `0.9711632453567938`
- `brier`: `0.1627236329948126`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18827893008356508`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002734797383132188`
- `max_f1`: `0.972972972972973`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5104172809781126`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_metal_nut_k4_seed0_head_pca_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
