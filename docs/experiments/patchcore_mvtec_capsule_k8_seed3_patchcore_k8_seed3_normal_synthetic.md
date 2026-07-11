# Run patchcore_mvtec_capsule_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9797209179150671`
- `auroc`: `0.9154367770243319`
- `brier`: `0.8114855369242547`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8152176085630235`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012350433054521229`
- `max_f1`: `0.9411764705882353`
- `model_storage_mb`: `6.0`
- `nll`: `3.990534539160116`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_capsule_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
