# Run ablation_calib_upper_mvtec_cable_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9549243274893354`
- `auroc`: `0.9148317407561279`
- `brier`: `0.25364579474722887`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.2872808884221611`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0029774589979268133`
- `max_f1`: `0.89171974522293`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6969350305465428`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
