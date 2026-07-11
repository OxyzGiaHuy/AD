# Run patchcore_mvtec_grid_k4_seed3_patchcore_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_grid_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.999697519661222`
- `auroc`: `0.9991645781119465`
- `brier`: `0.717945490296632`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7171030355265172`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012403813429558888`
- `max_f1`: `0.991304347826087`
- `model_storage_mb`: `6.0`
- `nll`: `3.4789269877079403`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_grid_k4_seed3_patchcore_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
