# Run ablation_calib_upper_mvtec_toothbrush_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_toothbrush_k1_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.990351026155624`
- `auroc`: `0.9783950617283951`
- `brier`: `0.21255509193813446`
- `calibration_anomaly_val_count`: `3`
- `ece`: `0.24695138442210662`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.001608233182476117`
- `max_f1`: `0.9642857142857143`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.748999806087804`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_toothbrush_k1_seed0_calib_subspace_head_k1_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
