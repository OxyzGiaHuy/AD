# Run ablation_pca64_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7926022841494043`
- `auroc`: `0.8416666666666667`
- `brier`: `0.3532785300410072`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.4028891320154071`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0026348153315484523`
- `max_f1`: `0.7441860465116279`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.743500758605476`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
