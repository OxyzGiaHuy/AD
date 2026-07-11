# Run ablation_calib_upper_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_pill_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9878484465523159`
- `auroc`: `0.9473046638400969`
- `brier`: `0.06666510494444274`
- `calibration_anomaly_val_count`: `14`
- `ece`: `0.06092122393155023`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001611833990204568`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.21793776981580826`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_pill_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
