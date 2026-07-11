# Run patchcore_mvtec_tile_k4_seed3_patchcore_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_tile_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9961024601532296`
- `auroc`: `0.9906204906204906`
- `brier`: `0.7044595062447983`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7011461063411533`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012218413508345937`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `6.0`
- `nll`: `3.4560252193110776`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_tile_k4_seed3_patchcore_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
