# Run p2_no_cache_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 runtime_no_cache --out-dir outputs/paper_tables --resume`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9820928868310992`
- `auroc`: `0.9626984126984127`
- `brier`: `0.23387656254166012`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23730877005910295`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001380303178925112`
- `max_f1`: `0.9763779527559056`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.46803945043625`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/p2_runtime_no_cache/p2_no_cache_mvtec_bottle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
