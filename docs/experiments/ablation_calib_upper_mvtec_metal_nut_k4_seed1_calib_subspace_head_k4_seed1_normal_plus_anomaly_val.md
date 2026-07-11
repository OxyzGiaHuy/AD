# Run ablation_calib_upper_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9882698429042821`
- `auroc`: `0.9577922077922078`
- `brier`: `0.12932118155032762`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.15166403887406843`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.009249729350349813`
- `max_f1`: `0.9529411764705882`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4360122548992767`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
