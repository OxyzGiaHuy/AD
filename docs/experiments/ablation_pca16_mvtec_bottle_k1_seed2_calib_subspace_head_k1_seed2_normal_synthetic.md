# Run ablation_pca16_mvtec_bottle_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_bottle_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9344937475921659`
- `auroc`: `0.8682539682539683`
- `brier`: `0.24037764946679435`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.24066294819475653`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.00266576627920191`
- `max_f1`: `0.9130434782608695`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `2.4325961582237676`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_bottle_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
