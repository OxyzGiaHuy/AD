# Run ablation_calib_upper_mvtec_zipper_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9810245073529583`
- `auroc`: `0.9395254629629629`
- `brier`: `0.11947785617840369`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.1313876931156431`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014310230500996113`
- `max_f1`: `0.9427312775330396`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3714109482850964`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
