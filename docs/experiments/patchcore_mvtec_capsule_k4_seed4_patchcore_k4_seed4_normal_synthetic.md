# Run patchcore_mvtec_capsule_k4_seed4_patchcore_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_capsule_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9742439916570224`
- `auroc`: `0.9038691663342641`
- `brier`: `0.7148484008103806`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7531844696989565`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012780715683192917`
- `max_f1`: `0.9422222222222222`
- `model_storage_mb`: `6.0`
- `nll`: `2.2094288754322338`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_capsule_k4_seed4_patchcore_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
