# Run ablation_alpha_0p25_mvtec_tile_k1_seed1_head_pca_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p25_mvtec_tile_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.9824464187174669`
- `auroc`: `0.9487734487734488`
- `brier`: `0.2250866825178249`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.35851869827661764`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001958268240858347`
- `max_f1`: `0.9325153374233128`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.6431450761841476`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_alpha_0p25_mvtec_tile_k1_seed1_head_pca_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
