# Run ablation_pca32_mvtec_carpet_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9987454156439238`
- `auroc`: `0.9959871589085072`
- `brier`: `0.21072798609155768`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22232647482146564`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0023825703363897456`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.5958784375871087`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
