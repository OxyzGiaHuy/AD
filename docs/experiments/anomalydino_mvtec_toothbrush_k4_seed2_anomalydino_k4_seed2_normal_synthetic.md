# Run anomalydino_mvtec_toothbrush_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_toothbrush_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9334800726791179`
- `auroc`: `0.8805555555555555`
- `brier`: `0.6878058250165472`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6909174169413745`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012317671351844356`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `6.0`
- `nll`: `2.8570905452172464`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_toothbrush_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
