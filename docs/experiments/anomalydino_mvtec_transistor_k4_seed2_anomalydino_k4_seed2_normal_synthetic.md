# Run anomalydino_mvtec_transistor_k4_seed2_anomalydino_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_transistor_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8647290533259376`
- `auroc`: `0.8979166666666667`
- `brier`: `0.39573479924292926`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3914972069556825`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.01257807580754161`
- `max_f1`: `0.821917808219178`
- `model_storage_mb`: `6.0`
- `nll`: `2.139756263814438`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_transistor_k4_seed2_anomalydino_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
