# Run ablation_pca128_mvtec_grid_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca128_mvtec_grid_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.2657864738518722`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.267494498155056`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0025942549109458923`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.5659370422363281`
- `nll`: `1.5563973479256974`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca128_mvtec_grid_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
