# Run ablation_pca32_mvtec_carpet_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_carpet_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9991270920549259`
- `auroc`: `0.9971910112359551`
- `brier`: `0.09983655772460594`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.13516110898210454`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0018900488145076311`
- `max_f1`: `0.9834254143646409`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.3513536441889207`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_carpet_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
