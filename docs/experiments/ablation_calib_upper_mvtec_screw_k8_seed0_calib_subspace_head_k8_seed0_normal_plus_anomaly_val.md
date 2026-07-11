# Run ablation_calib_upper_mvtec_screw_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_screw_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.899098663617213`
- `auroc`: `0.8197831978319783`
- `brier`: `0.143892987720672`
- `calibration_anomaly_val_count`: `11`
- `ece`: `0.1265026699476594`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0013561848201007652`
- `max_f1`: `0.8916666666666667`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.49688329577103496`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_screw_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
