# Run ablation_calib_upper_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9874981437368998`
- `auroc`: `0.9550865800865801`
- `brier`: `0.06711580386418242`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.05722411785204458`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0032433061421198667`
- `max_f1`: `0.9485714285714286`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.21569142370446998`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
