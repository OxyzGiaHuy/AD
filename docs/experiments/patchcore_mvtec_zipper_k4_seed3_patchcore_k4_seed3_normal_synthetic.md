# Run patchcore_mvtec_zipper_k4_seed3_patchcore_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_zipper_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9963412727260212`
- `auroc`: `0.9868697478991597`
- `brier`: `0.7809630276168469`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7804557374602998`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012505200796372054`
- `max_f1`: `0.9743589743589743`
- `model_storage_mb`: `6.0`
- `nll`: `4.386773291373481`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_zipper_k4_seed3_patchcore_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
