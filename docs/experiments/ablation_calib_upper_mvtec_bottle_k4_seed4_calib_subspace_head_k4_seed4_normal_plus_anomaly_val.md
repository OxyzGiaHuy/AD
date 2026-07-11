# Run ablation_calib_upper_mvtec_bottle_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_bottle_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9969892206135925`
- `auroc`: `0.9912280701754386`
- `brier`: `0.05057460180071502`
- `calibration_anomaly_val_count`: `6`
- `ece`: `0.07889824999230251`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016668824745076044`
- `max_f1`: `0.9824561403508771`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.16447766179980283`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_bottle_k4_seed4_calib_subspace_head_k4_seed4_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
