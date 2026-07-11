# Run patchcore_mvtec_tile_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_tile_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9950527336079512`
- `auroc`: `0.9884559884559885`
- `brier`: `0.7037642934955229`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7027078464937707`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012245060748651497`
- `max_f1`: `0.9767441860465116`
- `model_storage_mb`: `6.0`
- `nll`: `3.3740297183644232`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_tile_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
