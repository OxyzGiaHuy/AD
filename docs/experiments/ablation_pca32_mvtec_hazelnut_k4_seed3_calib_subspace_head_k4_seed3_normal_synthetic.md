# Run ablation_pca32_mvtec_hazelnut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_hazelnut_k4_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9781231286455636`
- `auroc`: `0.9671428571428572`
- `brier`: `0.31328734642362666`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.334137210520831`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0015047563070600682`
- `max_f1`: `0.9496402877697842`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `1.1331495577278146`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_hazelnut_k4_seed3_calib_subspace_head_k4_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
