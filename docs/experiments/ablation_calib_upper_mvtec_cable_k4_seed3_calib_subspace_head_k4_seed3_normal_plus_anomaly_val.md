# Run ablation_calib_upper_mvtec_cable_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9290296059004178`
- `auroc`: `0.8803489821354383`
- `brier`: `0.3114009030255614`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.3376172303307987`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019677376097187085`
- `max_f1`: `0.8470588235294118`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.067116460497009`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
