# Run ablation_pca64_mvtec_toothbrush_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_toothbrush_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.978379479997127`
- `auroc`: `0.9416666666666667`
- `brier`: `0.27860606491087614`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28199551502863573`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0014551694371870586`
- `max_f1`: `0.9090909090909091`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `2.8662405839700633`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_toothbrush_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
