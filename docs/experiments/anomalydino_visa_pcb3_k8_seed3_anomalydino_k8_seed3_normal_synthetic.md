# Run anomalydino_visa_pcb3_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k8_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8269995658512176`
- `auroc`: `0.8148514851485148`
- `brier`: `0.4961273236337318`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4956787234069131`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.07842840944690194`
- `max_f1`: `0.752`
- `model_storage_mb`: `6.0`
- `nll`: `3.3165622545385474`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
