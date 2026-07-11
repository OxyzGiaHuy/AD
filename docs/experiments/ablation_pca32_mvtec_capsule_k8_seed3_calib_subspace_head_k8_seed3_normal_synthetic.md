# Run ablation_pca32_mvtec_capsule_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k8_seed3.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8960375656212631`
- `auroc`: `0.7040287195851616`
- `brier`: `0.12351590015957295`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10385867146154248`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0020999654873528266`
- `max_f1`: `0.9285714285714286`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.43953826128013157`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `3`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k8_seed3_calib_subspace_head_k8_seed3_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
