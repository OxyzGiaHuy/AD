# Run patchcore_mvtec_pill_k4_seed0_patchcore_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_pill_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.985788988829833`
- `auroc`: `0.9326241134751773`
- `brier`: `0.8088817971737626`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.820938503291614`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012348601973788467`
- `max_f1`: `0.9488054607508533`
- `model_storage_mb`: `6.0`
- `nll`: `3.2875532660032056`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_pill_k4_seed0_patchcore_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
