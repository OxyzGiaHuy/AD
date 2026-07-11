# Run ablation_pca16_mvtec_capsule_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_capsule_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9146245769088011`
- `auroc`: `0.713203031511767`
- `brier`: `0.27435293420102635`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2877512569549722`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002361786283665534`
- `max_f1`: `0.9191489361702128`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.304642936189219`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_capsule_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
