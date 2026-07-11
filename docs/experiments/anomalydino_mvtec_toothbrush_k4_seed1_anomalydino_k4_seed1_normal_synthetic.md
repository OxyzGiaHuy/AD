# Run anomalydino_mvtec_toothbrush_k4_seed1_anomalydino_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_toothbrush_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9594423391446762`
- `auroc`: `0.9194444444444444`
- `brier`: `0.6831944638331393`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6873639652150728`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01272353729499238`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `6.0`
- `nll`: `2.7377908428077427`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_toothbrush_k4_seed1_anomalydino_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
