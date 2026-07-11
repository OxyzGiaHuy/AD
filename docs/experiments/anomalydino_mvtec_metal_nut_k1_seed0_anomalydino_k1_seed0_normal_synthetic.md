# Run anomalydino_mvtec_metal_nut_k1_seed0_anomalydino_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_metal_nut_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9911878827192696`
- `auroc`: `0.9638318670576735`
- `brier`: `0.19130434782608696`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.19130434782608696`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003806325485524924`
- `max_f1`: `0.9587628865979382`
- `model_storage_mb`: `2.00537109375`
- `nll`: `3.5239563233600646`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_metal_nut_k1_seed0_anomalydino_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
