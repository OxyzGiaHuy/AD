# Run ablation_alpha_0p75_mvtec_cable_k1_seed3_head_pca_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_cable_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9466708438893473`
- `auroc`: `0.8997376311844077`
- `brier`: `0.23880631136295263`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.05719612121582032`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002716593109071255`
- `max_f1`: `0.8615384615384616`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6707774111982323`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_cable_k1_seed3_head_pca_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
