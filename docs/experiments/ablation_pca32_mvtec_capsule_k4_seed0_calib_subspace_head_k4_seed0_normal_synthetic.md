# Run ablation_pca32_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8798845237821613`
- `auroc`: `0.6673314718787395`
- `brier`: `0.1221777570069514`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.11097741045170664`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002889932556585832`
- `max_f1`: `0.9203539823008849`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.4623332168002672`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
