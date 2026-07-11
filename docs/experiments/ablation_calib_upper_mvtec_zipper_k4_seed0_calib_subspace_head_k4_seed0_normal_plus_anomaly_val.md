# Run ablation_calib_upper_mvtec_zipper_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9852309332684394`
- `auroc`: `0.9513888888888888`
- `brier`: `0.09481686609547718`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.11297648735344402`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0023145659959742`
- `max_f1`: `0.9464285714285714`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3193382170840883`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
