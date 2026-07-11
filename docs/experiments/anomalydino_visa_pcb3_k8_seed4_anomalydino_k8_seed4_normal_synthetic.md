# Run anomalydino_visa_pcb3_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_pcb3_k8_seed4.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.7208938186193978`
- `auroc`: `0.7426732673267327`
- `brier`: `0.4963467177295759`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4960484990096577`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.09164432038678162`
- `max_f1`: `0.7196652719665272`
- `model_storage_mb`: `6.0`
- `nll`: `3.4148801968512137`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_pcb3_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
