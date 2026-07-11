# Run anomalydino_mvtec_screw_k2_seed3_anomalydino_k2_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_screw_k2_seed3.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8269776206602099`
- `auroc`: `0.6837466693994672`
- `brier`: `0.25625`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.25625`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.008650469535496086`
- `max_f1`: `0.8821292775665399`
- `model_storage_mb`: `4.0107421875`
- `nll`: `4.720299446787697`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/anomalydino_mvtec_screw_k2_seed3_anomalydino_k2_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
