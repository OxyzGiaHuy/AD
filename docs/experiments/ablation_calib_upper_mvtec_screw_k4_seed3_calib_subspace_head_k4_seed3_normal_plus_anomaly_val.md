# Run ablation_calib_upper_mvtec_screw_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8611853108461971`
- `auroc`: `0.7502258355916892`
- `brier`: `0.1794633132107309`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.15622285953504123`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017573558694164225`
- `max_f1`: `0.8669527896995708`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6901763393516925`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
