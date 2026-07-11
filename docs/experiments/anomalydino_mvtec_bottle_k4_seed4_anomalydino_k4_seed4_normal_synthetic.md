# Run anomalydino_mvtec_bottle_k4_seed4_anomalydino_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_bottle_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9997519841269841`
- `auroc`: `0.9992063492063492`
- `brier`: `0.7457746500737058`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7457432183689516`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01297950170126306`
- `max_f1`: `0.9921259842519685`
- `model_storage_mb`: `6.0`
- `nll`: `3.642586079758217`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_bottle_k4_seed4_anomalydino_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
