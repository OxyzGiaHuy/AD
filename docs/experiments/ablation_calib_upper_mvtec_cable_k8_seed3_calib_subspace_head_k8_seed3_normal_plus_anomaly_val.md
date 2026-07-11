# Run ablation_calib_upper_mvtec_cable_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9309021136514497`
- `auroc`: `0.8778562525965933`
- `brier`: `0.31276909433748534`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.33839863834651646`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002950146886790898`
- `max_f1`: `0.8588957055214724`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.9804139246843776`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k8_seed3_calib_subspace_head_k8_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
