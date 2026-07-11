# Run ablation_pca32_mvtec_bottle_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_bottle_k8_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9916158312868186`
- `auroc`: `0.9761904761904762`
- `brier`: `0.0874466992695106`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10239896590748518`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.003690603492130716`
- `max_f1`: `0.9763779527559056`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.4133873018174192`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_bottle_k8_seed4_calib_subspace_head_k8_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
