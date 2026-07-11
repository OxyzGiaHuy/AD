# Run anomalydino_mvtec_transistor_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_transistor_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8387833013667297`
- `auroc`: `0.8929166666666667`
- `brier`: `0.38276478002651565`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.37017619688995185`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012909805439412593`
- `max_f1`: `0.8045977011494253`
- `model_storage_mb`: `6.0`
- `nll`: `1.5484665879697384`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_transistor_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
