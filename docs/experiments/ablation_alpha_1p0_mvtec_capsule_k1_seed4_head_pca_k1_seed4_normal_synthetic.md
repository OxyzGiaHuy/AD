# Run ablation_alpha_1p0_mvtec_capsule_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9347437973023034`
- `auroc`: `0.762664539289988`
- `brier`: `0.15331983083348727`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10643151583093582`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017513774448271954`
- `max_f1`: `0.9066666666666666`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.4885315974073992`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
