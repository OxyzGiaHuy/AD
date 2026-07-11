# Run anomalydino_visa_pcb3_k2_seed1_anomalydino_k2_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k2_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7624856366258203`
- `auroc`: `0.7783168316831683`
- `brier`: `0.5024875621890548`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5024875621890548`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.09530633771375044`
- `max_f1`: `0.7522123893805309`
- `model_storage_mb`: `4.0107421875`
- `nll`: `9.256162963341737`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k2_seed1_anomalydino_k2_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
