# Run ablation_calib_upper_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9225201971686913`
- `auroc`: `0.7444005270092227`
- `brier`: `0.14110270907280542`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.13005429654779133`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002206973120814464`
- `max_f1`: `0.9073170731707317`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.527546382476775`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
