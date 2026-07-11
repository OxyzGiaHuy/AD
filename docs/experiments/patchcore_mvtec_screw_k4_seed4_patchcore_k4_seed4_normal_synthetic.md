# Run patchcore_mvtec_screw_k4_seed4_patchcore_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/patchcore_mvtec_screw_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `patchcore`

## Metrics

- `ap`: `0.7984195438639642`
- `auroc`: `0.6607911457265833`
- `brier`: `0.7382832230414584`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7395103892100451`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012445298582315445`
- `max_f1`: `0.8712121212121212`
- `model_storage_mb`: `6.0`
- `nll`: `4.2694273250061645`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/patchcore_mvtec_screw_k4_seed4_patchcore_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
