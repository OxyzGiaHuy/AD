# Run ablation_alpha_0p25_mvtec_grid_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_grid_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9675462335206241`
- `auroc`: `0.9131161236424394`
- `brier`: `0.22634394565338786`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26851577942187976`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001934743008743494`
- `max_f1`: `0.918918918918919`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6456534080494775`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_grid_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
