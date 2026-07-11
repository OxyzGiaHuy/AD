# Run ablation_calib_upper_mvtec_metal_nut_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9967672253487453`
- `auroc`: `0.987012987012987`
- `brier`: `0.09408706455813423`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.12069155194989915`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015370645296742332`
- `max_f1`: `0.9693251533742331`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3134395696553323`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
