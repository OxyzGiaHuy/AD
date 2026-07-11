# Run anomalydino_mvtec_screw_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_screw_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8782832454720855`
- `auroc`: `0.7747489239598279`
- `brier`: `0.6453848980897697`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6726020453032105`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012685156136285514`
- `max_f1`: `0.88`
- `model_storage_mb`: `6.0`
- `nll`: `2.0048315229821285`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_screw_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
