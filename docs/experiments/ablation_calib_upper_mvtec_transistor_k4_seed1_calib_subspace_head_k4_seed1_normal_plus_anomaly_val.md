# Run ablation_calib_upper_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7692082075965695`
- `auroc`: `0.8171296296296297`
- `brier`: `0.5148488101158158`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.5560595138619344`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0016830114764161408`
- `max_f1`: `0.676923076923077`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.7227206949052065`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k4_seed1_calib_subspace_head_k4_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
