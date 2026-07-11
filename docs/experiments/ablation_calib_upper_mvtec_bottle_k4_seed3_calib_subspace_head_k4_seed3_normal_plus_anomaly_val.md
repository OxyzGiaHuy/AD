# Run ablation_calib_upper_mvtec_bottle_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_bottle_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.984810514408284`
- `auroc`: `0.9640350877192982`
- `brier`: `0.08440337701365347`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.11197151330771382`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014395416750536336`
- `max_f1`: `0.9572649572649573`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.2974427940027478`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_bottle_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
