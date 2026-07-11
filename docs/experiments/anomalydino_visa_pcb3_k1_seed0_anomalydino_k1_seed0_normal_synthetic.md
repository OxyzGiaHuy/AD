# Run anomalydino_visa_pcb3_k1_seed0_anomalydino_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k1_seed0.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7446265549431739`
- `auroc`: `0.7438613861386139`
- `brier`: `0.5024875621890548`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5024875621890548`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.06526968876520793`
- `max_f1`: `0.7169811320754716`
- `model_storage_mb`: `2.00537109375`
- `nll`: `9.256162963341737`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k1_seed0_anomalydino_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
