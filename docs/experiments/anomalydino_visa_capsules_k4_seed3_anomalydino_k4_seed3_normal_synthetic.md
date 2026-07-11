# Run anomalydino_visa_capsules_k4_seed3_anomalydino_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_capsules_k4_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9533386859146264`
- `auroc`: `0.929`
- `brier`: `0.6221519915313098`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6211188717852565`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.09306508341105654`
- `max_f1`: `0.9117647058823529`
- `model_storage_mb`: `6.0`
- `nll`: `3.927656404515278`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_visa_capsules_k4_seed3_anomalydino_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
