# Run ablation_calib_upper_mvtec_zipper_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9788958007433537`
- `auroc`: `0.9305555555555556`
- `brier`: `0.11959916906790717`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.1368344978562423`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016557961170162473`
- `max_f1`: `0.9344978165938864`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.4392099863385005`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k4_seed2_calib_subspace_head_k4_seed2_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
