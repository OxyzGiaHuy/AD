# Run patchcore_mvtec_tile_k4_seed1_patchcore_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_tile_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.998675902200269`
- `auroc`: `0.9967532467532467`
- `brier`: `0.7040170343455939`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.701020148357886`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012842538694922741`
- `max_f1`: `0.9940828402366864`
- `model_storage_mb`: `6.0`
- `nll`: `3.4275846366054354`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_tile_k4_seed1_patchcore_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
