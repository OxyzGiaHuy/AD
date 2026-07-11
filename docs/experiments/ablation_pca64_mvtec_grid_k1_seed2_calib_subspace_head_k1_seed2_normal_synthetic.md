# Run ablation_pca64_mvtec_grid_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_grid_k1_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9598245198594175`
- `auroc`: `0.9055973266499582`
- `brier`: `0.26922513765181194`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2692279525292226`
- `k_shot`: `1`
- `latency_sec_per_image`: `0.0015860071214727866`
- `max_f1`: `0.9203539823008849`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `4.264624898896346`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `1369`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_grid_k1_seed2_calib_subspace_head_k1_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
