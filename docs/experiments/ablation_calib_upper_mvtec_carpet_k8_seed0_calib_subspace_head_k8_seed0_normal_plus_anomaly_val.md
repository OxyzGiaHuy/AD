# Run ablation_calib_upper_mvtec_carpet_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_carpet_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.999386431743066`
- `auroc`: `0.9982363315696648`
- `brier`: `0.018189469829511636`
- `calibration_anomaly_val_count`: `8`
- `ece`: `0.04885375207512202`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002056423198739323`
- `max_f1`: `0.9938650306748467`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.06966931720562179`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_carpet_k8_seed0_calib_subspace_head_k8_seed0_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
