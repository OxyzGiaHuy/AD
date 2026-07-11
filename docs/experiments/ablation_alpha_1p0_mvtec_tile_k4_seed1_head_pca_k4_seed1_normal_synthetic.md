# Run ablation_alpha_1p0_mvtec_tile_k4_seed1_head_pca_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_1p0_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.988814256820453`
- `auroc`: `0.9682539682539683`
- `brier`: `0.19043510540039751`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2189899270351116`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024607758491467205`
- `max_f1`: `0.9473684210526315`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5655608903313633`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_alpha_1p0_mvtec_tile_k4_seed1_head_pca_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
