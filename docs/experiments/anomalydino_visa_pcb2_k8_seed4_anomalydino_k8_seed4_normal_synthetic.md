# Run anomalydino_visa_pcb2_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb2_k8_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.6951819802753286`
- `auroc`: `0.698`
- `brier`: `0.48320569851554057`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48042716095922516`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.06616917016915977`
- `max_f1`: `0.6827586206896552`
- `model_storage_mb`: `6.0`
- `nll`: `2.0797825449572707`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb2_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
