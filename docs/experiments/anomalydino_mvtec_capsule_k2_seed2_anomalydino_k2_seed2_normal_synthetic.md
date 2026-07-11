# Run anomalydino_mvtec_capsule_k2_seed2_anomalydino_k2_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_capsule_k2_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.976565453973761`
- `auroc`: `0.8970881531711209`
- `brier`: `0.17424242424242425`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1742424242424242`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008663246958431873`
- `max_f1`: `0.9375`
- `model_storage_mb`: `4.0107421875`
- `nll`: `3.2096640764040534`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_capsule_k2_seed2_anomalydino_k2_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
