# Run ablation_pca32_mvtec_transistor_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_transistor_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.7581714739208826`
- `auroc`: `0.80375`
- `brier`: `0.2298922429591014`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.22572413973743097`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0017928759939968585`
- `max_f1`: `0.6888888888888889`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.7586426927772534`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_transistor_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
