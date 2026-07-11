# Run patchcore_mvtec_grid_k1_seed0_patchcore_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_grid_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.996100112959874`
- `auroc`: `0.9891395154553049`
- `brier`: `0.2692307692307692`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2692307692307693`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.003793666975047344`
- `max_f1`: `0.9739130434782609`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.959414052403588`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/patchcore_mvtec_grid_k1_seed0_patchcore_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
