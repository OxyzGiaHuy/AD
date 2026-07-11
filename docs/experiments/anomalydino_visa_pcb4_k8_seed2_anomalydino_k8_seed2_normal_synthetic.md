# Run anomalydino_visa_pcb4_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb4_k8_seed2.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7221482595030015`
- `auroc`: `0.7662376237623763`
- `brier`: `0.4513776769625032`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.45274608980734554`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09055747144591453`
- `max_f1`: `0.7359307359307359`
- `model_storage_mb`: `6.0`
- `nll`: `1.5315786662817843`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb4_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
