# Run ablation_pca32_mvtec_screw_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_screw_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8707323175683089`
- `auroc`: `0.7169501947120311`
- `brier`: `0.1834602677264885`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1707382931374013`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002484871924389154`
- `max_f1`: `0.8686131386861314`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.6544655284113339`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_screw_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
