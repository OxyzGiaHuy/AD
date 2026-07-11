# Run ablation_calib_upper_mvtec_hazelnut_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9874586874731035`
- `auroc`: `0.9793650793650793`
- `brier`: `0.08989328362137232`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.1343337578102223`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015657826064570436`
- `max_f1`: `0.9333333333333333`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.28172143744792943`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
