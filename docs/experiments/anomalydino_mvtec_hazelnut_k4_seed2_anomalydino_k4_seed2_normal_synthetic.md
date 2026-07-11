# Run anomalydino_mvtec_hazelnut_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_hazelnut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.994098603996609`
- `auroc`: `0.9892857142857143`
- `brier`: `0.6306736148955059`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6296110971703787`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012834075533530928`
- `max_f1`: `0.9571428571428572`
- `model_storage_mb`: `6.0`
- `nll`: `3.4855017002985633`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_hazelnut_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
