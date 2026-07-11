# Run anomalydino_visa_pcb2_k4_seed4_anomalydino_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb2_k4_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.6598843928001097`
- `auroc`: `0.6806`
- `brier`: `0.4826832979263813`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48031323242466895`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.09008036246523261`
- `max_f1`: `0.6932270916334662`
- `model_storage_mb`: `6.0`
- `nll`: `2.0509785904558213`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb2_k4_seed4_anomalydino_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
