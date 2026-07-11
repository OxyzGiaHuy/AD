# Run anomalydino_mvtec_grid_k1_seed3_anomalydino_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_grid_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9968462823725982`
- `auroc`: `0.9908103592314118`
- `brier`: `0.2692307692307692`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2692307692307693`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0046570234908125336`
- `max_f1`: `0.9734513274336283`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.959414052403588`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_grid_k1_seed3_anomalydino_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
