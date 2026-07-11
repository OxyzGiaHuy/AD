# Run patchcore_mvtec_tile_k4_seed4_patchcore_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_tile_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.7176474168948949`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.716818171350442`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012292005344588533`
- `max_f1`: `1.0`
- `model_storage_mb`: `6.0`
- `nll`: `6.67286703819095`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_tile_k4_seed4_patchcore_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
