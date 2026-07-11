# Run ablation_pca32_mvtec_screw_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8633101158067166`
- `auroc`: `0.682721869235499`
- `brier`: `0.2096627705687224`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.17391662091831678`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017022747197188437`
- `max_f1`: `0.8614232209737828`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6667971341429122`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
