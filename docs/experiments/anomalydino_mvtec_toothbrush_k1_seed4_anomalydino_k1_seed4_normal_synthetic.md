# Run anomalydino_mvtec_toothbrush_k1_seed4_anomalydino_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_toothbrush_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9540805335930462`
- `auroc`: `0.9`
- `brier`: `0.2857142857142857`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2857142857142857`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004782673548020068`
- `max_f1`: `0.9354838709677419`
- `model_storage_mb`: `2.00537109375`
- `nll`: `5.263051646836459`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_toothbrush_k1_seed4_anomalydino_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
