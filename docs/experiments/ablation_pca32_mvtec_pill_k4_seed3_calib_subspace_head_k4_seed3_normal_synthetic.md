# Run ablation_pca32_mvtec_pill_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_pill_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9865699376656435`
- `auroc`: `0.930987452264048`
- `brier`: `0.08948079786812219`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09730178590314636`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001974624018380028`
- `max_f1`: `0.9419795221843004`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.3181135076962064`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_pill_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
