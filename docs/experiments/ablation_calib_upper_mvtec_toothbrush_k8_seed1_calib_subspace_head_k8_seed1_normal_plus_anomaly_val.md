# Run ablation_calib_upper_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9905752532317028`
- `auroc`: `0.9783950617283951`
- `brier`: `0.05152853488212345`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.06794549541500136`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0038211862914837324`
- `max_f1`: `0.9642857142857143`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.18358748720067938`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
