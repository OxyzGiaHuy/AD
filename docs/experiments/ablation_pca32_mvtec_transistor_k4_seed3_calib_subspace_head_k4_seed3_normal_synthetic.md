# Run ablation_pca32_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7912973598187166`
- `auroc`: `0.8233333333333334`
- `brier`: `0.4910940388480158`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.5318046581745147`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0026675952784717084`
- `max_f1`: `0.7058823529411765`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.8976036195998425`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
