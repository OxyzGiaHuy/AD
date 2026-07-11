# Run anomalydino_visa_fryum_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/visa_full/anomalydino_visa_fryum_k8_seed3.yaml`
- Dataset: `visa`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9812112187145332`
- `auroc`: `0.958`
- `brier`: `0.6029203211943129`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6087639003495375`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.08475841913372278`
- `max_f1`: `0.9381443298969072`
- `model_storage_mb`: `6.0`
- `nll`: `2.0262368347156623`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_visa_fryum_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
