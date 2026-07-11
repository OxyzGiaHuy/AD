# Run ablation_pca64_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_pill_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9775194481629853`
- `auroc`: `0.8911620294599017`
- `brier`: `0.15557813553860358`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15562348308677443`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0018133540487218047`
- `max_f1`: `0.9431438127090301`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.5542792056086625`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_pill_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
