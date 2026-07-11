# Run anomalydino_mvtec_grid_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_grid_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9991228070175439`
- `auroc`: `0.9974937343358395`
- `brier`: `0.717302435658008`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7163445722544566`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0122076096968391`
- `max_f1`: `0.9911504424778761`
- `model_storage_mb`: `6.0`
- `nll`: `3.4493485192745115`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_grid_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
