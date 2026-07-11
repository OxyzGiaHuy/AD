# Run ablation_calib_upper_mvtec_capsule_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.970088294910447`
- `auroc`: `0.8880105401844532`
- `brier`: `0.11701462098027195`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.08496833433870414`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023832935229188106`
- `max_f1`: `0.9320388349514563`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.36244236470591035`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
