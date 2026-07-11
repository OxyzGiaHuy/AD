# Run ablation_calib_upper_mvtec_screw_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.888030540196485`
- `auroc`: `0.7678410117434508`
- `brier`: `0.20354848275222107`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.18976749542275534`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017826217132926787`
- `max_f1`: `0.8617886178861789`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.8275208334477973`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
