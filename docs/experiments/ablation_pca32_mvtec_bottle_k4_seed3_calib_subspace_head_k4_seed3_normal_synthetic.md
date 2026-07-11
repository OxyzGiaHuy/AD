# Run ablation_pca32_mvtec_bottle_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9757769341673671`
- `auroc`: `0.9452380952380952`
- `brier`: `0.16311388784342276`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18043013306962974`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013943035379949823`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.772246576896487`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
