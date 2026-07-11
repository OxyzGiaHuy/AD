# Run ablation_pca32_mvtec_metal_nut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9885059089693211`
- `auroc`: `0.9535679374389052`
- `brier`: `0.06670220953245581`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.07288130821417203`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.002494866044624992`
- `max_f1`: `0.9574468085106383`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.22469901619309784`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
