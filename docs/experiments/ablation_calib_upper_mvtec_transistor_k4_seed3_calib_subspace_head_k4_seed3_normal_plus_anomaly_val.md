# Run ablation_calib_upper_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7809330640511902`
- `auroc`: `0.8555555555555555`
- `brier`: `0.23573588170339868`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.24630380185165754`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00145931801913927`
- `max_f1`: `0.7435897435897436`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.1113061044022543`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
