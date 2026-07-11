# Run anomalydino_mvtec_carpet_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_carpet_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.99949912793935`
- `auroc`: `0.9983948635634029`
- `brier`: `0.7419189327835239`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7440480829741901`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01241275961073036`
- `max_f1`: `0.9888888888888889`
- `model_storage_mb`: `6.0`
- `nll`: `3.349389607804277`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_carpet_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
