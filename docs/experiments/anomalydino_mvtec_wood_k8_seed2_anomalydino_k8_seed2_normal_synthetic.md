# Run anomalydino_mvtec_wood_k8_seed2_anomalydino_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_wood_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9855878701664029`
- `auroc`: `0.956140350877193`
- `brier`: `0.7487404841503223`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7492927853165408`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012255811780879769`
- `max_f1`: `0.9516129032258065`
- `model_storage_mb`: `6.0`
- `nll`: `3.8000004278267263`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_wood_k8_seed2_anomalydino_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
