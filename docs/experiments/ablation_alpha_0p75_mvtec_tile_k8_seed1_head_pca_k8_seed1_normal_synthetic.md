# Run ablation_alpha_0p75_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_alpha_0p75_mvtec_tile_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `head_pca`

## Metrics

- `ap`: `0.98719678805309`
- `auroc`: `0.9675324675324676`
- `brier`: `0.18006454479411213`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.29201108471960086`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0018943501875186579`
- `max_f1`: `0.9647058823529412`
- `model_storage_mb`: `0.4721717834472656`
- `nll`: `0.5453748343995904`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_alpha_0p75_mvtec_tile_k8_seed1_head_pca_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
