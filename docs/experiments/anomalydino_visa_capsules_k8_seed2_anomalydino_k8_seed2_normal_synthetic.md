# Run anomalydino_visa_capsules_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_capsules_k8_seed2.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.960131831524999`
- `auroc`: `0.9445`
- `brier`: `0.5974121788940907`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5953426211548504`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.08622861795593054`
- `max_f1`: `0.9306930693069307`
- `model_storage_mb`: `6.0`
- `nll`: `2.400324997869954`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_capsules_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
