# Run patchcore_mvtec_tile_k8_seed4_patchcore_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_tile_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9959992511265134`
- `auroc`: `0.990981240981241`
- `brier`: `0.7094556433388771`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7059583446144277`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012115293954554787`
- `max_f1`: `0.9880952380952381`
- `model_storage_mb`: `6.0`
- `nll`: `3.8469990579746023`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_tile_k8_seed4_patchcore_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
