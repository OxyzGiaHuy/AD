# Run ablation_pca32_mvtec_carpet_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9993839222710742`
- `auroc`: `0.9979935794542536`
- `brier`: `0.18634598741814132`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.20706862236699486`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.002877141325137554`
- `max_f1`: `0.9886363636363636`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.1518321550878488`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
