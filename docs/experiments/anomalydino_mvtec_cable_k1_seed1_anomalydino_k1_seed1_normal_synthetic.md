# Run anomalydino_mvtec_cable_k1_seed1_anomalydino_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/anomalydino_mvtec_cable_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `anomalydino`

## Metrics

- `ap`: `0.8977189336698761`
- `auroc`: `0.8095952023988006`
- `brier`: `0.38666666666666666`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.3866666666666667`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.004743435159325599`
- `max_f1`: `0.7906976744186046`
- `model_storage_mb`: `2.00537109375`
- `nll`: `7.122663225185343`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/anomalydino_mvtec_cable_k1_seed1_anomalydino_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
