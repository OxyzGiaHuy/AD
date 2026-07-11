# Run patchcore_mvtec_capsule_k8_seed1_patchcore_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_capsule_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9885588845252319`
- `auroc`: `0.947746310331073`
- `brier`: `0.7852999523109344`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7978415478190238`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.013189968949353153`
- `max_f1`: `0.963302752293578`
- `model_storage_mb`: `6.0`
- `nll`: `3.0769861209572436`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_capsule_k8_seed1_patchcore_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
