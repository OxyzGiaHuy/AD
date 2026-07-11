# Run ablation_pca16_mvtec_grid_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9463781672478069`
- `auroc`: `0.8596491228070176`
- `brier`: `0.11469303385313354`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14281817637264538`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0015168869151518894`
- `max_f1`: `0.896`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.3554752329664463`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
