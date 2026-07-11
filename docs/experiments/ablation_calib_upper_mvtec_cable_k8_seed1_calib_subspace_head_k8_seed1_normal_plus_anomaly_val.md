# Run ablation_calib_upper_mvtec_cable_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_cable_k8_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9454277434477294`
- `auroc`: `0.8973826339842127`
- `brier`: `0.20718356660102852`
- `calibration_anomaly_val_count`: `9`
- `ece`: `0.2373833858163644`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.00194748802810696`
- `max_f1`: `0.89171974522293`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.5851272241907544`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_cable_k8_seed1_calib_subspace_head_k8_seed1_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
