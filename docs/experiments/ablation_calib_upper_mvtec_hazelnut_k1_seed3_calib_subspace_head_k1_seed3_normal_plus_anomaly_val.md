# Run ablation_calib_upper_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_calib_upper_mvtec_hazelnut_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9977755454907143`
- `auroc`: `0.9964285714285714`
- `brier`: `0.2349497771351265`
- `calibration_anomaly_val_count`: `7`
- `ece`: `0.2879572985241714`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0022696489739475897`
- `max_f1`: `0.9763779527559056`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6259515743515153`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_calib_upper_mvtec_hazelnut_k1_seed3_calib_subspace_head_k1_seed3_normal_plus_anomaly_val/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
