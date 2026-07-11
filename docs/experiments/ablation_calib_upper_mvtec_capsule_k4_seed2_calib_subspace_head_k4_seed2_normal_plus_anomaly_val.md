# Run ablation_calib_upper_mvtec_capsule_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_capsule_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9639649876752777`
- `auroc`: `0.8603425559947299`
- `brier`: `0.12350263887128257`
- `calibration_anomaly_val_count`: `10`
- `ece`: `0.10938479213929567`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020754144786566983`
- `max_f1`: `0.919431279620853`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.42111588622607415`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_capsule_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
