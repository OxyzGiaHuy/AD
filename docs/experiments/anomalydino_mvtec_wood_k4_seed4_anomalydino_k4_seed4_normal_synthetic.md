# Run anomalydino_mvtec_wood_k4_seed4_anomalydino_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_wood_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9927073633952852`
- `auroc`: `0.9763157894736842`
- `brier`: `0.7513849438795287`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7515937373118735`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01255312123441998`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `6.0`
- `nll`: `4.017925571508115`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_wood_k4_seed4_anomalydino_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
