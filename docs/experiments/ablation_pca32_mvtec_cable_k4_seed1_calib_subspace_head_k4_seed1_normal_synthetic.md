# Run ablation_pca32_mvtec_cable_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_cable_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.936854357365032`
- `auroc`: `0.8768740629685158`
- `brier`: `0.31039299925117275`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.32120092619870166`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0021382766341169674`
- `max_f1`: `0.8540540540540541`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `2.200147254795012`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_cable_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
