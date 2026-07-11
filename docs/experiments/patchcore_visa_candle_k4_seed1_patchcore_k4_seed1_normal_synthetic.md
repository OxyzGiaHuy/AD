# Run patchcore_visa_candle_k4_seed1_patchcore_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_candle_k4_seed1.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.8784679135995975`
- `auroc`: `0.8917`
- `brier`: `0.4884229549550074`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4829833795747254`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.05211767916567624`
- `max_f1`: `0.8372093023255814`
- `model_storage_mb`: `6.0`
- `nll`: `2.2618752977775087`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_visa_candle_k4_seed1_patchcore_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
