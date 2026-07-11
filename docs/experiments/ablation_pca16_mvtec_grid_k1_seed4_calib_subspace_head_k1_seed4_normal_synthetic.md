# Run ablation_pca16_mvtec_grid_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_grid_k1_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9961880146893601`
- `auroc`: `0.9891395154553049`
- `brier`: `0.2677024618692163`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2683812525027838`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0016858623100396914`
- `max_f1`: `0.9739130434782609`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `1.7355118660875282`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_grid_k1_seed4_calib_subspace_head_k1_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
