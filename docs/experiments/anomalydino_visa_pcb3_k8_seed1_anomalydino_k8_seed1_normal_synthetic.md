# Run anomalydino_visa_pcb3_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k8_seed1.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7674014174914311`
- `auroc`: `0.7935643564356436`
- `brier`: `0.48317843498158`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.47957441283723534`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.06898141636591942`
- `max_f1`: `0.7580645161290323`
- `model_storage_mb`: `6.0`
- `nll`: `2.1336240352087095`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
