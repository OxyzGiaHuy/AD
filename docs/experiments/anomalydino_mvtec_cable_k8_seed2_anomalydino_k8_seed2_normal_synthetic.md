# Run anomalydino_mvtec_cable_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_cable_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9512239439415336`
- `auroc`: `0.9092953523238381`
- `brier`: `0.5939866615960622`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5924494546093046`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012267028292020163`
- `max_f1`: `0.8617021276595744`
- `model_storage_mb`: `6.0`
- `nll`: `2.5893462131705065`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_cable_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
