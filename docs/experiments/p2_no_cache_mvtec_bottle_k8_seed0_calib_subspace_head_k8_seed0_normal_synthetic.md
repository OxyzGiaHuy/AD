# Run p2_no_cache_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 runtime_no_cache --out-dir outputs/paper_tables --resume`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9953837495276107`
- `auroc`: `0.9865079365079366`
- `brier`: `0.05613434081495258`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.08070001959890488`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013483004218124482`
- `max_f1`: `0.984375`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.22876804355627794`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/p2_runtime_no_cache/p2_no_cache_mvtec_bottle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
