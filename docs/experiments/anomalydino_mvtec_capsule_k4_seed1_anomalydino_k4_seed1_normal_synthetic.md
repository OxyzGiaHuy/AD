# Run anomalydino_mvtec_capsule_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_capsule_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9807582115683657`
- `auroc`: `0.9154367770243319`
- `brier`: `0.8250295705954499`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8250862537304949`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01288158804968451`
- `max_f1`: `0.9439252336448598`
- `model_storage_mb`: `6.0`
- `nll`: `6.707135254625478`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_capsule_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
