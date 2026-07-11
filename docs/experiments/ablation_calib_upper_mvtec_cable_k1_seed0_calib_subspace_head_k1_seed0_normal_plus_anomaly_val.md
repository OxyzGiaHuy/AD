# Run ablation_calib_upper_mvtec_cable_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.947753663275665`
- `auroc`: `0.9000830909846281`
- `brier`: `0.3588438530188137`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.37599180987540703`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0021220741278313577`
- `max_f1`: `0.8831168831168831`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.1821915412389958`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
