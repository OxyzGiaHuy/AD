# Run anomalydino_visa_pcb2_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb2_k4_seed2.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.6968850528031806`
- `auroc`: `0.7274`
- `brier`: `0.4783308779790441`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.474793638815172`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.11283419749699533`
- `max_f1`: `0.7206477732793523`
- `model_storage_mb`: `6.0`
- `nll`: `1.9383541035777494`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb2_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
