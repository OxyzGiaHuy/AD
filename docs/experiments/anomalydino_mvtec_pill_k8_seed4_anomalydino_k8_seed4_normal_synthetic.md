# Run anomalydino_mvtec_pill_k8_seed4_anomalydino_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_pill_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9851343635708252`
- `auroc`: `0.933442444080742`
- `brier`: `0.7487454632676306`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.782443606791025`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0123201676359969`
- `max_f1`: `0.9547038327526133`
- `model_storage_mb`: `6.0`
- `nll`: `2.412058986080279`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_pill_k8_seed4_anomalydino_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
