# Run ablation_pca128_mvtec_toothbrush_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_toothbrush_k1_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9874658289241622`
- `auroc`: `0.9666666666666667`
- `brier`: `0.28547251441777793`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.28559310237566626`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0017040129307480086`
- `max_f1`: `0.9354838709677419`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `3.34734884868112`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_toothbrush_k1_seed3_calib_subspace_head_k1_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
