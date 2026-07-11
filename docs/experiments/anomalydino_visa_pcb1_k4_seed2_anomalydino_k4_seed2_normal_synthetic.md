# Run anomalydino_visa_pcb1_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb1_k4_seed2.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8381282511418946`
- `auroc`: `0.8991`
- `brier`: `0.4894271799944688`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48537922113202514`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.07380000050179661`
- `max_f1`: `0.8557213930348259`
- `model_storage_mb`: `6.0`
- `nll`: `2.2898795501155393`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb1_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
