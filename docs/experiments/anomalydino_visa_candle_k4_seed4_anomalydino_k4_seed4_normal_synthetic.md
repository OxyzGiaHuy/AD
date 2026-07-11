# Run anomalydino_visa_candle_k4_seed4_anomalydino_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_candle_k4_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8300568527048867`
- `auroc`: `0.8567`
- `brier`: `0.4773999619526681`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.47094500246923415`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.07399072768166662`
- `max_f1`: `0.8071748878923767`
- `model_storage_mb`: `6.0`
- `nll`: `1.91096731585547`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_candle_k4_seed4_anomalydino_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
