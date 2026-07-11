# Run patchcore_mvtec_carpet_k1_seed3_patchcore_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_carpet_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9979883846749179`
- `auroc`: `0.9935794542536116`
- `brier`: `0.23931623931623933`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23931623931623935`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.005075648379249451`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.408368047692076`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_carpet_k1_seed3_patchcore_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
