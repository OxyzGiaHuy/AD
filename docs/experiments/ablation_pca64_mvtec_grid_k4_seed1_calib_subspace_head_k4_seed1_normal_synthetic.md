# Run ablation_pca64_mvtec_grid_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_grid_k4_seed1.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `1.0`
- `auroc`: `1.0`
- `brier`: `0.2223847891470942`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.23987442063979608`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.001984043930394527`
- `max_f1`: `1.0`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.822365627642337`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `1`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_grid_k4_seed1_calib_subspace_head_k4_seed1_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
