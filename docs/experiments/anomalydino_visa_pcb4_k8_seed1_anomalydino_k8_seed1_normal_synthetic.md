# Run anomalydino_visa_pcb4_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb4_k8_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7424626179280817`
- `auroc`: `0.7713861386138614`
- `brier`: `0.4692387070369121`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.46355811654780044`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09561296269779478`
- `max_f1`: `0.782258064516129`
- `model_storage_mb`: `6.0`
- `nll`: `1.780713528810093`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb4_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
