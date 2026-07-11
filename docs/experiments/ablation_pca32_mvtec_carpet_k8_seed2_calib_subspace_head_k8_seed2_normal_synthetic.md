# Run ablation_pca32_mvtec_carpet_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9994920791527584`
- `auroc`: `0.9983948635634029`
- `brier`: `0.09478425169776614`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15138237082805386`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.001476187991280841`
- `max_f1`: `0.994413407821229`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.35602222667366806`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
