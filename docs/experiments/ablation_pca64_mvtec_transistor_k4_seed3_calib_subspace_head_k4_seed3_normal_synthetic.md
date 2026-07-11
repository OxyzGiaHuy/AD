# Run ablation_pca64_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_transistor_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7989086673278355`
- `auroc`: `0.8608333333333333`
- `brier`: `0.4216517046732294`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.46749372631544245`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0024186297319829463`
- `max_f1`: `0.7674418604651163`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `3.0802382317092802`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
