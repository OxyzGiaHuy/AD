# Run anomalydino_mvtec_pill_k1_seed3_anomalydino_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_pill_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9677471554345506`
- `auroc`: `0.8592471358428805`
- `brier`: `0.15568862275449102`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15568862275449102`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0047184162867997224`
- `max_f1`: `0.9351535836177475`
- `model_storage_mb`: `2.00537109375`
- `nll`: `2.867890422886933`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_pill_k1_seed3_anomalydino_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
