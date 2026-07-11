# Run anomalydino_visa_pcb4_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb4_k8_seed0.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7419824428630295`
- `auroc`: `0.8037623762376238`
- `brier`: `0.45912288034749854`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.454194874071808`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.1049744950431348`
- `max_f1`: `0.788135593220339`
- `model_storage_mb`: `6.0`
- `nll`: `1.623905629734308`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb4_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
