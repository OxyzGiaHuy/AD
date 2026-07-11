# Run calib_subspace_head_mvtec_grid_k2_seed3_calib_subspace_head_k2_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_grid_k2_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9946360359612121`
- `auroc`: `0.985797827903091`
- `brier`: `0.2681107201529294`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.26841646203627956`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0013219801804576165`
- `max_f1`: `0.9734513274336283`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.7335984854409918`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_grid_k2_seed3_calib_subspace_head_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
