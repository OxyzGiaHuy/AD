# Run anomalydino_mvtec_carpet_k2_seed4_anomalydino_k2_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_carpet_k2_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9989601064838266`
- `auroc`: `0.9967897271268058`
- `brier`: `0.23931623931623933`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23931623931623935`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008964130288770055`
- `max_f1`: `0.994413407821229`
- `model_storage_mb`: `4.0107421875`
- `nll`: `4.408368047692076`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_carpet_k2_seed4_anomalydino_k2_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
