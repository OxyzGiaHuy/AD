# Run anomalydino_visa_pcb2_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb2_k4_seed0.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.6872931065717868`
- `auroc`: `0.7056`
- `brier`: `0.49716297571984974`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.49634053862755534`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.06775641988962888`
- `max_f1`: `0.7111111111111111`
- `model_storage_mb`: `6.0`
- `nll`: `3.0635554079188343`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb2_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
