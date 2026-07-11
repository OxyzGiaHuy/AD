# Run patchcore_mvtec_grid_k1_seed2_patchcore_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_grid_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.998849582973828`
- `auroc`: `0.9966583124477861`
- `brier`: `0.2692307692307692`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2692307692307693`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004754143504378123`
- `max_f1`: `0.9911504424778761`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.959414052403588`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_grid_k1_seed2_patchcore_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
