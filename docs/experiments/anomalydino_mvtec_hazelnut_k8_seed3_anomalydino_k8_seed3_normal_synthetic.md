# Run anomalydino_mvtec_hazelnut_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9968870278536006`
- `auroc`: `0.995`
- `brier`: `0.618686910345048`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6165565696375613`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01259468404406851`
- `max_f1`: `0.9929078014184397`
- `model_storage_mb`: `6.0`
- `nll`: `2.7362370699711933`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
