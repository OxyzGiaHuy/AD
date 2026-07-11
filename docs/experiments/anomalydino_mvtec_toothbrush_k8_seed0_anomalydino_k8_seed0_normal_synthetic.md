# Run anomalydino_mvtec_toothbrush_k8_seed0_anomalydino_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9408657661785488`
- `auroc`: `0.8916666666666667`
- `brier`: `0.6905400842575378`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.6924329045494753`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.012647123076021671`
- `max_f1`: `0.9375`
- `model_storage_mb`: `6.0`
- `nll`: `2.937298356400987`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/anomalydino_mvtec_toothbrush_k8_seed0_anomalydino_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
