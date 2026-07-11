# Run patchcore_mvtec_bottle_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_bottle_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9898438419747954`
- `auroc`: `0.9722222222222222`
- `brier`: `0.7341530799198939`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7370261394093374`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012403375525251928`
- `max_f1`: `0.984375`
- `model_storage_mb`: `6.0`
- `nll`: `3.1449793953850405`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_bottle_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
