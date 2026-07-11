# Run patchcore_mvtec_tile_k4_seed2_patchcore_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9936700205362177`
- `auroc`: `0.9852092352092352`
- `brier`: `0.7098129171558747`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7061782275211129`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012495835749512045`
- `max_f1`: `0.9700598802395209`
- `model_storage_mb`: `6.0`
- `nll`: `3.8562193453971165`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_tile_k4_seed2_patchcore_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
