# Run ablation_calib_upper_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9305603284067886`
- `auroc`: `0.7672375933245499`
- `brier`: `0.14308590395645687`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.1274815553028259`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0023907502868869266`
- `max_f1`: `0.916256157635468`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5543008399132575`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
