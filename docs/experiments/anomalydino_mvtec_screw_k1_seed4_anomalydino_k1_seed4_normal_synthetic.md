# Run anomalydino_mvtec_screw_k1_seed4_anomalydino_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_screw_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.80968937536495`
- `auroc`: `0.6540274646443943`
- `brier`: `0.25625`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25625`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004845170548651368`
- `max_f1`: `0.8614232209737828`
- `model_storage_mb`: `2.00537109375`
- `nll`: `4.720299446787697`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_screw_k1_seed4_anomalydino_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
