# Run anomalydino_mvtec_toothbrush_k4_seed4_anomalydino_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_toothbrush_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9405623143715474`
- `auroc`: `0.8722222222222222`
- `brier`: `0.6951387801879881`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6974842247686216`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012657664272756804`
- `max_f1`: `0.9230769230769231`
- `model_storage_mb`: `6.0`
- `nll`: `3.1011138533818996`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_toothbrush_k4_seed4_anomalydino_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
