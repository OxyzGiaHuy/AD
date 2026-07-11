# Run ablation_pca32_mvtec_capsule_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k1_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.8423450741153621`
- `auroc`: `0.6406063023534104`
- `brier`: `0.17424178214429709`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.174242103190133`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0019099700236410806`
- `max_f1`: `0.9276595744680851`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `3.049768879236901`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k1_seed1_calib_subspace_head_k1_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
