# Run ablation_calib_upper_mvtec_screw_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8945274991679834`
- `auroc`: `0.790650406504065`
- `brier`: `0.16910371835066576`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.15449891693815088`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0016111767282021925`
- `max_f1`: `0.8702928870292888`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5837699125917706`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k8_seed4_calib_subspace_head_k8_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
