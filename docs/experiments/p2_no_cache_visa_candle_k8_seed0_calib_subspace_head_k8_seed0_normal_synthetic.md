# Run p2_no_cache_visa_candle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 runtime_no_cache --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8713067057939664`
- `auroc`: `0.8837`
- `brier`: `0.17847666907363263`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19089140300871804`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.007692001014947891`
- `max_f1`: `0.8415841584158416`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.7417165745470907`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/p2_runtime_no_cache/p2_no_cache_visa_candle_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
