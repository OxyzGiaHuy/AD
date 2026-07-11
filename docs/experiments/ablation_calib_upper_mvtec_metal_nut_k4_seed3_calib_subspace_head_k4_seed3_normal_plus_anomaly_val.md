# Run ablation_calib_upper_mvtec_metal_nut_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9947574559819281`
- `auroc`: `0.9788961038961039`
- `brier`: `0.0687852812180022`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.09756719581079937`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002317111517460841`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.21136535677065535`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
