# Run ablation_pca64_mvtec_capsule_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9435474181617609`
- `auroc`: `0.7989629038691664`
- `brier`: `0.12551717240221172`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1273262180955939`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0038933369726168385`
- `max_f1`: `0.933920704845815`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.0087351221278704`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_capsule_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
