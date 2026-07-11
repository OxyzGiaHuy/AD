# Run anomalydino_visa_pcb4_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb4_k4_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7950847128611355`
- `auroc`: `0.8203960396039603`
- `brier`: `0.47741847694815776`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4728036982039759`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.07245468632758256`
- `max_f1`: `0.7787610619469026`
- `model_storage_mb`: `6.0`
- `nll`: `1.95154926522644`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb4_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
