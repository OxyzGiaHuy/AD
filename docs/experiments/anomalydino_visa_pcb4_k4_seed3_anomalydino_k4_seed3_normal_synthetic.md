# Run anomalydino_visa_pcb4_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb4_k4_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.820506660537585`
- `auroc`: `0.8601980198019802`
- `brier`: `0.36561356044702964`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.343171585925776`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.07624855315989226`
- `max_f1`: `0.8333333333333334`
- `model_storage_mb`: `6.0`
- `nll`: `1.0057263007510935`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb4_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
