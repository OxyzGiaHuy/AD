# Run ablation_calib_upper_mvtec_leather_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_leather_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.0012659596629457238`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.018337922632370336`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013989886349957922`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.01903580082748385`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_leather_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
