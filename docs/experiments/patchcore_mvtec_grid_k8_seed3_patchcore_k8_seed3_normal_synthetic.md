# Run patchcore_mvtec_grid_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_grid_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.6594962480595546`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6913305521488955`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01249204848248225`
- `max_f1`: `1.0`
- `model_storage_mb`: `6.0`
- `nll`: `2.197062065171952`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_grid_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
