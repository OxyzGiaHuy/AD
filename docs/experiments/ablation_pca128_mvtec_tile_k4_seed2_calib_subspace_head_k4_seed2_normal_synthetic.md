# Run ablation_pca128_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9928095034439368`
- `auroc`: `0.983044733044733`
- `brier`: `0.13789211656483483`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17709756890932726`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003623345261837682`
- `max_f1`: `0.9655172413793104`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.6455893279492583`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
