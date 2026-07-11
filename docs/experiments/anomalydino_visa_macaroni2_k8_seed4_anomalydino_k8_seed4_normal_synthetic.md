# Run anomalydino_visa_macaroni2_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_macaroni2_k8_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7992957846212441`
- `auroc`: `0.791`
- `brier`: `0.4839956224724109`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.48067671758355573`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09936409421265126`
- `max_f1`: `0.7449392712550608`
- `model_storage_mb`: `6.0`
- `nll`: `2.0959098463134156`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_macaroni2_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
