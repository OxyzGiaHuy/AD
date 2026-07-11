# Run anomalydino_mvtec_carpet_k1_seed2_anomalydino_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_carpet_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9966751771418705`
- `auroc`: `0.9895666131621188`
- `brier`: `0.23931623931623933`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23931623931623935`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00501268837823827`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.408368047692076`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_carpet_k1_seed2_anomalydino_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
