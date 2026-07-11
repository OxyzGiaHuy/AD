# Run ablation_calib_upper_mvtec_cable_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9231755617520009`
- `auroc`: `0.874740340673037`
- `brier`: `0.3239061430628274`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.3442716869056647`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00165885495325775`
- `max_f1`: `0.8306010928961749`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.999566209078868`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
