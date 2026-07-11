# Run anomalydino_visa_pcb4_k1_seed1_anomalydino_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb4_k1_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7581226816759188`
- `auroc`: `0.806930693069307`
- `brier`: `0.5024875621890548`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5024875621890548`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.07320007878304714`
- `max_f1`: `0.7764705882352941`
- `model_storage_mb`: `2.00537109375`
- `nll`: `9.256162963341737`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb4_k1_seed1_anomalydino_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
