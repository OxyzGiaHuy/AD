# Run ablation_pca64_mvtec_carpet_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_carpet_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9988757132041219`
- `auroc`: `0.9963884430176565`
- `brier`: `0.1027919491534704`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1178781842518375`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0042765830667355125`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6201251532729497`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_carpet_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
