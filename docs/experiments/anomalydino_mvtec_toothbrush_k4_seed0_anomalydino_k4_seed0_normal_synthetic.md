# Run anomalydino_mvtec_toothbrush_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_toothbrush_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.9328817594445421`
- `auroc`: `0.8861111111111111`
- `brier`: `0.706914922126807`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7073437253046515`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.013024706659572465`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `6.0`
- `nll`: `3.776577757035215`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_toothbrush_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
