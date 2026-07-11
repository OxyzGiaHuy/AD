# Run anomalydino_mvtec_grid_k2_seed0_anomalydino_k2_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_grid_k2_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9982285127544198`
- `auroc`: `0.9949874686716792`
- `brier`: `0.2692307692307692`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2692307692307693`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008552605596681436`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `4.0107421875`
- `nll`: `4.959414052403588`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_grid_k2_seed0_anomalydino_k2_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
