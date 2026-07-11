# Run anomalydino_visa_pcb1_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb1_k4_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7553400666427611`
- `auroc`: `0.777`
- `brier`: `0.43457414632085956`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.42477216647937893`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.07334468227811158`
- `max_f1`: `0.751131221719457`
- `model_storage_mb`: `6.0`
- `nll`: `1.3656522799933253`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb1_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
