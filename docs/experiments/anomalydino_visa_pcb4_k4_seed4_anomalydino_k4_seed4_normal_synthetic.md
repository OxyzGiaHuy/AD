# Run anomalydino_visa_pcb4_k4_seed4_anomalydino_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb4_k4_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7889563895697497`
- `auroc`: `0.85`
- `brier`: `0.47266999211765476`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4688645948224993`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.07981975405333351`
- `max_f1`: `0.8412017167381974`
- `model_storage_mb`: `6.0`
- `nll`: `1.837632377312113`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb4_k4_seed4_anomalydino_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
