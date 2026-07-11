# Run anomalydino_mvtec_cable_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_cable_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9534734942451975`
- `auroc`: `0.9115442278860569`
- `brier`: `0.5932472168139753`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5917527134592334`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.01262267208347718`
- `max_f1`: `0.8783068783068783`
- `model_storage_mb`: `6.0`
- `nll`: `2.563294356640472`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_cable_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
