# Run ablation_calib_upper_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_carpet_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9998494429388738`
- `auroc`: `0.9995590828924162`
- `brier`: `0.02583305363845874`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.06667899704375947`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002483016409731786`
- `max_f1`: `0.9938650306748467`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.10279105139449322`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_carpet_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
