# Run anomalydino_mvtec_zipper_k1_seed0_anomalydino_k1_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_zipper_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9952587236273379`
- `auroc`: `0.9831932773109243`
- `brier`: `0.2119205298013245`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21192052980132448`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0048296153422025655`
- `max_f1`: `0.9754098360655737`
- `model_storage_mb`: `2.00537109375`
- `nll`: `3.9037204293753867`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_zipper_k1_seed0_anomalydino_k1_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
