# Run calib_subspace_head_mvtec_tile_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9952906419907501`
- `auroc`: `0.9891774891774892`
- `brier`: `0.10146466332961994`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1269341541820357`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0012983878294372151`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5998184132039125`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
