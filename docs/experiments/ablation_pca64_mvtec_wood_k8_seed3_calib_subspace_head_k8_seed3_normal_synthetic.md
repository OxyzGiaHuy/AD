# Run ablation_pca64_mvtec_wood_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_wood_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9842801569004818`
- `auroc`: `0.9587719298245614`
- `brier`: `0.13190535962390662`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.143384635284885`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0025609564036130905`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.034360791700713`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_wood_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
