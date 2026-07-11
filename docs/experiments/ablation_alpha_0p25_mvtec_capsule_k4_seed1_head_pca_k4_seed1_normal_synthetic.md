# Run ablation_alpha_0p25_mvtec_capsule_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_capsule_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9813336233634179`
- `auroc`: `0.9130434782608695`
- `brier`: `0.2026663472131028`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.30378195011254516`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019824588106888714`
- `max_f1`: `0.9310344827586207`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5977397081580905`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_capsule_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
