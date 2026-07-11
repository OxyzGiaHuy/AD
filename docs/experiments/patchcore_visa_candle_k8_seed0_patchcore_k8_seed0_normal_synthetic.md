# Run patchcore_visa_candle_k8_seed0_patchcore_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/patchcore_visa_candle_k8_seed0.yaml`
- Dataset: `visa`
- Model: `patchcore`

## Metrics

- `ap`: `0.8784827673210296`
- `auroc`: `0.8936`
- `brier`: `0.48575660287808115`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.47971712884958834`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.06479899948462844`
- `max_f1`: `0.8450704225352113`
- `model_storage_mb`: `6.0`
- `nll`: `2.1540233239074733`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_visa_candle_k8_seed0_patchcore_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
