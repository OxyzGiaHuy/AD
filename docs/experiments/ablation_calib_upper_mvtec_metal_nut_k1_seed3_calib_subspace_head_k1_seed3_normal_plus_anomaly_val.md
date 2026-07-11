# Run ablation_calib_upper_mvtec_metal_nut_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9913022457552636`
- `auroc`: `0.9664502164502164`
- `brier`: `0.12428226568841864`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.14188426367516788`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002142179880361512`
- `max_f1`: `0.9529411764705882`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.39428257835069147`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
