# Run ablation_pca32_mvtec_capsule_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9264809028480846`
- `auroc`: `0.7618667730355005`
- `brier`: `0.11088749362642954`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.10265911472114655`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0020719499355464272`
- `max_f1`: `0.9285714285714286`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.3805249398609786`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
