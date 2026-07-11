# Run ablation_alpha_0p75_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9419441551009029`
- `auroc`: `0.7877941763063422`
- `brier`: `0.1641512278964112`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1781703680753708`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0028925184442689924`
- `max_f1`: `0.9224137931034483`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5147845526585194`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
