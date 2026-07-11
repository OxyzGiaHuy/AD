# Run ablation_calib_upper_mvtec_metal_nut_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_metal_nut_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9894169154966208`
- `auroc`: `0.9604978354978355`
- `brier`: `0.1517619073567678`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.16839229554500218`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0024520514251769716`
- `max_f1`: `0.9585798816568047`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.528862824545985`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_metal_nut_k1_seed2_calib_subspace_head_k1_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
