# Run calib_subspace_head_mvtec_tile_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9934380409059012`
- `auroc`: `0.9848484848484849`
- `brier`: `0.27742323281723935`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27968488646368694`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0012830810573620673`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.0461019017933997`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k1_seed0_calib_subspace_head_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
