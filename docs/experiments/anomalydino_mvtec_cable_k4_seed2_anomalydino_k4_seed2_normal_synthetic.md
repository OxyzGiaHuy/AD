# Run anomalydino_mvtec_cable_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_cable_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.959419007377414`
- `auroc`: `0.9265367316341829`
- `brier`: `0.6080939556453602`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.606852069950352`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012358917308350405`
- `max_f1`: `0.8695652173913043`
- `model_storage_mb`: `6.0`
- `nll`: `3.444557694387338`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_cable_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
