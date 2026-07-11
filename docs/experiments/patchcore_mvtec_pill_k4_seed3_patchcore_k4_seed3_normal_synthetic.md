# Run patchcore_mvtec_pill_k4_seed3_patchcore_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_pill_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9910778871405324`
- `auroc`: `0.955264593562466`
- `brier`: `0.7930311460400935`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8109957739197744`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012261020644250031`
- `max_f1`: `0.9562043795620438`
- `model_storage_mb`: `6.0`
- `nll`: `2.9548520222077346`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_pill_k4_seed3_patchcore_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
