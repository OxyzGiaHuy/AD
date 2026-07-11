# Run ablation_alpha_0p0_mvtec_grid_k1_seed2_head_pca_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p0_mvtec_grid_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9598245198594175`
- `auroc`: `0.9055973266499582`
- `brier`: `0.256680630402027`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.34825197091469395`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0034610427295168242`
- `max_f1`: `0.9203539823008849`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.7065036989505306`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p0_mvtec_grid_k1_seed2_head_pca_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
