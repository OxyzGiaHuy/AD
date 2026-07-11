# Run ablation_calib_upper_mvtec_zipper_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9861119191486121`
- `auroc`: `0.9537037037037037`
- `brier`: `0.09349966449557634`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.10592060216835564`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013947256308581148`
- `max_f1`: `0.9432314410480349`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3178406361754191`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
