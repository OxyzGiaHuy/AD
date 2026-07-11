# Run anomalydino_mvtec_metal_nut_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_metal_nut_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.997072735676865`
- `auroc`: `0.9872922776148583`
- `brier`: `0.7477223040374108`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7718943683673506`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01263739756591942`
- `max_f1`: `0.9735449735449735`
- `model_storage_mb`: `6.0`
- `nll`: `2.6471116142168802`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_metal_nut_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
