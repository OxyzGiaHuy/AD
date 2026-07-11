# Run ablation_pca128_mvtec_leather_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_leather_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.2337924676783888`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2453030275721703`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016559039603077595`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.0072718046287437`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_leather_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
