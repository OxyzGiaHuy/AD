# Run p2_no_cache_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 runtime_no_cache --out-dir outputs/paper_tables --resume`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9479183332658181`
- `auroc`: `0.9002998500749625`
- `brier`: `0.2008929116946688`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22977215870904422`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003512794810036818`
- `max_f1`: `0.88`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7558576863610506`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/p2_runtime_no_cache/p2_no_cache_mvtec_cable_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
