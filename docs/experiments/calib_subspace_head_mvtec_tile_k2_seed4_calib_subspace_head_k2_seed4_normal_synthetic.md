# Run calib_subspace_head_mvtec_tile_k2_seed4_calib_subspace_head_k2_seed4_normal_synthetic

- Command: `/home/crl/AD/src/run_experiment.py --config configs/generated/mvtec_full/calib_subspace_head_mvtec_tile_k2_seed4.yaml`
- Dataset: `mvtec`
- Model: `calib_subspace_head`

## Metrics

- `ap`: `0.9941746082680379`
- `auroc`: `0.9862914862914863`
- `brier`: `0.15536515921119814`
- `calibration_anomaly_val_count`: `0`
- `ece`: `0.18581564615393048`
- `k_shot`: `2`
- `latency_sec_per_image`: `0.0012989184604241298`
- `max_f1`: `0.9710982658959537`
- `model_storage_mb`: `0.4721870422363281`
- `nll`: `0.6887287752057446`
- `peak_memory_mb`: `nan`
- `pixel_auroc`: `nan`
- `pro`: `nan`
- `seed`: `4`
- `support_patch_count`: `2738`

## Notes

- Predictions written to outputs/calib_subspace_head_mvtec_tile_k2_seed4_calib_subspace_head_k2_seed4_normal_synthetic/predictions.parquet
- Patch heatmap tensor saved as patch_scores.npy
