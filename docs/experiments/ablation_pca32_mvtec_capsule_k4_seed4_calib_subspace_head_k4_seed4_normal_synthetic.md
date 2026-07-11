# Run ablation_pca32_mvtec_capsule_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca32_mvtec_capsule_k4_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9376402757405515`
- `auroc`: `0.7746310331072995`
- `brier`: `0.12384597242446094`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.12161267260936173`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.00205537523001884`
- `max_f1`: `0.9184549356223176`
- `model_storage_mb`: `0.4253120422363281`
- `nll`: `0.621140994726971`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca32_mvtec_capsule_k4_seed4_calib_subspace_head_k4_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
