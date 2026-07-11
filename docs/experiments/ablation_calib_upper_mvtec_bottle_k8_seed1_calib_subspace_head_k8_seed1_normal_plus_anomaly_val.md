# Run ablation_calib_upper_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_bottle_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9952012508699369`
- `auroc`: `0.987719298245614`
- `brier`: `0.032221529462967156`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.0749997335377258`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002884647651732742`
- `max_f1`: `0.991304347826087`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.16164462228457663`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_bottle_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
