# Run anomalydino_mvtec_screw_k4_seed0_anomalydino_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_screw_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8970935081492081`
- `auroc`: `0.8159458905513425`
- `brier`: `0.727844738256008`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.7313017989363289`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.012677177879959345`
- `max_f1`: `0.8782287822878229`
- `model_storage_mb`: `6.0`
- `nll`: `3.407162027458996`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/anomalydino_mvtec_screw_k4_seed0_anomalydino_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
