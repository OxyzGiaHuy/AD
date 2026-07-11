# Run ablation_calib_upper_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9919964887299237`
- `auroc`: `0.9702380952380952`
- `brier`: `0.05400987075819993`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.04462394684131416`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0027895052302277313`
- `max_f1`: `0.9595375722543352`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.17917099192332991`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k4_seed0_calib_subspace_head_k4_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
