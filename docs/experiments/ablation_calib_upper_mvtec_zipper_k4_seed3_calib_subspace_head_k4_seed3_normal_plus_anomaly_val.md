# Run ablation_calib_upper_mvtec_zipper_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_zipper_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.983347141307356`
- `auroc`: `0.9456018518518519`
- `brier`: `0.11972860545705562`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.139171761061464`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.003027318378112146`
- `max_f1`: `0.9427312775330396`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.38901545626168527`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_zipper_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
