# Run anomalydino_mvtec_pill_k8_seed1_anomalydino_k8_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_pill_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9828069028211711`
- `auroc`: `0.9192580469176214`
- `brier`: `0.8442052675873029`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.8442163913238969`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012507738400540666`
- `max_f1`: `0.9424460431654677`
- `model_storage_mb`: `6.0`
- `nll`: `8.51472183492767`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_pill_k8_seed1_anomalydino_k8_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
