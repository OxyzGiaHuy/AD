# Run ablation_pca32_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_wood_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9854014005150866`
- `auroc`: `0.9578947368421052`
- `brier`: `0.16324993387380482`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.1845083860562572`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0014141921567011482`
- `max_f1`: `0.9666666666666667`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.2254024910601489`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_wood_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
