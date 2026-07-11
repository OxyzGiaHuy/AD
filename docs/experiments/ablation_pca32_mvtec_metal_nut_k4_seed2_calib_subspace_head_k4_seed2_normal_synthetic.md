# Run ablation_pca32_mvtec_metal_nut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_metal_nut_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9787059020572612`
- `auroc`: `0.9208211143695014`
- `brier`: `0.14739821150420607`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15886119008064264`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0019114517323348833`
- `max_f1`: `0.9533678756476683`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.7062422599362693`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_metal_nut_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
