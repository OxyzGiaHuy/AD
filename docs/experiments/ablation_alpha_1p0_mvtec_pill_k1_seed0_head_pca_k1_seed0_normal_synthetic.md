# Run ablation_alpha_1p0_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_pill_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9368083842399217`
- `auroc`: `0.7210856519367158`
- `brier`: `0.14540805399545162`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11820044738803792`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00283063123906087`
- `max_f1`: `0.9235880398671097`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.47181310057610815`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_pill_k1_seed0_head_pca_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
