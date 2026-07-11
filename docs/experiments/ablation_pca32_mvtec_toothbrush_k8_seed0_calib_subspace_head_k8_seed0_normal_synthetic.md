# Run ablation_pca32_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_toothbrush_k8_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9869117951443219`
- `auroc`: `0.9666666666666667`
- `brier`: `0.1008640397772366`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.125360253000898`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0037569931397835412`
- `max_f1`: `0.9523809523809523`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.40784219775369773`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_toothbrush_k8_seed0_calib_subspace_head_k8_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
