# Run anomalydino_mvtec_hazelnut_k1_seed4_anomalydino_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9796173004296508`
- `auroc`: `0.9664285714285714`
- `brier`: `0.36363636363636365`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.36363636363636365`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0050427559255199`
- `max_f1`: `0.9315068493150684`
- `model_storage_mb`: `2.00537109375`
- `nll`: `6.698429365973675`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k1_seed4_anomalydino_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
