# Run calib_subspace_head_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_cable_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9566936078738982`
- `auroc`: `0.9104197901049476`
- `brier`: `0.19643530628820247`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.21433165356982495`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001293374312420686`
- `max_f1`: `0.8994082840236687`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6952080624439599`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_cable_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
