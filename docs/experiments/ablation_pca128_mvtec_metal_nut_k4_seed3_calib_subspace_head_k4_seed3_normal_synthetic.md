# Run ablation_pca128_mvtec_metal_nut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_metal_nut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9975719830321266`
- `auroc`: `0.9897360703812317`
- `brier`: `0.10505014109622343`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1271301369952119`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0017373184794964999`
- `max_f1`: `0.9738219895287958`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.44953888168089806`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_metal_nut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
