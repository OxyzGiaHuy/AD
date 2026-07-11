# Run ablation_calib_upper_mvtec_transistor_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8976218492524526`
- `auroc`: `0.9291666666666667`
- `brier`: `0.5841726469593208`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.6027945335954427`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017850622922802966`
- `max_f1`: `0.8333333333333334`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.5953996888442257`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k1_seed1_calib_subspace_head_k1_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
