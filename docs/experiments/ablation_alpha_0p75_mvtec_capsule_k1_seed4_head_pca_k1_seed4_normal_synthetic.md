# Run ablation_alpha_0p75_mvtec_capsule_k1_seed4_head_pca_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_capsule_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.957590140042639`
- `auroc`: `0.8181092939768648`
- `brier`: `0.1653570435235287`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20531586580204245`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002439757329270695`
- `max_f1`: `0.9045643153526971`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5174330885440636`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_capsule_k1_seed4_head_pca_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
