# Run p2_no_cache_visa_candle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `scripts/run_p2_priority_experiments.py --tasks visa_pca128 runtime_no_cache --out-dir outputs/paper_tables --resume`
- Dataset: `visa`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8624320276872788`
- `auroc`: `0.8715`
- `brier`: `0.49116540748260235`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.49520721763372416`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005332932081073522`
- `max_f1`: `0.8144796380090498`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `4.884539041498094`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/p2_runtime_no_cache/p2_no_cache_visa_candle_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
