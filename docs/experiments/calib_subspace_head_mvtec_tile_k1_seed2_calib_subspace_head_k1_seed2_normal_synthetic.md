# Run calib_subspace_head_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9920414996777024`
- `auroc`: `0.9812409812409812`
- `brier`: `0.27139321830757085`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.27621454560858577`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0012955700453275289`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.9307165519285774`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
