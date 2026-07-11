# Run ablation_pca16_mvtec_tile_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca16_mvtec_tile_k4_seed0.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9928658812919035`
- `auroc`: `0.983044733044733`
- `brier`: `0.11596380057925008`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.14550854520410558`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.0013412079877323574`
- `max_f1`: `0.9704142011834319`
- `model_storage_mb`: `0.4018745422363281`
- `nll`: `0.363010629082242`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `0`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca16_mvtec_tile_k4_seed0_calib_subspace_head_k4_seed0_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
