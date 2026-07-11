# Run anomalydino_mvtec_metal_nut_k2_seed1_anomalydino_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_metal_nut_k2_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9946613084385615`
- `auroc`: `0.9775171065493646`
- `brier`: `0.19130434782608696`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19130434782608696`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008512465380456137`
- `max_f1`: `0.9732620320855615`
- `model_storage_mb`: `4.0107421875`
- `nll`: `3.5239563233600646`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_metal_nut_k2_seed1_anomalydino_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
