# Run anomalydino_mvtec_zipper_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_zipper_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.994885894398029`
- `auroc`: `0.9829306722689075`
- `brier`: `0.7790841241765087`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7781868869691644`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012821879422921218`
- `max_f1`: `0.9790794979079498`
- `model_storage_mb`: `6.0`
- `nll`: `4.234293892922333`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_zipper_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
