# Run ablation_pca64_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_ablations/ablation_pca64_mvtec_tile_k4_seed2.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9890825784271374`
- `auroc`: `0.9736652236652237`
- `brier`: `0.1765342533077917`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.2033104751513809`
- `k_shot`: `4`
- `latency_sec_per_image`: `0.002897832303857192`
- `max_f1`: `0.96`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `1.2261395421853671`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `2`
- `support_patch_count`: `5476`

## Notes

- Predictions written to outputs/ablation_pca64_mvtec_tile_k4_seed2_calib_subspace_head_k4_seed2_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
