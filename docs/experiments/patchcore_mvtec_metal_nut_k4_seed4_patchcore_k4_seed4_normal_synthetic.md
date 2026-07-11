# Run patchcore_mvtec_metal_nut_k4_seed4_patchcore_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_metal_nut_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9782757020807423`
- `auroc`: `0.9271749755620723`
- `brier`: `0.7855121771759374`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.791855566519434`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012297461019909901`
- `max_f1`: `0.9587628865979382`
- `model_storage_mb`: `6.0`
- `nll`: `3.4518110210140986`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_metal_nut_k4_seed4_patchcore_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
