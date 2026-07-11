# Run ablation_calib_upper_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7814052202562879`
- `auroc`: `0.6117886178861789`
- `brier`: `0.23805212507010484`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.23696302847574222`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015134937286176938`
- `max_f1`: `0.8653061224489796`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.1003965944522716`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
