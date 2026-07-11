# Run ablation_pca16_mvtec_carpet_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_carpet_k8_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9979946905382658`
- `auroc`: `0.9935794542536116`
- `brier`: `0.08555418816317192`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.09912040367977232`
- `k_shot`: `8`
- `latency_sec_per_image`: `0.0014156379187718416`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.29863838992896724`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `10952`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_carpet_k8_seed2_calib_subspace_head_k8_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
