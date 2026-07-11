# Run patchcore_mvtec_pill_k8_seed3_patchcore_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_pill_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9835271653058373`
- `auroc`: `0.9268957992362248`
- `brier`: `0.8099458000286646`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8213305085518224`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012314142625845835`
- `max_f1`: `0.9583333333333334`
- `model_storage_mb`: `6.0`
- `nll`: `3.31492256647968`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/patchcore_mvtec_pill_k8_seed3_patchcore_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
