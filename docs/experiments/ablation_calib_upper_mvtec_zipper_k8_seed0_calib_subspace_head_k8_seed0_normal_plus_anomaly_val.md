# Run ablation_calib_upper_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9856495166618496`
- `auroc`: `0.953125`
- `brier`: `0.09436073395562176`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.10311394790187477`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023212099447846414`
- `max_f1`: `0.9464285714285714`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.33022962126925864`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
