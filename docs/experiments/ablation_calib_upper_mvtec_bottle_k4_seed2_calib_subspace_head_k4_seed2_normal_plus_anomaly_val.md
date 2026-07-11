# Run ablation_calib_upper_mvtec_bottle_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_bottle_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9942131263528626`
- `auroc`: `0.9850877192982456`
- `brier`: `0.07058102712930592`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.11292599344795408`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002663523369988838`
- `max_f1`: `0.9827586206896551`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.22904341990943514`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_bottle_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
