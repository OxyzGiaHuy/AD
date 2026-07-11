# Run anomalydino_visa_pcb2_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb2_k8_seed2.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.6979424986646634`
- `auroc`: `0.7271`
- `brier`: `0.46657095823086164`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4620279341284186`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09059557682834565`
- `max_f1`: `0.7123287671232876`
- `model_storage_mb`: `6.0`
- `nll`: `1.7101167332641853`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb2_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
