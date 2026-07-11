# Run anomalydino_visa_pcb1_k4_seed4_anomalydino_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb1_k4_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8055956537264549`
- `auroc`: `0.8588`
- `brier`: `0.49288072854627507`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48980928758275694`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.07115781203843653`
- `max_f1`: `0.8115942028985508`
- `model_storage_mb`: `6.0`
- `nll`: `2.5068840345274657`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb1_k4_seed4_anomalydino_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
