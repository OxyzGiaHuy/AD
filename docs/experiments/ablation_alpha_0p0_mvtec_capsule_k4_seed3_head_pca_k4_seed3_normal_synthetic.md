# Run ablation_alpha_0p0_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_capsule_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9731660286901723`
- `auroc`: `0.8871160749900279`
- `brier`: `0.24064451998794256`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3206941178350737`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00329342322198279`
- `max_f1`: `0.9333333333333333`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6744147782075769`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_capsule_k4_seed3_head_pca_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
