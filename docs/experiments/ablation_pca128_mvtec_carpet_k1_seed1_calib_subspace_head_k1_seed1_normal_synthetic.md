# Run ablation_pca128_mvtec_carpet_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_carpet_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9993839222710742`
- `auroc`: `0.9979935794542536`
- `brier`: `0.17635367452812314`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.201642367320183`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0037071844960889244`
- `max_f1`: `0.9886363636363636`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.7767550715468641`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_carpet_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
