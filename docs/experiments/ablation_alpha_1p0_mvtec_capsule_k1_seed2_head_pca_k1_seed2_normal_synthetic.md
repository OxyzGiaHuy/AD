# Run ablation_alpha_1p0_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_capsule_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9156633984481024`
- `auroc`: `0.7207818109293976`
- `brier`: `0.1535634278562419`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10228167429114843`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002323250314503005`
- `max_f1`: `0.9224137931034483`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.48934057941169506`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_capsule_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
