# Run patchcore_mvtec_grid_k8_seed1_patchcore_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_grid_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.7167706243485232`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7157910824036942`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012312843535955135`
- `max_f1`: `1.0`
- `model_storage_mb`: `6.0`
- `nll`: `3.4226849442794274`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_grid_k8_seed1_patchcore_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
