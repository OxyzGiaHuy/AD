# Run anomalydino_visa_pcb2_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb2_k8_seed0.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7181334360509852`
- `auroc`: `0.751`
- `brier`: `0.4937140624820044`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.49191406843834556`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.080421919291839`
- `max_f1`: `0.7115384615384616`
- `model_storage_mb`: `6.0`
- `nll`: `2.612842189686512`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb2_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
