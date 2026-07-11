# Run anomalydino_visa_pcb4_k2_seed3_anomalydino_k2_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb4_k2_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7786700085483469`
- `auroc`: `0.8322772277227722`
- `brier`: `0.5024875621890548`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5024875621890548`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.07864388822582527`
- `max_f1`: `0.8105726872246696`
- `model_storage_mb`: `4.0107421875`
- `nll`: `9.256162963341737`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb4_k2_seed3_anomalydino_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
