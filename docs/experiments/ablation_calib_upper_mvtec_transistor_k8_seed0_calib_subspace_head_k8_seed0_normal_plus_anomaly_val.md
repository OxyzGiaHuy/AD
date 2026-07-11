# Run ablation_calib_upper_mvtec_transistor_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_transistor_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7926505762678667`
- `auroc`: `0.8407407407407408`
- `brier`: `0.19762881683027267`
- `calibration_anomaly_val_count`: `4`
- `ece`: `0.16924826860728592`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025588821542138853`
- `max_f1`: `0.7142857142857143`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6806259478818975`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_transistor_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
