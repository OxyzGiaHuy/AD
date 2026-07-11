# Run anomalydino_mvtec_transistor_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_transistor_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8424740114316915`
- `auroc`: `0.89375`
- `brier`: `0.34289705950489185`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.31143644616007804`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012476840503513813`
- `max_f1`: `0.810126582278481`
- `model_storage_mb`: `6.0`
- `nll`: `1.0644112324063502`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_transistor_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
