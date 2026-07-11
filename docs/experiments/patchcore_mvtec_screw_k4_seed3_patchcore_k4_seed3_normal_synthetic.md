# Run patchcore_mvtec_screw_k4_seed3_patchcore_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.841823928361695`
- `auroc`: `0.7353965976634557`
- `brier`: `0.7101830572673004`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7189430364232976`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012546632438898087`
- `max_f1`: `0.8932806324110671`
- `model_storage_mb`: `6.0`
- `nll`: `2.8361303489130503`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_screw_k4_seed3_patchcore_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
