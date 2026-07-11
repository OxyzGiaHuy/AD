# Run anomalydino_visa_pcb3_k2_seed0_anomalydino_k2_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k2_seed0.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7490997670214906`
- `auroc`: `0.7530693069306931`
- `brier`: `0.5024875621890548`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5024875621890548`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.10653855336542746`
- `max_f1`: `0.7387387387387387`
- `model_storage_mb`: `4.0107421875`
- `nll`: `9.256162963341737`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k2_seed0_anomalydino_k2_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
