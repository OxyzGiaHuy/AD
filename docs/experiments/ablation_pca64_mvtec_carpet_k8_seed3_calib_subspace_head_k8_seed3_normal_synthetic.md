# Run ablation_pca64_mvtec_carpet_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9970797779244166`
- `auroc`: `0.9907704654895666`
- `brier`: `0.08372656666313512`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10323400501734936`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025310683995485306`
- `max_f1`: `0.978021978021978`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6448530698016037`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
