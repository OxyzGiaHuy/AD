# Run patchcore_mvtec_grid_k4_seed0_patchcore_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_grid_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.9970642204483386`
- `auroc`: `0.9916457811194653`
- `brier`: `0.7287647826550947`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7278556644838924`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012547863647341728`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `6.0`
- `nll`: `4.901433325430907`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_grid_k4_seed0_patchcore_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
