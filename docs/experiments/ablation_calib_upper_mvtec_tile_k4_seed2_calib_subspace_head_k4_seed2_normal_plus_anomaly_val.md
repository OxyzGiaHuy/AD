# Run ablation_calib_upper_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9880942450284527`
- `auroc`: `0.9740829346092504`
- `brier`: `0.11077656939909555`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.14672662960279967`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021694140560036407`
- `max_f1`: `0.9559748427672956`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.3379054641573237`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
