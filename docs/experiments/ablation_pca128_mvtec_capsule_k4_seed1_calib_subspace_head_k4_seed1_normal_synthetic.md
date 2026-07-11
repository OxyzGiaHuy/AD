# Run ablation_pca128_mvtec_capsule_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_capsule_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9843301803199208`
- `auroc`: `0.9285999202233746`
- `brier`: `0.13885978997159953`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.15077706990819992`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0028151673772795634`
- `max_f1`: `0.9545454545454546`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `0.6008701648595619`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_capsule_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
