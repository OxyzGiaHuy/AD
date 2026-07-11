# Run anomalydino_visa_pcb3_k2_seed4_anomalydino_k2_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k2_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7146973223050503`
- `auroc`: `0.7453465346534653`
- `brier`: `0.5024875621890548`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5024875621890548`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0734543240541101`
- `max_f1`: `0.7158671586715867`
- `model_storage_mb`: `4.0107421875`
- `nll`: `9.256162963341737`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k2_seed4_anomalydino_k2_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
