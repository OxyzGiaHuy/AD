# Run patchcore_mvtec_metal_nut_k8_seed0_patchcore_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.995468137373171`
- `auroc`: `0.9809384164222874`
- `brier`: `0.78091194255746`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7882481883603918`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012370102901173675`
- `max_f1`: `0.9680851063829787`
- `model_storage_mb`: `6.0`
- `nll`: `3.310737355020418`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_metal_nut_k8_seed0_patchcore_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
