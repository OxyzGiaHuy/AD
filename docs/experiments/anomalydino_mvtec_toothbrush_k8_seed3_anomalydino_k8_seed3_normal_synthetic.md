# Run anomalydino_mvtec_toothbrush_k8_seed3_anomalydino_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_toothbrush_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9108159287698404`
- `auroc`: `0.8694444444444445`
- `brier`: `0.7047650404395586`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7054412322384971`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012472041749528475`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `6.0`
- `nll`: `3.5956834431550795`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_toothbrush_k8_seed3_anomalydino_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
