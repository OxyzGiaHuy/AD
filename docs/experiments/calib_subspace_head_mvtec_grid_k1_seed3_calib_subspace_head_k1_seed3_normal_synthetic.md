# Run calib_subspace_head_mvtec_grid_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_grid_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9601180321331445`
- `auroc`: `0.908939014202172`
- `brier`: `0.2692224098133466`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2692265884998517`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0013070515571878506`
- `max_f1`: `0.95`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `3.9673828031792766`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_grid_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
