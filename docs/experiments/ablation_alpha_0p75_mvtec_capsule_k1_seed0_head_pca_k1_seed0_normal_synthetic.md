# Run ablation_alpha_0p75_mvtec_capsule_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9497511549707842`
- `auroc`: `0.788193059433586`
- `brier`: `0.16645648195246227`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.16028683564879675`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022019808406405377`
- `max_f1`: `0.9121338912133892`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5201266946254766`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
