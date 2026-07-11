# Run ablation_calib_upper_mvtec_transistor_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9027108962439061`
- `auroc`: `0.9291666666666667`
- `brier`: `0.35684188337517053`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.4299418213001142`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0022700867460419736`
- `max_f1`: `0.821917808219178`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.3541197374384062`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
