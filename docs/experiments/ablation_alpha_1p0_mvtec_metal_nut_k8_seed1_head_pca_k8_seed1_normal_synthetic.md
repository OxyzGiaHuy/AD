# Run ablation_alpha_1p0_mvtec_metal_nut_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_metal_nut_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9930941150447894`
- `auroc`: `0.9696969696969697`
- `brier`: `0.15428058514232745`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1619228316389996`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022885714860066122`
- `max_f1`: `0.9613259668508287`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.48985366427785515`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_metal_nut_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
