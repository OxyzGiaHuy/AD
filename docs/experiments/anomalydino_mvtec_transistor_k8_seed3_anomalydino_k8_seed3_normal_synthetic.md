# Run anomalydino_mvtec_transistor_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_transistor_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8033174196355191`
- `auroc`: `0.8845833333333334`
- `brier`: `0.3791541363295774`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36526499355211856`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012297126483172178`
- `max_f1`: `0.813953488372093`
- `model_storage_mb`: `6.0`
- `nll`: `1.4690387302249512`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_transistor_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
