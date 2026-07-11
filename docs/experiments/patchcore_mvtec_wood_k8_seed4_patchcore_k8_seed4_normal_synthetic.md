# Run patchcore_mvtec_wood_k8_seed4_patchcore_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_wood_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9911525058044882`
- `auroc`: `0.9736842105263158`
- `brier`: `0.7420604644993652`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7435413794002579`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012402570888965944`
- `max_f1`: `0.9752066115702479`
- `model_storage_mb`: `6.0`
- `nll`: `3.41549463071526`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_wood_k8_seed4_patchcore_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
