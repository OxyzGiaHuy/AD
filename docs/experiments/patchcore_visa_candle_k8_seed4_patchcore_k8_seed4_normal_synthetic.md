# Run patchcore_visa_candle_k8_seed4_patchcore_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_candle_k8_seed4.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.8270504194788038`
- `auroc`: `0.8683`
- `brier`: `0.4855006329200826`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4805890211462975`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.08621803621761501`
- `max_f1`: `0.8125`
- `model_storage_mb`: `6.0`
- `nll`: `2.138398875682341`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_candle_k8_seed4_patchcore_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
